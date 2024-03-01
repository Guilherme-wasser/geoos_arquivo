const { exec } = require("child_process");
const util = require('util');

const execPromise = util.promisify(exec);

function execShellCommand(cmd, ctx,) {
    const exec = require('child_process').exec;
    return new Promise((resolve, reject) => {
        exec("sleep 3", ctx,
        (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing process: ${error}`);
                console.error(stderr);
            }
            console.log(`Process output: ${stdout}`);
            console.error(stderr);
        });
    });
}

function os_func_sync() {
    this.execCommand = function (cmd) {
        return new Promise((resolve, reject)=> {
           exec(cmd, (error, stdout, stderr) => {
             if (error) {
                reject(error);
                return;
            }
            resolve(stdout)
           });
       })
   }
}


class MohidOilSimulation {
    constructor() {

        this.executableFilePath = "./Oil_Spill_Tool/";
        this.executableFileName = "./SpillTool.py";
        this.prefix_args = [
            "--emission_temporal",
            "Instantaneous",
            "--oil_class",
            "VeryLightOil",
            "--point_volume",
            "50"]
    }

    simulate_core(lon, lat, initial_date, end_date, cb) {
        // Code to execute the process and return the values

        var args = this.prefix_args.concat(
            ["--lon", lon,
            "--lat", lat,
            "--initial_date", initial_date,
            "--end_date", end_date]);
        
        exec(this.executableFileName + " " + args.join(" "),
            {
                cwd: this.executableFilePath
            },
            (error, stdout, stderr) => {
            // exec("sleep 2", (error, stdout, stderr) => {
                if (error) {
                    cb(stderr);
                }
                cb(stdout);
            });

        // var os = new os_func_sync();


        // os.execCommand('sleep 2').then(res=> {
        //     var x = null;
        //     x.test();
        //     cb(0);
        // }).catch(err=> {
        //     var x = null;
        //     x.test();
        //     cb(1);
        // });
    }

    simulate(lon, lat, initial_date, end_date, cb) {
        console.log("Starting Mohid simulation");
        return this.simulate_core(lon, lat, initial_date, end_date, (err) => {
            console.log(err);    
            var result = [];
            var curr_tsmp = Date.parse(initial_date);
            var fname;

            while(curr_tsmp < Date.parse(end_date)) {
                var dt = new Date(curr_tsmp);
                var y = dt.getFullYear();
                var m = (dt.getMonth() + 1)
                var d = dt.getDate();
                var h = dt.getHours();
                var mn = dt.getMinutes();

                curr_tsmp += 1000*60*60; // 1 hour
                fname = "Spill_"+y+"_ "+m+"_"+d+"_ "+h+"_ "+mn+"_  0.00000000.nc";
                fname = this.executableFilePath+"/res/Run1/"+fname;
                result.push(fname);
            }
            // console.log(fname);
            cb(result);
        });
    }


    test(cb){
        var m = new MohidOilSimulation();
        m.simulate("-48.1225", "-27.956389", "2023-06-17:04:00", "2023-06-18:06:00", (res) => {
            cb(res);
        });
    }
}


module.exports = MohidOilSimulation;