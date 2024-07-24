import os

def executar_script(caminho_script):
    """
    Função para executar um script Python localizado em um caminho específico.
    """
    with open(caminho_script) as f:
        codigo = f.read()
        exec(codigo)

# Diretório base onde os scripts estão localizados
diretorio_base = "/opt/geoos"

# Caminhos dos scripts a serem executados
caminhos_scripts = [
    "download_ftp_metocean.py",
    "S_SE/todos.py",
    "CEP/todos.py",
    "FPOLIS/todos.py",
    "BABI/todos.py",
    "NORTE/todos.py",
    "SCPRSP/todos.py"
]

for caminho_rel in caminhos_scripts:
    caminho_abs = os.path.join(diretorio_base, caminho_rel)
    print(f"Executando {caminho_abs}...")
    executar_script(caminho_abs)
    print(f"{caminho_abs} executado com sucesso!\n")

