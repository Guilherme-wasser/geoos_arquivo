const { exec } = require("child_process");
const util = require('util');
const execPromise = util.promisify(exec);

class MohidOilSimulation {
    constructor() {
        this.executableFilePath = "/usr/src/app/Oil_Spill_Tool/";
        this.executableFileName = "SpillTool.py";
        this.prefix_args = [
            "--emission_temporal",
            "Instantaneous",
            "--oil_class",
            "VeryLightOil",
            "--point_volume",
            "50"
        ];
    }

    async simulate_core(lon, lat, initial_date, end_date) {
        const args = this.prefix_args.concat(
            ["--lon", lon,
            "--lat", lat,
            "--initial_date", initial_date,
            "--end_date", end_date]
        );
        const command = `${this.executableFilePath}${this.executableFileName} ${args.join(" ")}`;

        try {
            const { stdout } = await execPromise(command, { cwd: this.executableFilePath });
            return stdout;
        } catch (error) {
            throw new Error(`Error executing SpillTool.py: ${error}`);
        }
    }

    generateFileList(initial_date, end_date) {
        let result = [];
        let curr_tsmp = Date.parse(initial_date);
        
        while (curr_tsmp < Date.parse(end_date)) {
            let dt = new Date(curr_tsmp);
            let y = dt.getFullYear();
            let m = dt.getMonth() + 1;
            let d = dt.getDate();
            let h = dt.getHours();
            let mn = dt.getMinutes();

            let fname = `Spill_${y}_${m}_${d}_${h}_${mn}_0.00000000.nc`;
            fname = `${this.executableFilePath}res/Run1/${fname}`;
            result.push(fname);

            curr_tsmp += 1000 * 60 * 60; // Incrementa uma hora
        }
        return result;
    }

    async simulate(lon, lat, initial_date, end_date, cb) {
        console.log("Starting Mohid simulation");
        
        try {
            await this.simulate_core(lon, lat, initial_date, end_date);
            
            let fileList = this.generateFileList(initial_date, end_date);
            console.log('File list generated:', fileList);
            cb(null, fileList);
        } catch (error) {
            console.error('Simulation error:', error);
            cb(error);
        }
    }

}

module.exports = MohidOilSimulation;
