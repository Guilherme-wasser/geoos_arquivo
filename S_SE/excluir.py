import os

def excluir_arquivos_pasta(caminho_pasta):
    # Checa se o caminho especificado é realmente uma pasta
    if not os.path.isdir(caminho_pasta):
        print("O caminho especificado não é uma pasta.")
        return

    # Lista todos os arquivos e pastas dentro do caminho especificado
    for nome_arquivo in os.listdir(caminho_pasta):
        # Cria o caminho completo até o arquivo
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        # Checa se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_arquivo):
            # Exclui o arquivo
            os.remove(caminho_arquivo)
            print(f"Arquivo {nome_arquivo} excluído com sucesso.")
        else:
            print(f"O item '{nome_arquivo}' é uma pasta e não será excluído.")

# Caminho para a pasta de onde você quer excluir os arquivos
caminho_da_pasta = "/opt/geoos/data/UFPR/S_SE"

# Chama a função para excluir arquivos da pasta especificada
excluir_arquivos_pasta(caminho_da_pasta)

