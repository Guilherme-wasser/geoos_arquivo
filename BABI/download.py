from ftplib import FTP
import os

# Função para salvar o nome da última pasta processada
def salvar_ultima_pasta_processada(nome_pasta):
    with open('/opt/geoos/BABI/ultima_pasta_processada.txt', 'w') as f:
        f.write(nome_pasta)

# Função para ler o nome da última pasta processada
def ler_ultima_pasta_processada():
    try:
        with open('/opt/geoos/BABI/ultima_pasta_processada.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ''

# Informações do servidor FTP
ftp_host = '200.17.232.3'
ftp_user = 'G_Souza'
ftp_passwd = 'Gavet@2000'

# Conexão com o servidor FTP
ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_passwd)

# Entrando no Diretório de trabalho no servidor FTP
ftp.cwd('/Public/BSO/Backup/Babitonga')

# Listando conteúdo do diretório e selecionando a última pasta
conteudo_diretorio = ftp.nlst()
conteudo_diretorio.sort()  # Ordena as pastas pelo nome
ultima_pasta = conteudo_diretorio[-1]  # Seleciona a última pasta

print(conteudo_diretorio)

ultima_pasta_processada = ler_ultima_pasta_processada()

if ultima_pasta != ultima_pasta_processada:
    ftp.cwd(ultima_pasta)  # Entra na última pasta
    arquivos_para_baixar = ftp.nlst()  # Lista os arquivos na última pasta
    
    for nome_arquivo in arquivos_para_baixar:
        caminho_local = f'/opt/geoos/data/UFPR/Babitonga/{nome_arquivo}'
        with open(caminho_local, 'wb') as arquivo_local:
            ftp.retrbinary(f'RETR {nome_arquivo}', arquivo_local.write)
        print(f'Arquivo {nome_arquivo} baixado com sucesso.')
    
    salvar_ultima_pasta_processada(ultima_pasta)
else:
    print('Nenhum arquivo novo para baixar.')

print("processo finalizado")

# Fechar a conexão FTP
ftp.quit()
