class Welcome extends ZCustomController {
    onThis_init() {
        // Inicialização do componente
    }

    onEnterPortal_click() {
        window.location.href = '/portal';
    }

    onEnterDocs_click() {
        window.location.href = '/doc';
    }
}

ZVC.export(Welcome);
