class Modelo extends ZCustomController {
    onThis_init() {
        // Acessar a instância de AddObjectPanel que já está sendo usada
        this.addObjectPanel = window.geoos.addObjectPanel;
        this.currentMarker = null; // Adicione esta linha para manter o marcador atual
        // Configuração do arrasto da janela
        this.setupDraggableWindow();
        this.setupDraggableButton();

        // Botões e eventos      
        this.find("#meuBotao").onclick = () => this.mostrarJanelaPopUp();
        this.find(".close").onclick = () => this.onJanelaPopUpFechar_click();
        this.find("#inserirCoordMapa").onclick = () => this.startMapClickListening();
        this.find("#enviarCoordenadas").onclick = () => this.enviarCoordenadasNc();
        // Adiciona o manipulador de eventos para o novo botão
        this.irParaCoordenadas = () => {
            const lat = parseFloat(this.find("#coordX").value);
            const lng = parseFloat(this.find("#coordY").value);
        
            if (!isNaN(lat) && !isNaN(lng)) {
                // Remove o marcador anterior, se existir
                if (this.currentMarker) {
                    this.currentMarker.remove();
                }
        
                // Cria um novo marcador nas coordenadas especificadas e o adiciona ao mapa
                this.currentMarker = L.marker([lat, lng]).addTo(window.geoos.mapPanel.map);
        
                // Centraliza o mapa nas novas coordenadas e ajusta o zoom
                window.geoos.mapPanel.deserialize({lat: lat, lng: lng, zoom: 10});
            } else {
                alert("Coordenadas inválidas.");
            }
        };
        this.find("#irParaCoordenadas").onclick = this.irParaCoordenadas;
        this.find("#limparCoordenadas").onclick = () => this.limparDadosDoMapa();
    }

    // Método para enviar coordenadas
    enviarCoordenadasNc() {
        if (this.currentMarker) {
            const latLng = this.currentMarker.getLatLng();
            const coordenadas = { lat: latLng.lat, lng: latLng.lng };

            // Exibir ícone de carregamento
            this.mostrarIconeCarregamento(true);

            // Simula o envio de coordenadas e o recebimento do arquivo netcdf
            setTimeout(() => {
                this.mostrarIconeCarregamento(false);
                // Aqui você pode adicionar a lógica para lidar com o arquivo netcdf recebido
            }, 3000); // Ajuste este tempo conforme necessário

            console.log("Coordenadas enviadas:", coordenadas);
        } else {
            alert("Por favor, insira as coordenadas primeiro.");
        }
    }
    
    // Método para mostrar ou ocultar o ícone de carregamento
    mostrarIconeCarregamento(mostrar) {
        // Aqui, você pode implementar a lógica para mostrar ou ocultar um ícone de carregamento
        // Por exemplo, alterar a visibilidade de um elemento HTML com um ícone de carregamento
        const iconeCarregamento = this.find("#iconeCarregamento"); // Substitua pelo seu seletor correto
        if (iconeCarregamento) {
            iconeCarregamento.style.display = mostrar ? "block" : "none";
        }
    }     

    initButtonPosition(button) {
        if (!button.style.left) {
            button.style.left = button.offsetLeft + "px";
        }
        if (!button.style.top) {
            button.style.top = button.offsetTop + "px";
        }
        button.style.position = 'absolute'; // Garantir que o botão esteja posicionado absolutamente
    }

    startMapClickListening() {
        // Verificar se a instância de AddObjectPanel está disponível
        if (this.addObjectPanel) {
            this.addObjectPanel.activeOption = "point"; // Definir a opção desejada
            this.addObjectPanel.startAdding(); // Iniciar o processo de adição

        // Sobrescrever o método handleMapClick para capturar as coordenadas
        this.addObjectPanel.handleMapClick = (p) => {
            // Remove o marcador anterior, se existir
            if (this.currentMarker) {
                this.currentMarker.remove();
            }

            // Atualizar os campos de coordenadas
            this.find("#coordX").value = p.lat; // ou p.x
            this.find("#coordY").value = p.lng; // ou p.y

            // Adiciona um marcador no local clicado
            this.currentMarker = L.marker([p.lat, p.lng]).addTo(window.geoos.mapPanel.map);

            this.addObjectPanel.stopAdding(); // Parar de adicionar após o clique
        };
        }
    }

    mostrarJanelaPopUp() {
        this.find("#janelaPopUp").style.display = "block";
    }

    onJanelaPopUpFechar_click() {
        this.find("#janelaPopUp").style.display = "none";
    }

    makeButtonDraggable(button) {
        let initialX = 0, initialY = 0;
        let isDragging = false;
    
        const dragMouseDown = e => {
            e.preventDefault();
            initialX = e.clientX - button.getBoundingClientRect().left;
            initialY = e.clientY - button.getBoundingClientRect().top;
            document.onmouseup = closeDragElement;
            document.onmousemove = buttonDrag;
            isDragging = true;
        };
    
        const buttonDrag = e => {
            if (!isDragging) return;
            e.preventDefault();
            button.style.left = (e.clientX - initialX) + 'px';
            button.style.top = (e.clientY - initialY) + 'px';
        };
    
        const closeDragElement = () => {
            document.onmouseup = null;
            document.onmousemove = null;
            isDragging = false;
        };
    
        button.onmousedown = dragMouseDown;
    }
    
    makeWindowDraggable(windowElement, handle) {
        let initialX = 0, initialY = 0;
        let isDragging = false;
    
        const dragMouseDown = e => {
            e.preventDefault();
            // Calcula a posição inicial do cursor
            initialX = e.clientX;
            initialY = e.clientY;
    
            document.onmouseup = closeDragElement;
            document.onmousemove = windowDrag;
            isDragging = true;
        };
    
        const windowDrag = e => {
            if (!isDragging) return;
            e.preventDefault();
            // Aplica o deslocamento à janela mantendo-a alinhada com o cursor
            const newX = e.clientX - initialX + windowElement.offsetLeft;
            const newY = e.clientY - initialY + windowElement.offsetTop;
            windowElement.style.left = newX + 'px';
            windowElement.style.top = newY + 'px';
            initialX = e.clientX;
            initialY = e.clientY;
        };
    
        const closeDragElement = () => {
            document.onmouseup = null;
            document.onmousemove = null;
            isDragging = false;
        };
    
        handle.onmousedown = dragMouseDown;
    }
    
    
    limparDadosDoMapa() {
        console.log("Limpar coordenadas e marcador.");
        
        if (this.currentMarker) {
            console.log("Removendo marcador.");
            this.currentMarker.remove();
            this.currentMarker = null;
        } else {
            console.log("Nenhum marcador para remover.");
        }
    
        this.find("#coordX").value = "";
        this.find("#coordY").value = "";
    }

    setupDraggableButton() {
        const btn = this.find("#meuBotao");
        this.initButtonPosition(btn);
        this.makeButtonDraggable(btn);
    }
    
    setupDraggableWindow() {
        const popup = this.find("#janelaPopUp");
        const header = popup.querySelector(".header");
        this.makeWindowDraggable(popup, header);
    }   
}
ZVC.export(Modelo);
