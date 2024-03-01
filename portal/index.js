const config = require("./lib/Config");

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

        app.get("/docs", (req, res) => {
            res.redirect("http://localhost:8000");
        });

        app.get("/docs", (req, res) => {
            res.redirect("http://localhost:8000");
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

        app.post('/salvar-coordenadas', (req, res) => {
            const data = req.body;
            const filePath = path.join('/home/data/cabral', 'coordenadas.json');
            fs.writeFile(filePath, JSON.stringify(data, null, 2), (err) => {
                if (err) {
                    console.error(err);
                    res.status(500).send('Erro ao salvar o arquivo');
                    return;
                }
                res.json({ message: 'Dados salvos com sucesso.' });
            });
        });

        app.get('/executar-script-python', (req, res) => {
            var m = new MohidOilSimulation();
            m.simulate("-48.1225", "-27.956389", "2023-06-17:04:00", "2023-06-17:05:00", (v) => {
                // v[0] = "/home/data/cabral/P-53_2019_ 4_ 2_ 0_ 0_ 0.00000000.nc";
                console.log(v);
                const scriptPath = path.join(__dirname, 'rastro_geojson.py');
                const pythonProcess = spawn('python3', [scriptPath, v[0]]);

                pythonProcess.stdout.on('data', (data) => {
                    console.log(`stdout: ${data}`);
                });

                pythonProcess.stderr.on('data', (data) => {
                    console.error(`stderr: ${data}`);
                    res.status(500).send('Erro ao executar o script Python');
                });

                pythonProcess.on('close', (code) => {
                    console.log(`Processo Python finalizado com código ${code}`);
                    res.send('Script Python executado com sucesso');
                });
            });
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
 