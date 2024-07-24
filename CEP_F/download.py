from ftplib import FTP
import os

# Informações do servidor FTP
ftp_host = '200.17.232.3'
ftp_user = 'G_Souza'
ftp_passwd = 'Gavet@2000'

# Nome da pasta específica de onde baixar os arquivos (atualize conforme necessário)
nome_pasta_especifica = '20240418_20240419'

# Lista de arquivos específicos para baixar
arquivos_especificos = [
    'Hydrodynamic_2_Surface.hdf5',
    'WaterProperties_2_Surface.hdf5'
]

# Conexão com o servidor FTP
ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_passwd)

# Entrando no Diretório de trabalho no servidor FTP
ftp.cwd(f'/Public/BSO/Backup/CEP/{nome_pasta_especifica}')

# Para cada arquivo na lista de arquivos específicos, verifica se está disponível e baixa
for nome_arquivo in arquivos_especificos:
    caminho_local = f'/opt/geoos/data/UFPR/CEP/{nome_arquivo}'
    # Verifica se o diretório local existe, se não, cria
    os.makedirs(os.path.dirname(caminho_local), exist_ok=True)
    with open(caminho_local, 'wb') as arquivo_local:
        ftp.retrbinary(f'RETR {nome_arquivo}', arquivo_local.write)
    print(f'Arquivo {nome_arquivo} baixado com sucesso.')

print("Processo finalizado")

# Fechar a conexão FTP
ftp.quit()
