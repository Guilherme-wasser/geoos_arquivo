import subprocess

# Definir a ordem dos scripts a serem executados
scripts_para_executar = ["download.py", "transf.py", "transf2.py", "BABI_V.py", "BABI_U.py", "altura.py","temperatura.py", "salinidade.py", "excluir.py"]

# Definir o caminho onde os scripts estão localizados
caminho_dos_scripts = "/opt/geoos/BABI_F/"

# Executar cada script por vez
for script in scripts_para_executar:
    try:
        subprocess.run(["python3", f"{caminho_dos_scripts}{script}"], check=True)
        print(f"Script {script} executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script {script}: {e}")
    except Exception as e:
        print(f"Erro inesperado ao executar o script {script}: {e}")
