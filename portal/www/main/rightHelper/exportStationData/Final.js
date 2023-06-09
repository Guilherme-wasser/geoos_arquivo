class Final extends ZCustomController {
    onThis_init(options) {
        this.working.hide();
        this.error.hide();
        this.options = options;
        let desc = "Desde ";
        if (options.dsOriginal) {
            desc += window.toLang("$[javascripts.Final01]")
        } else {
            const descAcum = {
                "5m":"5 minutos", "15m":"15 minutos", "30m":"30 minutos", "1h": window.toLang("$[javascripts.Final16]"),
                "6h":"6 horas", "12h":"12 horas", "1d":window.toLang("$[javascripts.Final02]"), "1M":window.toLang("$[javascripts.Final17]")
            }
            desc += window.toLang("$[javascripts.Final03]") + descAcum[options.temporalidad] + window.toLang("$[javascripts.Final04]")
        }
        let vars = Object.keys(options.variables).reduce((list, v) => {
            if (options.variables[v]) list.push(v);
            return list;
        }, [])
        if (vars.length == 1) desc += window.toLang("$[javascripts.Final05]");
        else desc += window.toLang("$[javascripts.Final06]") + vars.length + window.toLang("$[javascripts.Final10]");
        desc += window.toLang("$[javascripts.Final08]");
        if (options.dsOriginal || options.temporalidad != "1M") {
            desc += window.toLang("$[javascripts.Final09]") + options.fmtFromTime + window.toLang("$[javascripts.Final11]") + options.fmtToTime;
        } else {
            desc += window.toLang("$[javascripts.Final12]") + options.fmtFromTime + window.toLang("$[javascripts.Final13]") + fmtToTime;
        }
        this.exportDesc.text = desc;
    }

    async doExport() {
        this.working.show();
        try {
            if (this.options.dsOriginal) {
                let filter = {};
                filter[this.options.colCodigoEstacion] = this.options.station.code;
                let columns = Object.keys(this.options.variables).reduce((list, v) => {
                    if (this.options.variables[v]) list.push(v);
                    return list;
                }, [])
                let rows = await this.options.station.server.client.queryDataSet(
                    this.options.dataSet.code, 
                    this.options.fromTime, this.options.toTime,
                    filter, columns
                )
                let head = window.toLang("$[javascripts.Final15]") + columns.reduce((st, col) => {
                    return st + ";" + col;
                }, "");

                let csv = rows.reduce((txt, row) => {
                    let m = moment.tz(row.time, window.timeZone);
                    let st = m.format("DD/MM/YYYY HH:mm");
                    st += columns.reduce((st, col) => {
                        return st + ";" + ((isNaN(row[col]) || row[col] == null)?"":row[col].toLocaleString("en", {useGrouping:false}));
                    }, "");
                    return txt + "\n" + st;
                }, head);
                var downloadLink = document.createElement("a");
                var blob = new Blob(["\ufeff", csv]);
                var url = URL.createObjectURL(blob);
                downloadLink.href = url;
                downloadLink.download = "estacion-" + this.options.station.code + ".csv";

                document.body.appendChild(downloadLink);
                downloadLink.click();
                document.body.removeChild(downloadLink);

                this.triggerEvent("finish");
            } else {
                let filter = {estacion:this.options.station.code};
                let units = {};
                let vars = this.options.variables;                
                let variables = this.options.listaVariables.reduce((lista, v) => {
                    if (vars[v.code + "-avg"] || vars[v.code + "-min"] || vars[v.code + "-max"] || vars[v.code + "-n"]) lista.push(v.code);
                    console.log("options", v.options, v);
                    if (v.options && v.options.unit) units[v.code] = " [" + v.options.unit + "]";
                    else units[v.code] = "";
                    return lista;
                }, [])
                let data = await (this.options.station.server.client.queryMultiVarTimeSerie(
                    variables,                    
                    this.options.fromTime, this.options.toTime,
                    filter, this.options.temporalidad, true
                ).promise);
                let csv =  window.toLang("$[javascripts.Final15]") + variables.reduce((st, v) => {
                    let vName = v;                    
                    if (vName.startsWith("rie.")) vName = vName.substr(4);
                    let unit = units[v] || "";
                    if (this.options.variables[v + "-avg"]) st += ";" + vName + "_avg" + unit;
                    if (this.options.variables[v + "-min"]) st += ";" + vName + "_min" + unit;
                    if (this.options.variables[v + "-max"]) st += ";" + vName + "_max" + unit;
                    if (this.options.variables[v + "-n"]) st += ";" + vName + "_n [N°]";
                    return st;
                }, "");
                let indexes = {};
                variables.forEach(v => indexes[v] = 0);
                let time;
                do {
                    time = undefined;
                    variables.forEach(v => {
                        if (indexes[v] < data[v].length) {
                            let idx = indexes[v];
                            let t = data[v][idx].t;
                            if (time === undefined || t < time) time = t;
                        }
                    });
                    if (time) {
                        let m = moment.tz(time, window.timeZone);
                        let st = m.format("DD/MM/YYYY HH:mm");
                        variables.forEach(v => {
                            let avg="", min="", max="", nSamples="";
                            if (indexes[v] < data[v].length) {
                                let idx = indexes[v];
                                let t = data[v][idx].t;
                                if (t == time) {
                                    let val = data[v][idx];
                                    if (val.n && val.m !== null && val.M !== null) {
                                        // console.log("val", val);
                                        avg = (val.v / val.n).toLocaleString("en", {useGrouping:false});
                                        min = val.m.toLocaleString("en", {useGrouping:false});
                                        max = val.M.toLocaleString("en", {useGrouping:false});
                                        nSamples = val.n;
                                    }
                                    indexes[v]++;
                                }
                            }
                            if (this.options.variables[v + "-avg"]) st += ";" + avg;
                            if (this.options.variables[v + "-min"]) st += ";" + min;
                            if (this.options.variables[v + "-max"]) st += ";" + max;
                            if (this.options.variables[v + "-n"]) st += ";" + nSamples;
                        })
                        csv += "\n" + st;
                    }
                } while(time);
                var downloadLink = document.createElement("a");
                var blob = new Blob(["\ufeff", csv]);
                var url = URL.createObjectURL(blob);
                downloadLink.href = url;
                downloadLink.download = "estacion-" + this.options.station.code + ".csv";

                document.body.appendChild(downloadLink);
                downloadLink.click();
                document.body.removeChild(downloadLink);

                this.triggerEvent("finish");
            }
        } catch(error) {
            this.working.hide();
            this.error.show();
            this.error.find("#lblError").innerText = error.toString();
        }
    }
}
ZVC.export(Final);