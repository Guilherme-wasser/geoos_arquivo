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
        this.find("#executarScriptPython1").onclick = () => this.executarScriptPython();

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

    // Método para enviar coordenadas, ajustado para integração direta com eventos de UI
    enviarCoordenadasNc() {
        // Coleta de dados dos campos de entrada
        const coordX = this.find("#coordX").value;
        const coordY = this.find("#coordY").value;
        const initialDate = this.find("#initialDate").value;
        const endDate = this.find("#endDate").value;
        const emissionTemporal = this.find("#emissionTemporal").value;
        const spillDuration = this.find("#spillDuration").value;
        const oilClass = this.find("#oilClass").value;
        const pointVolume = this.find("#pointVolume").value;
        const nbrPartic = this.find("#nbrPartic").value;
        const diffusionH = this.find("#diffusionH").value;

        // Construção do objeto com os dados a serem enviados
        const dataToSend = {
            lon: parseFloat(coordX),
            lat: parseFloat(coordY),
            initial_date: initialDate,
            end_date: endDate,
            emission_temporal: emissionTemporal,
            spill_duration: parseInt(spillDuration, 10),
            oil_class: oilClass,
            point_volume: parseFloat(pointVolume),
            nbr_partic: parseInt(nbrPartic, 10),
            diffusion_h: parseFloat(diffusionH)
        };

        fetch('/salvar-coordenadas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataToSend),
        })
        .then(response => {
            if (response.ok && response.headers.get("Content-Type").includes("application/json")) {
                return response.json(); // Processa a resposta como JSON
            }
            throw new Error('A resposta do servidor não é JSON');
        })
        .then(data => {
            console.log('Dados enviados com sucesso:', data);
            this.mostrarIconeCarregamento(false); // Oculta ícone de carregamento
        })
        .catch((error) => {
            console.error('Erro ao enviar dados:', error);
            this.mostrarIconeCarregamento(false); // Oculta ícone de carregamento mesmo em caso de falha
        });

        // Mostrar ícone de carregamento
        this.mostrarIconeCarregamento(true);
    }

    async addModeloModeloLayer() {
        try {
            //é um método que retorna todas as camadas disponíveis
            let availableLayers = await window.geoos.getAvailableLayers("vector");
    
            // Encontrar a camada específica com o código "modelo.modelo"
            let modeloLayer = availableLayers.find(l => l.code === "modelo.modelo" && l.type === "vector");
    
            // Verificar se a camada foi encontrada
            if (!modeloLayer) {
                console.error("Camada 'modelo.modelo' não encontrada.");
                return;
            }
    
            // Adicionar a camada encontrada ao grupo ativo ou ao contexto desejado
            let group = window.geoos.getActiveGroup();
            if (!group) {
                console.error("Nenhum grupo ativo encontrado para adicionar a camada.");
                return;
            }
    
            // Criar uma instância da camada com base na configuração encontrada
            let geoosLayer = GEOOSLayer.create(modeloLayer);
    
            // Adicionar a instância da camada ao grupo
            await group.addLayer(geoosLayer);
    
            // Disparar um evento para notificar que uma nova camada foi adicionada
            await window.geoos.events.trigger("portal", "layerAdded", group);
    
            console.log("Camada 'modelo.modelo' adicionada com sucesso.");
        } catch (error) {
            console.error("Erro ao tentar adicionar a camada 'modelo.modelo':", error);
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
            // Calcula o novo deslocamento
            let newX = e.clientX - initialX + windowElement.offsetLeft;
            let newY = e.clientY - initialY + windowElement.offsetTop;
        
            // Garante que a janela não saia da área visível do navegador na parte superior e nas laterais
            newX = Math.max(0, newX); // Impede que saia pela esquerda
            newY = Math.max(0, newY); // Impede que saia por cima
        
            // Impede que a janela saia pela direita
            const maxNewX = window.innerWidth - windowElement.offsetWidth;
            newX = Math.min(maxNewX, newX);
        
            // Impede que a janela saia pela parte inferior
            const maxNewY = window.innerHeight - windowElement.offsetHeight;
            newY = Math.min(maxNewY, newY);
        
            // Aplica o novo deslocamento à janela
            windowElement.style.left = newX + 'px';
            windowElement.style.top = newY + 'px';
        
            // Atualiza as coordenadas iniciais para o próximo movimento
            initialX = e.clientX;
            initialY = e.clientY;
        };
        
        const closeDragElement = () => {
            document.onmouseup = null;
            document.onmousemove = null;
            isDragging = false;
        };
        
        // Supondo que `handle.onmousedown` e a lógica de inicialização já estejam definidos corretamente
        handle.onmousedown = dragMouseDown;
                
    }
    
    
    limparDadosDoMapa() {
        console.log("Limpar todas as entradas e remover marcador.");
    
        // Remove o marcador, se existir
        if (this.currentMarker) {
            console.log("Removendo marcador.");
            this.currentMarker.remove();
            this.currentMarker = null;
        } else {
            console.log("Nenhum marcador para remover.");
        }
    
        // Limpa todos os campos de texto e número
        this.find("#coordX").value = "";
        this.find("#coordY").value = "";
        this.find("#initialDate").value = "";
        this.find("#endDate").value = "";
        this.find("#spillDuration").value = "";
        this.find("#pointVolume").value = "";
        this.find("#nbrPartic").value = "";
        this.find("#diffusionH").value = "";
    
        // Reseta todas as seleções para o primeiro valor disponível
        this.find("#emissionTemporal").selectedIndex = 0;
        this.find("#oilClass").selectedIndex = 0;
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
    
    executarScriptPython() {
        // Mostrar ícone de carregamento
        this.mostrarIconeCarregamento(true);
    
        fetch('/executar-script-python', { method: 'GET' })
        .then(response => {
            if (!response.ok) {
                throw new Error('Falha ao executar o script Python');
            }
            return response.text(); // ou .json() se o seu script Python retorna JSON
        })
        .then(data => {
            console.log(data); // Log do resultado do script
            
            // Espera 2 segundos antes de chamar `addModeloModeloLayer`
            setTimeout(() => {
                this.addModeloModeloLayer();
            }, 2000 );
        })
        .catch((error) => {
            console.error('Erro:', error);
        })
        .finally(() => {
            // Ocultar ícone de carregamento independentemente do resultado
            this.mostrarIconeCarregamento(false);
        });
    }
    
    mostrarIconeCarregamento(mostrar) {
        const iconeCarregamento = this.find("#iconeCarregamento");
        if (iconeCarregamento) {
            iconeCarregamento.style.display = mostrar ? "block" : "none";
        }
    }
    
       
}
ZVC.export(Modelo);
