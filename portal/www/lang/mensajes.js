const mensajes = {

    // Comunes
    comunes: {
        aceptar: { es: "Aceptar", pt: "Aceitar"},
        cancelar: { es: "Cancelar", pt: "Cancelar"}
    },
    // MainMenu
    mainMenu: {
        recordame: { es: "Recordarme en este Equipo", pt: "Lembrar-me neste equipamento"},
        ling: { es: "Lenguaje", pt: "Linguagem"},
        W1: { es: "Buscar en Biblioteca ...", pt: "Buscar na Biblioteca"}, 
        //comunes en mainMenu html
        Seleccionar: { es: "Seleccionar", pt: "Selecionar"}, 
        Agregar: { es: "Agregar", pt:"Adicionar"},
        Objetos: { es: "Objetos", pt:"Objetos"},
        Capas: { es: "Capas", pt:"Camadas"},
        Estaciones: { es: "Estaciones", pt:"Estações"},
        punto: { es: "Punto", pt:"Ver"},
        tema: { es: "Tema", pt: "Emitir"},
        Contactar: { es: "Contactar", pt: "Contato"},
        Descripcion: { es: "Descripción", pt: "Descrição"},
        Editar: { es: "Editar", pt: "Editar"},
        Eliminar: { es: "Eliminar", pt: "Eliminar"},
        //
        CapaVeri: { es: "Capa Verificada", pt: "Camada Verificada"},
        AgregarMiPanel: { es: "Agregar a Mi Panel", pt: "Adicionar ao Meu Painel"},
        //MyPanel
        miPanel: { es: "Mi Panel", pt: "Meu Painel"},
        crearGrupo: { es: "Crear Grupo", pt: "Criar Grupo"},
        importarGrupo: { es: "Importar Grupo", pt: "Importar Grupo"},
        //
        bibliotecaCompartidaGeos: { es: "Biblioteca Compartida GEOOS", pt: "Biblioteca Compartilhada GEOOS"},
        soloVerificados: { es: "Sólo Verificados", pt: "Apenas Verificado"},
        //
        CapasComVar: { es: "Seleccionar Capas con Variables", pt: "Selecionar Camadas com Variáveis"}, 
        //
        BibliotecaGEOOS: { es: "Biblioteca GEOOS", pt:"Biblioteca GEOOS"},
        //AddObjectPanel html
        hagaclickenelmapa: { es: "Haga click en el mapa para agregar el punto en la ubicación deseada.", pt:"Clique no mapa para adicionar o ponto no local desejado."},
        Proximamente: { es: "Próximamente", pt:"Breve"},
        areaRectangular: { es: "Área Rectangular", pt:"Área Retangular"},
        hagaclickenlaubication: { es: "Haga click en el mapa en un punto para seleccionar una esquina del área. Haga click en la ubicación de la esquina opuesta para terminar.", pt:"Clique no mapa em um ponto para selecionar um canto da área. Clique no local do canto oposto para terminar."},
        //AddPanel html
        CapasComVar: { es: "Seleccionar Capas con Variables", pt: "Selecionar Camadas com Variáveis"}, 
        PuntosAreas: { es: "Puntos o Áreas de Interés", pt:"Pontos ou Áreas de Interesse"},
        EstMoni: { es: "Estaciones de Monitoreo", pt:"Estações de Monitoramento"},
        CapasImag: { es: "Capas de Imágenes", pt:"Camadas de Imagem"},
        CapasMultMed: { es: "Capas Multimedia", pt:"Camadas de Mídia"},
        CapasEsp: { es: "Capas Especiales", pt:"Camadas Especiais"},
        BuscarVariCap: { es: "Buscar Variable o Capa", pt:"Localizar Variável ou Camada"},
        NombreVarFil: { es: "Nombre de la Variable Filtrada", pt:"Nome da Variável Filtrada"},
        DescGel: { es: "Descripción General", pt:"Descrição Geral"},
        Detalles: { es: "Detalles", pt:"Detalhes"},
        DispGeo: { es: "Disponibilidad GEOOS", pt:"Disponibilidade GEOOS"},
        //Wpublish
        PubB: { es: "Publicar en Biblioteca", pt:"Publicar na Biblioteca"},
        TitPub: { es: "Título de la Publicación", pt:"Título de Publicação"},
        SelArras: { es: "Seleccione o Arrastre una imagen de captura que represente la Capa que comparte", pt:"Selecione ou arraste uma imagem de captura que representa a camada que você compartilha"},
        SelTema: { es: "Seleccione al menos un Tema", pt:"Selecione pelo menos um Tema"},
        PuedeEle: { es: "Puede elegir si su información personal (nombre, email, institución) se muestran junto a la capa compartida. Esto permite que los usuarios que tengan dudas puedan contactarlo directamente.", pt:"Você pode escolher se suas informações pessoais (nome, e-mail, instituição) são exibidas ao lado da camada compartilhada. Isso permite que usuários com dúvidas entrem em contato diretamente com você."},
        PermSC: { es: "Permitir ser contactado", pt:"Permitir ser contatado"},
        Pub: { es: "Publicar", pt:"Publicar"},
        //AddStationsPanel
        SelecionarEstacao: { es: "Seleccionar Estaciones", pt:"Selecionar Estações"},
        BuscarEstacion: { es: "Buscar Estación", pt:"Buscar Estação"},
        //AnalysisPanel
        NombreObjeto: { es: "Nombre del Objeto", pt:"Nome do Objeto"},
        Generando: { es: "Generando ...", pt:"Gerando ..."},
        //GroupProperties
        Nombre: { es: "Nombre", pt:"Nome"},
        //formula
        //formulaConfig
        ResolucionDeseada: { es: "Resolución Deseada (Longitud, Latitud) °", pt:"Resolução Desejada (Longitude, Latitude) °"},
        UnidadeMedida: { es: "Unidad Medida", pt:"Unidade de Medida"},
        NDecimales: { es: "N° Decimales", pt:"N° Decimais"},
        Tipo: { es: "Tipo", pt:"Tipo"},
        //Formula Results
        Trabajando: { es: "Trabajando ...", pt:"Trabalhando ..."},
        //Sources
        AgregarVarEntrada: { es: "Agregar Variable de Entrada a Fórmula", pt:"Adicionar variável de entrada à fórmula"},
        //WFormula
        EditarFormula: { es: "Editar Fórmula", pt:"Editar Fórmula"},
        Comience: { es: "Comience a escribir 'variable' para listar e insertar la lista de variables de entrada de la fórmula.", pt:"Comece a digitar 'variável' para listar e insira a lista de variáveis ​​de entrada da fórmula."},
        Grabar: { es: "Grabar", pt:"Gravar"},
        Cerrar: { es: "Cerrar", pt:"Fechar"},
        //WSourceTime
        TiempoVar: { es: "Tiempo de Variable", pt:"Tempo Variável"},
        TipoTiempo: { es: "Tipo de Tiempo", pt:"Tipo de Tempo"},
        TiempoFijo: { es: "Tiempo Fijo", pt:"Horário Fixo"},
        Desplazamiento: { es: "Desplazamiento", pt:"Deslocamento"},
        TiempoDelMapa: { es: "Tiempo del Mapa", pt:"Hora do Mapa"},
        Desplazamiento2 : { es: "Desplazamiento inválido", pt:"Deslocamento inválido"},
        //Tolerance
        BuscarItems: { es: "Buscar Items +/-", pt:"Buscar Items +/-"},
        //FixedLevelsProperties
        PuedaDefinir: { es: "Puede definir una lista separada por espacios de los valores para los niveles que desea extraer para las isolíneas de la variable.", pt:"Você pode definir uma lista separada por espaços dos valores para os níveis que deseja extrair para as isolinhas da variável."},
        SeUtilizaOpcion: { es: "Si utiliza esta opción, se ignorará el incremento y se extraerá sólo el nivel o los niveles que acá ingrese.", pt:"Se você usar esta opção, o incremento será ignorado e apenas o nível ou níveis inseridos aqui serão extraídos."},
        NivelesFijos: { es: "Niveles Fijos", pt:"Níveis Fixos"},
        //IsobandsProperties
        IncrementoAuto: { es: "Incremento Automático", pt:"Incremento Automático"},
        Incremento: { es: "Incremento", pt:"Incremento"},
        //IsolinesProperties
        GrosorLineas: { es: "Grosor de Líneas", pt:"Espessura da Linha"},
        ColorLineas: { es: "Color de Líneas", pt:"Cor da Linha"},
        //ParticlesProperties
        NParticulas: { es: "N° Partículas", pt:"N° Partículas"},
        Velocidad: { es: "Velocidad", pt:"Velocidade"},
        //LayerProperties
        ValorNivel: { es: "Valor en Nivel", pt:"Valor no Nível"},
        Opacidad: { es: "Opacidad", pt:"Opacidade"},
        Opacidad2: { es: "Opacidad: ", pt:"Opacidade: "},
        //Stations
        ZNort: { es: "Zona Norte", pt:"Zona Norte"},
        ZCentro: { es: "Zona Centro", pt:"Zona Centro"},
        ZSur: { es: "Zona Sur", pt:"Zona Sul"},
        ZAustral: { es: "Zona Austral", pt:"Zona Austral"},
        //Watchers
        Cancelando: { es: "Cancelando ...", pt:"Cancelando ..."},
        //Watchers Color Scale
        Escala: { es: "Escala", pt:"Escala"},
        CalcLim: { es: "Cálculo de Límites Automático", pt:"Cálculo de Limites Automático"},
        EliminarVal: { es: "Eliminar Valores fuera del Rango", pt:"Excluir valores fora do intervalo"},
        //PointObjectProperties
        Latitud: { es: "Latitud", pt:"Latitude"},
        Longitud: { es: "Longitud", pt:"Longitude"},
        //UOWatchers
        //UserObjectProperties
        //ColorScaleProperties
        //ConfigPanel
        Configuraciones: { es: "Configuraciones", pt:"Configurações"},
        //FavGroups
        GruposFavoritos: { es: "Grupos Favoritos", pt:"Grupos Favoritos"},
        //FavLayers
        CapasFavoritas: { es: "Capas Favoritas", pt:"Camadas Favoritas"},
        //FavStations
        Est_01: { es: "Estaciones", pt:"EStações"},
        EstacionesFavoritas: { es: "Estaciones Favoritas", pt:"Estações Favoritas"},
        //UserMarksPanel
        Favoritos: { es: "Favoritos", pt:"Favoritos"},
        MisGrupos: { es: "Mis Grupos", pt:"Meus Grupos"},
        MisCapas: { es: "Mis Capas", pt:"Minhas Camadas"},
        MisEStaciones: { es: "Mis Estaciones", pt:"Minhas Estações"},
        //AboutPage
        EsUnGeoPortal: { es: "es un GeoPortal que permite consultar información georreferenciada de diferentes tipos, incluyendo imagenes de datos satelitales, resultados de modelos de pronósticos, valores de sensores de estaciones meteorológicas en tiempo real, datos tabulares históricos clasificados por zonas geográficas, entre otros tipos.", pt:" é um GeoPortal que permite consultar informação georreferenciada de diferentes tipos, incluindo imagens de dados de satélite, resultados de modelos de previsão, valores de sensores de estações meteorológicas em tempo real, dados tabulares históricos classificados por áreas geográficas, entre outros tipos."},
        //ColabPage <latim>
        //Updates
        NotaVersion1: { es: "Nota de version B.S.O 2.3", pt:"Nota de versão do B.S.O 2.3"},
        NotaVersion2: { es: "1. Grupo inicial personalizado (configurable desde Favoritos)", pt:"1. Grupo inicial personalizado (configurável em Favoritos)"},
        NotaVersion3: { es: "Al iniciar B.S.O aparece un grupo de capas por defecto, el cual desde el Panel Favoritos puede ser cambiado. Basta con agregar cualquier grupo desde Mi Panel y hacer click en el pin para seleccionarlo como grupo por defecto", pt:"Ao iniciar GEOOs, um grupo de camadas aparece por padrão, o que pode ser alterado no Painel de Favoritos. Basta adicionar qualquer grupo do Meu Painel e clicar no alfinete para selecioná-lo como grupo padrão"},
        NotaVersion4: { es: "2. Se puede ver que estacion se agrego a Mi panel desde panel lateral", pt:"2. Você pode ver qual estação foi adicionada ao meu painel no painel lateral"},
        NotaVersion5: { es: "3. Barra de colores", pt:"3. Barra de cores"},
        NotaVersion6: { es: "Cuando se selecciona una capa y un visualizados, en la parte inferior derecha de la pantalla aparece una barra de colores en donde se muestra el significado de la gama de colores de esa capa, si presiona sobre la paleta, puede cambiar los colores por los que mas le acomoden", pt:"Quando uma camada e uma exibição são selecionadas, uma barra de cores aparece na parte inferior direita da tela onde é mostrado o significado da gama de cores dessa camada, se você pressionar na paleta, poderá alterar as cores para as quais elas se adequam você mais"},
        NotaVersion7: { es: "4. Corrección de errores en Grupos de Mi Panel", pt:"4. Correções de bugs em Meus Grupos de Painéis"},
        //UserHelpPanel
        Ayuda: { es: "Ayuda", pt:"Ajuda"},
        Novedades: { es: "Novedades", pt:"Novidades"},
        QueEsGeoos: { es: "Qué es B.S.O", pt:"O Que é B.S.O"},
        FAQ: { es: "FAQ", pt:"FAQ"},
        Colaboradores: { es: "Colaboradores", pt:"Colaboradores"},
        //WHelp
        Acerca: { es: "Acerca de ...", pt:"Acerca de ..."},
        ProyectoG: { es: "Proyecto B.S.O", pt:"Projeto B.S.O"},
        //InforBar
        //Map
        //WAudio
        AudioStrg: { es: "Audio", pt:"Audio"},
        //WYoutubeVideo
        CamaraVivo: { es: "Cámara en Vivo", pt:"Câmera ao vivo"},
        Expandir: { es: "Expandir", pt:"Expandir"},
        //DataSource
        OrigenLosDatos: { es: "Origen de los Datos", pt:"Origem dos Dados"},
        LosDatosPueden: { es: "Los datos pueden descargarse desde los valores originales informados por la Estación o como estadísticas desde los Períodos acumulados por GEOOS, desde grupos de 5 minutos hasta grupos mensuales.", pt:"Os dados podem ser baixados dos valores originais informados pela Estação ou como estatísticas dos Períodos acumulados pelo GEOOS, desde grupos de 5 minutos até grupos mensais."},
        DescargarValOrig: { es: "Descargar Valores Originales", pt:"Baixar valores Originais"},
        DescargarEstat: { es: "Descargar Estadísticas Acumuladas", pt:"Baixar Estatísticas Cumulativas"},
        //Exporter
        SelVar: { es: "Selección de Variables", pt:"Seleção de Variável"},
        PeriodoExtrac: { es: "Período de Extracción", pt:"Período de Extração"},
        Descargar: { es: "Descargar", pt:"Baixar"},
        Volver: { es: "Volver", pt:"Retornar"},
        Continuar: { es: "Continuar", pt:"Continuar"},
        //Final
        GenerandoConjunto: { es: "Generando conjunto de datos. Por favor espere ...", pt:"Gerando conjunto de dados. Por favor espere ..."},
        LosDatosSeran: { es: "Los datos serán descargados en formato CSV. Los campos se separaán por punto y coma ( ; ). Los valores numéricos se formatean con un punto para indicar la posición decimal, y sin agrupador de miles.", pt:"Os dados serão baixados no formato CSV. Os campos serão separados por ponto e vírgula ( ; ). Os valores numéricos são formatados com um ponto para indicar a posição decimal e sem agrupamento de milhares."},
        LosValoresExp: { es: "Los valores que se exportan se obtienen desde los repositorios a los que los envía cada estación. GEOOS sólo recopila los valores de las variables (sensores) de cada estación y no es responsable de la validez de estos datos.", pt:"Os valores que são exportados são obtidos dos repositórios para os quais cada estação os envia. O GEOOS coleta apenas os valores das variáveis ​​(sensores) de cada estação e não se responsabiliza pela validade desses dados."},
        //Periodo
        AgrupaT: { es: "Agrupación Temporal", pt:"Agrupamento Temporário"},
        FechaI: { es: "Fecha de Inicio", pt:"Data de início"},
        FechaT: { es: "Fecha de Término", pt:"Data de término"},
        //SelVariables
        SelVar: { es: "Seleccionar Variables", pt:"Selecionar Variáveis"},
        //RightHelper
        //SearchLocation
        BuscarLocal: { es: "Buscar Localidad", pt:"Buscar Localidade"},
        //Time
        Sabado: { es: "Sábado 23 Diciembre", pt:"Sábado 23 de Dezembro"},
        SaltoTiempo: { es: "Salto de tiempo: Días", pt:"Salto de tempo: Dias"},
        Horas: { es: "Horas", pt:"Horas"},
        Minutos: { es: "Minutos", pt:"Minutos"},
        //WAnim
        GenerarAnimacion: { es: "Generar Animación", pt:"Gerar Animação"},
        Titulo: { es: "Título", pt:"Título"},
        FormatoTiempo: { es: "Formato Tiempo", pt:"Formato de Tempo"},
        Generando: { es: "Generando", pt:"Gerando"},
        Estado: { es: "Estado", pt:"Estado"},
        Generar: { es: "Generar", pt:"Acionar"},
        //ToolObjcSelec
        SeleccioneObj: { es: "Seleccione el Objeto / Estación de Monitoreo", pt:"Selecione o Objeto/Estação de Monitoramento"},
        SeleccionarMiPanel: { es: "Seleccionar desde Mi Panel", pt:"Selecione em Meu Painel"},
        DesdeCapa: { es: "Desde la Capa", pt:"Da Camada"},
        UsarObj: { es: "Usar el Objecto", pt:"Use o Objeto"},
        AgregarNuevo: { es: "Agregar un Nuevo Objeto a Mi Panel", pt:"Adicionar um novo objeto ao meu painel"},
        AgregarArea: { es: "Agregar Área", pt:"Adicionar Área"},
        AgregarEstacion: { es: "Agregar Estación", pt:"Adicionar Estação"},
        //ToolPathSelec
        SeleccioneUna: { es: "Seleccione una Ruta", pt:"Selecione uma rota"},
        PuntosEnLa: { es: "Puntos en la Ruta", pt:"Pontos de rota"},
        NuevoPunto: { es: "Nuevo Punto", pt:"Novo Ponto"},
        PuntosDisponibles: { es: "Puntos Disponibles", pt:"Pontos Disponíveis"},
        //ToolColorScale
        //SelectRaster
        //AddTool
        CrearNuevo: { es: "Crear Nuevo Análisis", pt:"Criar Nova Análise"},
        SeleTipoAna: { es: "Seleccione el Tipo de Análisis", pt:"Selecione o tipo de análise"},
        NombreNuevo: { es: "Nombre del Nuevo Análisis", pt:"Nome da Nova Análise"},
        GenerarAnalises: { es: "Generar Análisis", pt:"Gerar Análise"},
        //ToolsPanel
        PanelAnalisis: { es: "Panel de Análisis", pt:"Painel de Análises"},
        //ViewTool
        //Top
        //WConfigTools
        ConfigHerra: { es: "Configurar Herramientas de Análisis", pt:"Configurar Ferramentas de Análise"},
        MisHerra: { es: "Mis Herramientas Frecuentes", pt:"Minhas Ferramentas Frequentes"},
        TodasHerramientas: { es: "Todas las Herramientas", pt:"Todas as Ferramentas"},
        //Logged
        CerrarSesion: { es: "Cerrar Sesión", pt:"Fechar Sessão"},
        //Login
        Correo: { es: "Correo", pt:"e-mail"},
        ContraS: { es: "Contraseña (*)", pt:"Senha (*)"},
        Olvidaste: { es: "¿Olvidaste tu contraseña?", pt:"Você esqueceu sua senha?"},
        IniciarS: { es: "Iniciar Sesión", pt:"Iniciar sessão"},
        //Profile
        DatosUs: { es: "Datos del Usuario", pt:"Dados do Usuário"},
        ElimFoto: { es: "Eliminar Foto", pt:"Eliminar Foto"},
        emaill: { es: "E-mail", pt:"E-mail"},
        instit: { es: "Institución", pt:"Instituição"},
        CambiarC: { es: "Cambiar Contraseña", pt:"Alterar a Senha"},
        GrabarC: { es: "Grabar Cambios", pt:"Salvar Alterações"},
        //Register
        SeLeEnviara: { es: "Se le enviará un código de 6 dígitos para verificar su dirección de correo electrónico.", pt:"Você receberá um código de 6 dígitos para verificar seu endereço de e-mail."},
        DireccionE: { es: "Dirección E-mail: ", pt:"Endereço de email: "},
        EnvCod: { es: "Enviar Código", pt:"Enviar código"},
        LaContraAl: { es: "La contraseña se almacena encriptada en nuestros servidores. Si la olvida podrá crear una nueva, pero no recuperarla.", pt:"A senha é armazenada criptografada em nossos servidores. Se você esquecê-lo, pode criar um novo, mas não recuperá-lo."},
        Registrarse: { es: "Registrarse", pt:"Registrar-se"},
        //UserAccPan
        CuentaUs: { es: "Cuenta del Usuario", pt:"Conta do Usuário"},
        Session: { es: "SESIÓN", pt:"SESSÃO"},
        Perfil: { es: "PERFIL", pt:"PERFIL"},
        REGISTRARSE: { es: "REGISTRARSE", pt:"REGISTRAR-SE"},
        //WCambiaPwd
        ContraAtual: { es: "Contraseña Actual", pt:"Senha atual"},
        NuevoContra: { es: "Nueva Contraseña", pt:"Nova senha"},
        RepetirNueva: { es: "Repetir Nueva Contraseña", pt:"Repita a nova senha"},
        //WCode
        VerCodRe: { es: "Verificar Código de Registro", pt:"Verifique o código de registro"},
        ComoMedidaDeS: { es: "Como medida de seguridad adicional, introduce el código de 6 dígitos que enviamos a tu correo.", pt:"Como medida de segurança adicional, digite o código de 6 dígitos que enviamos para o seu e-mail."},
        Confirmar: { es: "Confirmar", pt:"Confirmar"},
        //WOlvido
        Olvido: { es: "Olvidó Contraseña", pt:"Esqueceu sua senha"},
        DirEmail: { es: "Dirección E-mail", pt:"Endereço de email"},
        ParaVerSuId: { es: "Para verificar su identidad, se le enviará un código de 6 dígitos a su dirección de correo electrónico. Una vez recibido este código lo puede utilizar para crear una nueva contraseña.", pt:"Para verificar sua identidade, um código de 6 dígitos será enviado para seu endereço de e-mail. Depois de receber este código, você pode usá-lo para criar uma nova senha."},
        CodRec: { es: "Código de recuperação", pt:"Código Recuperación"},
        RepetirContra: { es: "Repetir Nueva Contraseña", pt:"Repita a nova senha"},
        //GeneralPage
        IdiomaInter: { es: "Idioma de la Interfaz de Usuario", pt:"Idioma da interface do usuário"},
        RequiereRecargar: { es: "Requiere recargar la página para ver los cambios", pt:"Requer recarregar a página para ver as alterações"},
        //GridPage
        Rango: { es: "Rango", pt:"Faixa"},
        Grossor: { es: "Grosor", pt:"Grossura"},
        Colorrr: { es: "Color", pt:"Cor"},
        LineaS: { es: "Línea Secundaria", pt:"Linha Secundaria"},
        LineaP: { es: "Línea Principal", pt:"Linha Principal"},

        //MapTypePage
        SelMapBase: { es: "Seleccione el Mapa Base", pt:"Selecione o Mapa Base"},
        SelMapBase01: { es: "Mostrar_Nombres", pt:"Mostrar_Nomes"},
        //UserConfigPanel
        General: { es: "General", pt:"Geral"},
        Mapa: { es: "Mapa", pt:"Mapa"},
        Grilla: { es: "Grilla", pt:"Grade"},
        //ZoomPanel
        //Portal
        //index
        //3DChartScaleAzxis.html
        FactorEs: { es: "Factor de Escala", pt:"Fator de Escala"},
        EsLat: { es: "Escalar Latitud / Longitud", pt:"Escalar Latitude / Longitude"},
        EscEjeZ: { es: "Escalar Eje Z (metros)", pt:"Escala eixo Z (metros)"},
        //Winfo.html
        Winfo1: { es: "Información", pt:"Informação"},
        //WConfirm.html
        WConf1: { es: "Confirmación", pt:"Confirmação"},
        //WminZfilter.html
        WminZ_01: { es: "Filtrar resultados", pt:"Filtrar resultados"},
        WminZ_02: { es: "Seleccionar [", pt:"Selecionar ["},
        WminZ_03: { es: "Muchos valores. Use opción 'Buscar'", pt:"Muitos valores. Use a opão buscar"},
        //WSeleccionaFecha.html
        WSelF_01: { es: "Ingreso de Fecha", pt:"Entrada de data"},
        //WselectVariables.html 
        WselVar_01: { es: "Seleccionar", pt:"Selecionar"},
        //TimeSerieTime. html
        TST_00: { es: "Tiempo", pt:"Tempo"},
        TST_01: { es: "Temporalidad", pt:"Temporalidade"},
        TST_02: { es: "Desde", pt:"De"},
        TST_03: { es: "días", pt:"dias"},
        TST_04: { es: "Hasta", pt:"Até"},
  
    },

    //javascripts
    javascripts: {

        //WselectVariables.js
        WselVariables_01: { es: "Variables en Centro", pt:"Variáveis ​no Centro"},
        WselVariables_02: { es: "Medidas por las Estaciones", pt:"Medições por Estações"},
        WselVariables_03: { es: "Otras Variables en el mismo Punto", pt:"Outras variáveis ​​no mesmo ponto"},
        WselVariables_04: { es: "Monitoreadas en la Estaciones", pt:"Monitorados nas Estações"},
        WselVariables_05: { es: "Otras Variables en el mismo Punto", pt:"Outras variáveis ​​no mesmo ponto"},
        WselVariables_06: { es: "Seleccionar", pt:"Selecionar"},
        WselVariables_07: { es: "Seleccionar", pt:"Selecionar"},

        //
        importarCapa: { es: "Importar Capa", pt: "Importar Capa"},
        nuevoGrupodecapas: { es: "Nuevo Grupo de Capas", pt: "Novo Grupo de Camadas"},
        PropriedadesDelGrupo: { es: "Propiedades del Grupo", pt: "Propriedades do Grupo"},
        Estaciones: { es: "Estaciones", pt: "Estações"},
        ConfirmaDesea: { es: "¿Confirma que desea eliminar el objeto '", pt: "Confirma que deseja eliminar o objeto"},
        SelectorTiempo: { es: "Selector Tiempo: BÁSICO", pt: "Seletor de tempo: BÁSICO"},
        SelectorTiempoCAPA: { es: "Selector Tiempo: CAPA", pt: "Seletor de tempo: CAPA"},
        NoHayCapas: { es: "No hay capas", pt: "sem camadas"},
        NoHaAgregado: { es: "No ha agregado capas con temporalidad definida", pt: "Você não adicionou camadas com temporalidade definida"},
        //Time js
        FijarTiempo: { es: "Fijar Tiempo de Inicio", pt: "Definir hora de início"},
        FijarTiempo2: { es: "Fijar Tiempo de Término", pt: "Definir hora de término"},
        Time1: { es: "Generar Animación", pt: "Gerar Animação"},
        Time2: { es: "Debe fijar el tiempo de inicio y de término antes de generar la animación", pt: "Você deve definir o horário de início e término antes de gerar a animação"},
        Time3: { es: "Debe fijar el tiempo de término después del tiempo de inicio", pt: "Você deve definir a hora de término após a hora de início"},
        //geoos-groups-layers js
        ObjUser: { es: "Objetos de Usuario", pt: "Objetos do usuário"},
        PropG: { es: "Propiedades del Grupo", pt: "Propriedades do grupo"},
        PropCapa: { es: "Propiedades de la Capa", pt: "Propriedades da Camada"},

        //Wlibrary js
        nn1: { es: "Todos los Temas", pt: "Todos os Temas"},
        nn2: { es: "Seleccione una Capa a la izquierda para ver sus detalles", pt: "Selecione uma camada à esquerda para ver seus detalhes"},
        nn3: { es: "No se encontraron capas. Repita la búsqueda", pt: "Nenhuma camada encontrada. pesquisa repetida"},
        nn4: { es: "¿Está seguro que desea eliminar permanentemente esta capa de la biblioteca?", pt: "Tem certeza de que deseja remover permanentemente esta camada da biblioteca?"},
        //Main js
        nn5: { es: " No hay layer codes", pt: " Não há códigos de camada"},
        //AddStationsPanel + AddPanel.js
        nn6: { es: "  estaciones encontradas", pt: "  estações encontradas"},
        nn7: { es: "No hay estaciones seleccionadas", pt: "Nenhuma estação selecionada"},
        nn8: { es: "Una estación seleccionada", pt: "Uma estação selecionada"},
        nn9: { es: "Filtrar por Tema", pt: "Filtrar por Tema"},
        nn10: { es: "Filtrar por Proveedor o Agencia", pt: "Filtrar por Provedor ou Agência"},
        nn11: { es: "Filtrar por Tipo de Información", pt: "Filtrar por tipo de informação"},
        nn12: { es: "Revisar provider, es obligatorio", pt: "Verifique o provedor, é obrigatório"},
        nn13: { es: "Filtrar por Zona o Región", pt: "Filtrar por Zona ou Região"},
        nn14: { es: "La capa no continene la seccion ", pt: "A camada não contém a seção "},
        nn15: { es: "Limpiar Filtros", pt: "Limpar Filtros"},
        nn16: { es: "Las capas especiales se deben configurar y agregar a favoritos sólo desde 'Mi Panel'", pt: "Camadas especiais devem ser configuradas e adicionadas aos favoritos apenas em 'Meu Painel'"},
        nn17: { es: "Las capas especiales no tienen información adicional", pt: "Camadas especiais não possuem informações adicionais"},
        nn18: { es: "Filtrar por Tipo de Estación", pt: "Filtrar por Tipo de Estação"},
        nn19: { es: "Filtrar por Sensor / Variable Monitoreada", pt: "Filtrar por Sensor / Variável Monitorada"},
        nn20: { es: "Filtros Activos: ", pt: "Filtros Ativos: "},
        nn21: { es: "Descargar Datos de Estación", pt: "Baixar dados da estação"},
        nn22: { es: "Limpiar Filtro", pt: "Limpar Filtro"},
        //AddPanel.js + etc
        Var1 : { es: "Variables", pt: "Variáveis"},
        Var2 : { es: " Variable", pt: " Variável"},
        Var3 : { es: "No Hay ", pt: "Não Há "},
        Var4 : { es: "  Seleccionadas", pt: "  Selecionadas"},
        Var5 : { es: " Una", pt: " Uma"},
        Var6 : { es: " Seleccionada", pt: " Selecionada"},
        Var7 : { es: "Variables", pt: "Variáveis"},
        Capa1 : { es: " Capa", pt: " Camada"},
        //
        datafrase1 : { es: " No hay descripción de la Capa", pt: " Não há descrição da camada"},
        datafrase2 : { es: "No hay detalles de la Capa", pt: "Sem detalhes da capa"},
        datafrase3 : { es: "No hay detalles de la disponibilidad en GEOOS para la Capa", pt: "Não há detalhes da disponibilidade em GEOOS para a Camada"},
        datafrase4 : { es: "Vista 3D de Terreno y Nubosidad", pt: "Terreno 3D e Nebulosidade"},
        datafrase5 : { es: "Terreno y Nubosidad", pt: "Terreno e Nebulosidade"},
        datafrase6: { es: "Seleccione el Área para Analizar", pt: "Selecione a Área para Analisar"},
        datafrase7 : { es: "Seleccione el Área para los datos del Gráfico", pt: "Selecione a área para os dados do gráfico"},
        datafrase8 : { es: "Nombre del Análisis", pt: "Nome da Análise"},
        datafrase9 : { es: "Escalar Ejes", pt: "Eixos de Escala"},
        datafrase10 : { es: "Selección de Variable", pt: "Seleção de variável"},
        datafrase11 : { es: "Escala de Colores", pt: "Escala de Cores"},
        datafrase12 : { es: "Mostrar Grilla de Coordenadas", pt: "Mostrar grelha de coordenadas"},
        datafrase13 : { es: "No hay datos", pt: "Não há dados"},
        datafrase14 : { es: "Cargando ...", pt: "Carregando ..."},

        //meses
        mes1 : { es: "Enero", pt: "Janeiro"},
        mes2 : { es: "Febrero", pt: "Fevereiro"},
        mes3 : { es: "Marzo", pt: "Março"},
        mes4 : { es: "Abril", pt: "Abril"},
        mes5 : { es: "Mayo", pt: "Maio"},
        mes6 : { es: "Junio", pt: "Junho"},
        mes7 : { es: "Julio", pt: "Julho"},
        mes8 : { es: "Agosto", pt: "Agosto"},
        mes9 : { es: "Septiembre", pt: "Setembro"},
        mes10 : { es: "Octubre", pt: "Outubro"},
        mes11 : { es: "Noviembre", pt: "Novembro"},
        mes12 : { es: "Diciembre", pt: "Dezembro"},
        //dias
        //Dia1 : { es: "Domingo", pt: "Domingo"},
        //Dia2 : { es: "Lunes", pt: "Segunda"},
        //Dia3 : { es: "Martes", pt: "Terça"},
        //Dia4 : { es: "Miércoles ", pt: "Quarta"},
        //Dia5 : { es: "Jueves", pt: "Quinta"},
        //Dia6 : { es: "Viernes", pt: "Sexta"},
        //Dia7 : { es: "Sábado", pt: "Sábado"},

        //addstationspanel
        add1 : { es: " No hay descripción de la Capa", pt: " Não há descrição da Camada"},
        add2 : { es: "No hay detalles de la Capa", pt: "Sem detalhes da capa"},
        add3 : { es: "No hay detalles de la disponibilidad en GEOOS para la Capa", pt: "Não há detalhes da disponibilidade em GEOOS para a Camada"},
        //3DChartMain.js
        lv1 : { es: "La variable que se grafica es '", pt: "A variável representada graficamente é '"},
        lv2 : { es: "'. Para cambiarla haga click en el ícono de configuraciones", pt: "'. Para alterá-lo, clique no ícone de configurações"},
        //ViewTool.js 
        VT1 : { es: "ADVERTENCIA", pt: "AVISO"},
        VT2 : { es: "Si no logras visualizar el analisis generado, puedes probar activando la 'aceleración de hardware' en tu navegador.", pt: "Se você não conseguir ver a análise gerada, tente habilitar a 'aceleração de hardware' em seu navegador."},
        VT3 : { es: "Para más información visita las preguntas frequentes.", pt: "Para mais informações visite as perguntas frequentes."},
        VT4 : { es: "¿Confirma que desea eliminar el análisis '", pt: "Tem certeza que deseja remover a análise '"},
        //MyPanel.js
        MP1 : { es: "Duplicar Grupo", pt: "Duplicar Grupo"},
        MP2 : { es: "Exportar Grupo", pt: "Exportar Grupo"},
        MP3 : { es: "Importar Capa", pt: "Importar Camada"},
        MP4 : { es: "Agregar a Favoritos", pt: "Adicionar aos favoritos"},
        MP5 : { es: "Compartir", pt: "Compartilhar"},
        MP6 : { es: "Eliminar las capas", pt: "Eliminar as Camadas"},
        MP7 : { es: "Escalas de Colores", pt: "Escalas de Cores"},
        MP8 : { es: "Eliminar el Grupo", pt: "Eliminar o Grupo"},
        MP9 : { es: "Eliminar grupo de Capas", pt: "Eliminar grupo de camadas"},
        MP10 : { es: "¿Confirma que desea eliminar el Grupo de Capas '", pt: "Tem certeza que deseja excluir o grupo de camadas '"},
        MP11 : { es: "Advertencia", pt: "Aviso"},
        MP12 : { es: "Se ha copiado al portapapeles un enlace con el grupo exportado", pt: "Um link para o grupo exportado foi copiado para a área de transferência"},
        MP13 : { es: "Compartir Grupo de Capas", pt: "Compartilhar Grupo de Camadas"},
        MP14 : { es: "Eliminar Todas las Capas", pt: "Excluir todas as camadas"},
        MP15 : { es: "¿Confirma que desea eliminar todas las capas?", pt: "Tem certeza de que deseja remover todas as camadas?"},
        MP16 : { es: "No se pudo eliminar las capas ", pt: "Não foi possível excluir as camadas "},
        MP17 : { es: "Duplicar Capa", pt: "Duplicar Camada"},
        MP18 : { es: "Exportar Capa", pt: "Exportar Camada"},
        MP19 : { es: "Compartir en Biblioteca", pt: "Compartilhar na Biblioteca"},
        MP20 : { es: "Eliminar la capa", pt: "Eliminar a Camada"},
        MP21 : { es: "Eliminar Capa", pt: "Eliminar Camada"},
        MP22 : { es: "¿Confirma que desea eliminar la Capa '", pt: "Tem certeza que deseja excluir Layer '"},
        MP23 : { es: "El archivo cargado no corresponde a una Capa exportada", pt: "O arquivo carregado não corresponde a uma Camada exportada"},
        MP24 : { es: "El archivo cargado no corresponde a un Grupo exportado", pt: "O arquivo enviado não corresponde a um grupo exportado"},
        
        //FormulaConfig.js
        FC1 : { es: "JavaScript por Punto en Browser", pt: "JavaScript por ponto no navegador"},
        FC2 : { es: "JavaScript por Punto en Servidor", pt: "JavaScript por ponto no servidor"},
        //Sources.js 
        Dias1: { es: "Días", pt: "Dias"},
        //WFormula.js
        WF1: { es: "No se encontró la función 'z' en el código", pt: "Função 'z' não encontrada no código"},
        //Tolerance.js
        Anos1: { es: "Años", pt: "Anos"},
        //Watchers.js
        Watchers1: { es: ">> Observar Nuevas Variables", pt: ">> Observar Novas Variáveis"},
        //FavGroups.js
        FG1: { es: "¿Confirma que desea eliminar el Grupo?", pt: "Tem certeza de que deseja excluir o Grupo?"},
        //FavStations.js
        FG2: { es: "¿Confirma que desea eliminar la Estación?", pt: "Tem certeza de que deseja excluir a Estação?"},
        //WPublish.js
        WP_01: { es: "La imagen debe ser de tipo PNG o JPG", pt: "A imagem deve ser do tipo PNG ou JPG"},
        WP_02: { es: "Debe cargar una imagen que represente la capa que está publicando", pt: "Você deve carregar uma imagem que represente a camada que você está publicando"},
        WP_03: { es: "Debe ingresar un nombre para mostrar", pt: "Você deve inserir um nome de exibição"},
        WP_04: { es: "Debe seleccionar al menos un tema o categoría para la capa de desea publicar.", pt: "Você deve selecionar pelo menos um tópico ou categoria para a camada que deseja publicar."},
        //Final.js
        Final01: { es: "los datos originales reportados por la estación", pt: "os dados originais relatados pela estação"},
        Final02: { es: "un día", pt: "Um dia"},
        Final03: { es: "las estadísticas acumuladas en grupos de ", pt: "as estatísticas acumuladas em grupos de"},
        Final04: { es: " de la estación", pt: "da estação"},
        Final05: { es: ", exportar los valores de una variable", pt: ", exporte os valores de uma variável"},
        Final06: { es: ", exportar los valores de ", pt: ", exporte os valores de"},
        Final07: { es: " variables", pt: " variáveis"},
        Final08: { es: " para el período comprendido entre ", pt: "para el período comprendido entre"},
        Final09: { es: "el día ", pt: "o dia"},
        Final10: { es: " variables", pt: " variáveis"},
        Final11: { es: " y el día ", pt: "e o dia"},
        Final12: { es: "el mes de ", pt: "o mês de"},
        Final13: { es: " y el mes de ", pt: "e o mês de"},
        Final14: { es: "el día ", pt: "o dia"},
        Final15: { es: "tiempo", pt: "tempo"},
        Final16: { es: "una hora", pt: "Uma hora"},
        Final17: { es: "un mes", pt: "Um mês"},
        //Periodo.js
        Pe01: { es: "El Período es Inválido", pt: "O período é inválido"},
        Pe02: { es: "La exportación de los datos originales de una estación no puede ser para un período mayor a un mes", pt: "A exportação dos dados originais de uma estação não pode ser por um período superior a um mês"},
        Pe03: { es: "Demasiados datos para exportar, por favor reducirlos. Puede acortar el período, escoger una agrupación temporal más alta o disminuir el número de variables", pt: "Muitos dados para exportar, reduza-os. Você pode encurtar o período, escolher um agrupamento temporal maior ou diminuir o número de variáveis."},
        //SelVariables.js
        SV_01: { es: "No se encontró el dataSet '", pt: "DataSet não encontrado '"},
        SV_02: { es: "' en zRepo", pt: "' en zRepo"},
        SV_03: { es: "No se encontró la variable ", pt: "Variável não encontrada "},
        SV_04: { es: "Valor Promedio del Grupo", pt: "Valor Médio do Grupo"},
        SV_05: { es: " Valor Mínimo en el Grupo", pt: "Valor Mínimo no Grupo"},
        SV_06: { es: "Valor Máximo en el Grupo", pt: "Valor Máximo no Grupo"},
        SV_07: { es: "N° Muestras en el Grupo", pt: "Nº de Amostras no Grupo"},
        //WAnim.js
        WA_01: { es: "Debe fijar el tiempo de inicio y de término antes de generar la animación", pt: "Você deve definir o horário de início e término antes de gerar a animação"},
        WA_02: { es: "Debe fijar el tiempo de término después del tiempo de inicio", pt: "Você deve definir a hora de término após a hora de início"},
        WA_03: { es: "Generando cuadros ...", pt: "Gerando quadros..."},
        WA_04: { es: "Cuadro ", pt: "Gráfico"},
        WA_05: { es: " generado en ", pt: " gerado em "},
        WA_06: { es: "Generando mp4", pt: "Gerando mp4"},
        WA_07: { es: "Espere la descarga", pt: "aguarde o download"},
        //SelectRasterVariable.js
        SVble_01: { es: "Seleccionar Variable", pt: "Selecionar Variável"},
        //Profile.js
        PROFILE_01: { es: "La imagen debe ser de tipo PNG o JPG", pt: "A imagem deve ser do tipo PNG ou JPG"},
        PROFILE_02: { es: "Arrastre una foto hasta la imagen", pt: "Arraste uma foto para a imagem"},
        //Register.js
        REG_01: { es: "Se le enviará un código de 6 dígitos para verificar su dirección de correo electrónico.", pt: "Você receberá um código de 6 dígitos para verificar seu endereço de e-mail."},
        REG_02: { es: "Espere unos minutos que el código llegue a su correo. Para enviar nuevamente, use el botón de envío. Sólo el último código enviado será válido.", pt: "Aguarde alguns minutos para que o código chegue em seu e-mail. Para enviar novamente, use o botão enviar. Somente o último código enviado será válido."},
        REG_03: { es: "Debe ingresar su nombre", pt: "Você deve inserir seu nome"},
        REG_04: { es: "Debe ingresar una contraseña de 4 caracteres o más.", pt: "Você deve digitar uma senha de 4 caracteres ou mais."},
        REG_05: { es: "La contraseña y su repetición son diferentes", pt: "A senha e sua repetição são diferentes"},
        REG_06: { es: "E-mail inválido", pt: "E-mail inválido"},
        //WCAmbiaPwd.js
        WCPwd_01: { es: "La contraseña y su repetición son diferentes", pt: "A senha e sua repetição são diferentes"},
        WCPwd_02: { es: "La contraseña debe tener al menos cuatro caracteres de largo", pt: "A senha deve ter pelo menos quatro caracteres"},
        WCPwd_03: { es: "Su contraseña ha sido modificada", pt: "Sua senha foi mudada"},
        //WCode.js
        WCode_01: { es: "Debe ingresar código de registro válido", pt: "Você deve inserir um código de registro válido"},
        //WOlvidoPwd.js
        Olvido_pwd_01: { es: "La contraseña debe tener al menos cuatro caracteres de largo", pt: "A senha deve ter pelo menos quatro caracteres"},
        //GridPage.js
        GPage_01: { es: "No Mostrar", pt: "Não Mostrar"},
        GPage_02: { es: "Espaciado Automático", pt: "Espaçamento Automático"},
        GPage_03: { es: "Cada 2 grados y 30 minutos", pt: "A cada 2 graus e 30 minutos"},
        GPage_04: { es: "Cada 5 grados", pt: "a cada 5 graus"},
        GPage_05: { es: "Cada 1 grado", pt: "a cada 1 grau"},
        GPage_06: { es: "Cada 10 grados", pt: "a cada 10 graus"},
        //Main.js
        Mainjs_01: { es: "agregó capa", pt: "camada adicionada"},
        //geoos.js 
        geoos_01: { es: "Sin Región Especificada", pt: "Sem Região Especifica"},
        geoos_02: { es: "Sin Tema Especificado", pt: "Sem Tema Especificado"},
        geoos_03: { es: "Sin Tipo Especificado", pt: "Sem Tipo Especificado"},
        geoos_04: { es: "No se encontró la variable ", pt: "Não encontrou a variável "},
        geoos_05: { es: " referenciada desde la estación ", pt: " referenciado da estação "},
        geoos_06: { es: " en el servidor ", pt: " no servidor "},
        geoos_07: { es: "La estación ", pt: "A estação"},
        geoos_08: { es: " en ", pt: " em "},
        geoos_09: { es: " no define variables", pt: "não define variáveis"},
        geoos_10: { es: "[ERROR] No puede eliminar el último grupo", pt: "[ERRO] Não é possível excluir o último grupo"},
        geoos_11: { es: "No hay capa de estaciones", pt: "Não há camada de estações"},
        geoos_12: { es: "Archivos del tipo de '", pt: "Arquivos do tipo '"},
        geoos_13: { es: "' no manejado", pt: "' não tratado"},
        //Werro html
        werro_01: { es: "Ha ocurrido un Error en la Operación", pt: "Ocorreu um erro de operação"},
        //geoos-query.js
        ley_01: { es: "         Leyendas", pt: "         Legendas"},
        ley_02: { es: "Colorear", pt: "Colorir"},
        //geoos-stations-layer.js
        geost_01: { es: "Observar Variables", pt: "Observar Variáveis"},
        geost_02: { es: "Escala de Colores", pt: "Escala de Cores"},
        geost_04: { es: "Estaciones", pt: "Estações"},

        //geoos-user-objects-layer.js
        geost_03: { es: "Propriedades del Objeto", pt: "Propriedades do Objeto"},
        //geoos-raster-layer.js
        geosr_01: { es: "Sin Información", pt: "Sem Informação"},
        geosr_02: { es: "Configurar Capa de Fórmula", pt: "Definir Camada de Fórmula"},
        geosr_03: { es: "Variables de Entrada a la Fórmula", pt: "Variáveis ​​de entrada de fórmula"},
        //isolenes.js
        geosi_01: { es: "Configurar Isolineas", pt: "Configurar Isolinhas"},
        geosi_02: { es: "Extraer Niveles Fijos", pt: "Extrair Níveis Fixos"},
        geosi_03: { es: "Isolineas", pt: "Isolinhas"},
        //data-points.js
        geosdata_01: { es: "Puntos con Datos", pt: "Pontos com Dados"},
        //vectores.js
        geosvec_01: { es: "Vectores", pt: "Vetores"},
        //timeserie.js
        timeserie_01: { es: "Selección de Variables", pt: "Seleção de variável"},
        timeserie_02: { es: "Configurar Temporalidad", pt: "Configurar a temporalidade"},
        timeserie_03: { es: "temporalidad ", pt: "temporalidade "},
        timeserie_04: { es: " no está manejada en serie de tiempo", pt: "não é baseado em séries temporais"},
        timeserie_05: { es: "Serie de Tiempo", pt: "Série de tempo"},
        //timeserietime.js
        timeserietime_00: { es: "Relativo al Mapa", pt: "Relativo ao Mapa"},
        timeserietime_01: { es: "Límites Fijos", pt: "Limites Fixos"},
        timeserietime_02: { es: "Inicio del Período", pt: "Início do Período"},
        timeserietime_03: { es: "Fin del Período", pt: "Fim do Período"},
        timeserietime_04: { es: "Mensual", pt: "Mensal"},
        
        //geoos-query.js
        geoos_query_01: { es: "promedio", pt: "média"},
        geoos_query_02: { es: " en mapa", pt: " no mapa"},
        geoos_query_03: { es: "Selección en Mapa", pt: "Seleção no mapa"},
        geoos_query_04: { es: "No se encontró la dimensión '", pt: "Dimensão não encontrada '"},
        geoos_query_05: { es: "No se encontró la estación ", pt: "estação não encontrada"},
        geoos_query_06: { es: "No se encontró el filtro por ", pt: "Filtro não encontrado por "},
        geoos_query_07: { es: "No se puede agregar estacion ", pt: "Não é possível adicionar estação"},
        //Exporter.js
        exp_01: { es: "Estación: ", pt: "Estação: "},
        exp_02: { es: "Estación", pt: "Estação"},
        exp_03: { es: "y", pt: "e"},
        //Timeserievars.js
        timeserie_01: { es: "Seleccionar Variable Principal", pt: "Selecionar a variável principal"},
        timeserie_02: { es: "Comparar con Variable", pt: "Comparar com Variável"},
        //SelectorFecha.js
        expS_01: { es: "Temporalidad ", pt: "Temporalidade"},
        expS_02: { es: " no soportada", pt: " não suportada"},
        //WMinZFilters.js
        expSW_01: { es: "No se encontraron resultados", pt: "Resultados nao encontrados"},
        expSW_02: { es: "Muchos valores. Refine la búsqueda", pt: "Muitos valores. Refaça a busca"},
        //DataPointsVisualizer.js
        demasiado_punto: { es: "Demasiados puntos. Aumente Zoom", pt: "Existem muitos dados, aumente o zoom"},
        //Mailer
        Mailer_01: { es: "No se ha configurado un servidor SMTP en este portal", pt: "Não existe servidor SMTP configurado para este portal"},
        Mailer_02: { es: "No se ha configurado un servidor correo en este portal", pt: "Não existe servidor de correio configurado para este portal"},
        Mailer_03: { es: "El correo ingresado ya se encuentra registrado en GEOOS. Use la opción 'Iniciar Sesión'. Desde ahí puede luego seleccionar 'Olvidó Contraseña' si es necesario.", pt: "O e-mail informado já está cadastrado no GEOOS. Use a opção 'Entrar'. A partir daí, você pode selecionar 'Esqueceu a senha', se necessário."},
        Mailer_04: { es: "Registro de Cuenta en GEOOS", pt: "Registo de Conta GEOOS"},

    }   
    }

if (window) {
    window.mensajes = mensajes
    window.languages = [

         {code:"es", name: "Español"
    }, 
    {
        code:"pt", name: "Português"
}]
} else {
    module.exports = mensajes;
}