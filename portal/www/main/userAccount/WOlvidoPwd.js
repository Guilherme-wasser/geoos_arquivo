class WOlvidoPwd extends ZDialog {
    onThis_init(options) {
        this.cmdOk.disable();
        this.regenerar.hide();
        this.working.hide();
        if (options && options.email) this.edEmail.value = options.email;
        this.onEdEmail_change();
    }

    emailValido(email) {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) return true;
        return false;
    }

    onEdEmail_change() {
        let email = this.edEmail.value.trim();
        if (this.emailValido(email)) this.cmdEnviarCodigo.enable();
        else this.cmdEnviarCodigo.disable();
    }

    async onCmdEnviarCodigo_click() {
        try {
            let email = this.edEmail.value.trim();
            this.cmdEnviarCodigo.hide();
            this.working.show();
            await zPost("enviaCodigoRecuperacion.geoos", {email});
            this.regenerar.show();
            this.cmdOk.enable();
            this.edEmail.disable();
        } catch(error) {
            console.error(error);
            //this.showDialog("common/WError", {message:"Se produjo un error y el correo no pudo ser enviado. Por favor inténtelo más tarde"})
            this.showDialog("common/WError", {message:error.toString()})
        } finally {
            this.cmdEnviarCodigo.show();
            this.working.hide();
        }
    }

    async onCmdOk_click() {
        try {
            let email = this.edEmail.value.trim();
            let codigoRecuperacon = this.edCodigo.value.trim();
            let newPwd = this.edNewPwd.value.trim();
            let newPwd2 = this.edNewPwd2.value.trim();
            if (newPwd != newPwd2) throw window.toLang("$[javascripts.WCPwd_01]");
            if (newPwd2.length < 4) throw window.toLang("$[javascripts.Olvido_pwd_01]")
            await zPost("regeneraPwdUsuario.geoos", {email:email, codigoRegistro:codigoRecuperacon, pwd:newPwd});
            this.close();
            this.showDialog("common/WInfo", {message: window.toLang("$[javascripts.WCPwd_03]")})
        } catch(error) {
            this.showDialog("common/WError", {message:error.toString()})
        }
    }
    onCmdCancel_click() {this.close()}
    onCmdClose_click() {this.close()}
}
ZVC.export(WOlvidoPwd);