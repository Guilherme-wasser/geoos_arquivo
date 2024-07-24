const config = require("./lib/Config");
const path = require('path');
const fs = require('fs').promises; // Importe fs.promises para usar async/await
const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

const MohidOilSimulation = require("./Oil_Spill_Tool/MohidOilSimulation");

async function startHTTPServer() {
    try {
        await (require("./lib/MongoDB")).init();
        const zServer = require("./lib/z-server");
        const express = require('express');
        const app = express();
        const bodyParser = require('body-parser');
        const http = require('http');
        const portal = require("./lib/Portal");
        const { spawn } = require('child_process');
        const path = require('path');
        const fs = require('fs');

        zServer.registerModule("geoos", portal);

        app.get("/", (req, res) => {
            res.sendFile(__dirname + "/www/main/welcome/");
        });

        app.get("/doc", (req, res) => {
            res.redirect("https://bsodoc.ufpr.br/");
        });

        //app.use((req, res, next) => {
        //    if (req.path.endsWith('.js')) {
        //        res.type('application/javascript');
        //    }
        //    next();
        //});
        

        // Serve os arquivos estáticos do portal principal na rota "/portal"
        app.use("/portal", express.static(__dirname + "/www"));

        app.use(bodyParser.urlencoded({limit: '50mb', extended:true}));
        app.use(bodyParser.json({limit: '50mb', extended: true}));


        //Middleware para definir X-Content-Type-Options: nosniff
        //app.use((req, res, next) => {
        //   res.header("X-Content-Type-Options", "nosniff");
        //   next();
        //});

        // index.js

        let simulationData = {}; // Variável para armazenar os dados da simulação

        app.post('/salvar-coordenadas', (req, res) => {
            simulationData = req.body; // Salva os dados recebidos para uso posterior
            res.json({ message: 'Dados recebidos com sucesso.' });
        });

        function excluirDadosModelo() {
            return new Promise((resolve, reject) => {
                exec('rm -rf /home/data/modelo/', (error, stdout, stderr) => {
                    if (error) {
                        console.error(`Erro ao excluir dados do modelo: ${error}`);
                        return reject(error);
                    }
                    console.log('Dados do modelo excluídos com sucesso');
                    resolve(stdout);
                });
            });
        }

        function excluirArquivosSpill() {
            const diretorio = '/usr/src/app/Oil_Spill_Tool/res/Run1/';
        
            fs.readdir(diretorio, (err, arquivos) => {
                if (err) {
                    console.error(`Erro ao tentar ler o diretório: ${err}`);
                    return;
                }
        
                arquivos.forEach((arquivo) => {
                    if (arquivo.startsWith('Spill_')) {
                        fs.unlink(path.join(diretorio, arquivo), (err) => {
                            if (err) {
                                console.error(`Erro ao tentar excluir o arquivo '${arquivo}': ${err}`);
                                return;
                            }
                            console.log(`Arquivo excluído: ${arquivo}`);
                        });
                    }
                });
            });
        }

        app.get('/executar-script-python', async (req, res) => {
            try {
                await excluirDadosModelo();
                await excluirArquivosSpill();
                
                var m = new MohidOilSimulation();
                m.simulate(
                    simulationData.lon, 
                    simulationData.lat, 
                    simulationData.initial_date, 
                    simulationData.end_date, 
                    async (error) => {
                        if (error) {
                            console.error('Erro durante a simulação:', error);
                            res.status(500).send('Erro ao executar a simulação.');
                            return;
                        }
                
                        const scriptPath = path.join(__dirname, 'rastro_geojson.py');
                        const command = `python3 ${scriptPath}`;
                
                        try {
                            const { stdout, stderr } = await execPromise(command);
                            console.log(`stdout: ${stdout}`);
                            if (stderr) {
                                console.error(`stderr: ${stderr}`);
                            }
                            res.send('Script Python e simulação executados com sucesso');
                        } catch (err) {
                            console.error('Erro ao executar o script Python após a simulação:', err);
                            res.status(500).send('Erro ao executar o script Python após a simulação.');
                        }
                    }
                );
            } catch (err) {
                console.error('Erro durante a preparação para a execução da simulação ou do script Python:', err);
                res.status(500).send('Erro ao preparar a execução da simulação ou do script Python.');
            }
        });
        
        app.use((req, res, next) => {
            res.header("Access-Control-Allow-Origin", "*");
            res.header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
            res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
            next();
        });
        
        app.post("/*.*", (req, res) => zServer.resolve(req, res));     

        app.get("/fotoPerfil/:email", async (req, res) => {
            let email = req.params.email;
            let foto = await portal.getFotoPerfil(email);
            if (foto) {
                let regex = /^data:.+\/(.+);base64,(.*)$/;
                let matches = foto.match(regex);
                let contentType = matches[1];
                let data = matches[2];
                let buffer = Buffer.from(data, 'base64');
                res.set('Cache-Control', 'no-store, no-cache, must-revalidate, private');
                res.setHeader('Content-Type', "image/" + contentType);
                res.status(200);
                res.send(buffer);
            } else {
                res.sendStatus(404);
            }
        });

        app.get("/fotoBiblio/:id", async (req, res) => {
            let id = req.params.id;
            let foto = await portal.getFotoCapaBiblio(id);
            if (foto) {
                let regex = /^data:.+\/(.+);base64,(.*)$/;
                let matches = foto.match(regex);
                let contentType = matches[1];
                let data = matches[2];
                let buffer = Buffer.from(data, 'base64');
                res.set('Cache-Control', 'no-store, no-cache, must-revalidate, private');
                res.setHeader('Content-Type', "image/" + contentType);
                res.status(200);
                res.send(buffer);
            } else {
                res.sendStatus(404);
            }
        });

        let webServerConfig = config.getWebServerConfig();
        if (webServerConfig.http) {
            let port = webServerConfig.http.port;
            httpServer = http.createServer(app);
            httpServer.listen(port, "::", _ => {
                console.log("[GEOOS HTTP Server 0.88] Listenning at Port " + port);
            });
        }
    } catch(error) {
        console.error("Can't start HTTP Server", error);
        process.exit(-1);
    }
}

startHTTPServer();
 
