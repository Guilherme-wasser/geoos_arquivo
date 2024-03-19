import ftplib
import os
from shutil import copyfile
import datetime

# Configurações FTP
FTP_SERVER = '200.17.232.3'
FTP_USER = 'G_Souza'
FTP_PASSWORD = 'Gavet@2000'
FTP_TARGET_FOLDER = '/Public/BSO/Backup/S_SE'

# Configurações locais
LOCAL_APP_FOLDER = '/opt/geoos/portal/Oil_Spill_Tool/GeneralData/Metocean/'
WRF_FILE = os.path.join(LOCAL_APP_FOLDER, 'wrf.hdf5')  # Localização do arquivo wrf.hdf5

try:
    # Conecta ao servidor FTP
    ftp = ftplib.FTP(FTP_SERVER)
    ftp.login(FTP_USER, FTP_PASSWORD)
    ftp.cwd(FTP_TARGET_FOLDER)

    # Lista as pastas no diretório alvo
    folders = ftp.nlst()

    # Garante que só vamos manter dados dos últimos 30 dias
    today = datetime.datetime.now()
    date_threshold = today - datetime.timedelta(days=30)
    folders_to_keep = [folder for folder in folders if datetime.datetime.strptime(folder.split('_')[0], '%Y%m%d') >= date_threshold]

    for folder in folders_to_keep:
        ftp.cwd(f'{FTP_TARGET_FOLDER}/{folder}')
        filenames = ftp.nlst()
        local_folder_path = os.path.join(LOCAL_APP_FOLDER, folder)
        hydro_file_downloaded = False
        water_file_downloaded = False
        
        for filename in filenames:
            if 'Hydrodynamic_2_Surface.hdf5' in filename:
                hydro_file_downloaded = True
                local_file_path = os.path.join(local_folder_path, filename)
                os.makedirs(local_folder_path, exist_ok=True)  # Cria a pasta local se ainda não existir
                with open(local_file_path, 'wb') as file:
                    ftp.retrbinary(f'RETR {filename}', file.write)
            
            elif 'WaterProperties_2_Surface.hdf5' in filename:
                water_file_downloaded = True
                local_file_path = os.path.join(local_folder_path, filename)
                os.makedirs(local_folder_path, exist_ok=True)  # Cria a pasta local se ainda não existir
                with open(local_file_path, 'wb') as file:
                    ftp.retrbinary(f'RETR {filename}', file.write)

        # Copia o arquivo wrf.hdf5 apenas se ambos os arquivos foram baixados
        if hydro_file_downloaded and water_file_downloaded:
            copyfile(WRF_FILE, os.path.join(local_folder_path, 'wrf.hdf5'))

    # Manutenção dos dados (remove os dados mais antigos se necessário)
    local_folders = os.listdir(LOCAL_APP_FOLDER)
    local_folders.sort()
    while len(local_folders) > 30:
        oldest_folder = local_folders.pop(0)
        oldest_folder_path = os.path.join(LOCAL_APP_FOLDER, oldest_folder)
        if os.path.isdir(oldest_folder_path):
            for filename in os.listdir(oldest_folder_path):
                os.remove(os.path.join(oldest_folder_path, filename))
            os.rmdir(oldest_folder_path)

    ftp.quit()
except Exception as e:
    print(f"Erro ao conectar ou operar no servidor FTP: {e}")
