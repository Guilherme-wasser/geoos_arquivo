"""
import ftplib
import os
from shutil import copyfile
import datetime

# Configurações FTP
FTP_SERVER = '200.17.232.3'
FTP_USER = 'G_Souza'
FTP_PASSWORD = 'Gavet@2000'
FTP_FOLDERS = {
    'S_SE': '/Public/BSO/Backup/S_SE',
    'CEP': '/Public/BSO/Backup/CEP',
    'SC_PR_SP': '/Public/BSO/Backup/SC_PR_SP',
    'Babitonga': '/Public/BSO/Backup/Babitonga'
}

# Configurações locais
LOCAL_FOLDERS = {
    'S_SE': '/opt/geoos/portal/Oil_Spill_Tool/GeneralData/Metocean/S_SE/',
    'CEP': '/opt/geoos/portal/Oil_Spill_Tool/GeneralData/Metocean/CEP/',
    'SC_PR_SP': '/opt/geoos/portal/Oil_Spill_Tool/GeneralData/Metocean/PR_SC/',
    'Babitonga': '/opt/geoos/portal/Oil_Spill_Tool/GeneralData/Metocean/Babitonga/'
}
LOCAL_APP_FOLDER_BASE = '/opt/geoos/portal/Oil_Spill_Tool/GeneralData/Metocean/'

WRF_FILE = os.path.join(LOCAL_APP_FOLDER_BASE, 'wrf.hdf5')  # Localização do arquivo wrf.hdf5

def download_ftp_files(ftp_folder, local_folder):
    try:
        ftp.cwd(ftp_folder)
        folders = ftp.nlst()

        # Garante que só vamos manter dados dos últimos 30 dias
        today = datetime.datetime.now()
        date_threshold = today - datetime.timedelta(days=30)
        folders_to_keep = [folder for folder in folders if datetime.datetime.strptime(folder.split('_')[0], '%Y%m%d') >= date_threshold]

        for folder in folders_to_keep:
            ftp.cwd(f'{ftp_folder}/{folder}')
            filenames = ftp.nlst()
            local_folder_path = os.path.join(local_folder, folder)
            hydro_file_downloaded = False
            water_file_downloaded = False

            # Verifica se os arquivos específicos já existem antes de tentar baixá-los
            for filename in filenames:
                if 'Hydrodynamic_2_Surface.hdf5' in filename or 'WaterProperties_2_Surface.hdf5' in filename:
                    local_file_path = os.path.join(local_folder_path, filename)
                    if not os.path.exists(local_file_path):  # Baixa apenas se o arquivo não existir
                        os.makedirs(local_folder_path, exist_ok=True)  # Cria a pasta local se ainda não existir
                        with open(local_file_path, 'wb') as file:
                            ftp.retrbinary(f'RETR {filename}', file.write)
                        if 'Hydrodynamic_2_Surface.hdf5' in filename:
                            hydro_file_downloaded = True
                        elif 'WaterProperties_2_Surface.hdf5' in filename:
                            water_file_downloaded = True

            # Copia o arquivo wrf.hdf5 para o diretório local se ambos os arquivos forem baixados
            wrf_local_file_path = os.path.join(local_folder_path, 'wrf.hdf5')
            if hydro_file_downloaded and water_file_downloaded and not os.path.exists(wrf_local_file_path):
                copyfile(WRF_FILE, wrf_local_file_path)

        # Manutenção dos dados (remove os dados mais antigos se necessário)
        local_folders = os.listdir(local_folder)
        local_folders.sort()
        while len(local_folders) > 30:
            oldest_folder = local_folders.pop(0)
            oldest_folder_path = os.path.join(local_folder, oldest_folder)
            if os.path.isdir(oldest_folder_path):
                for filename in os.listdir(oldest_folder_path):
                    os.remove(os.path.join(oldest_folder_path, filename))
                os.rmdir(oldest_folder_path)

    except Exception as e:
        print(f"Erro ao conectar ou operar no servidor FTP: {e}")

print("Baixando dados da NAS para o modelo de óleo")

try:
    # Conecta ao servidor FTP
    ftp = ftplib.FTP(FTP_SERVER)
    ftp.login(FTP_USER, FTP_PASSWORD)

    # Loop para processar todas as pastas FTP e locais
    for key in FTP_FOLDERS:
        download_ftp_files(FTP_FOLDERS[key], LOCAL_FOLDERS[key])

    ftp.quit()
except Exception as e:
    print(f"Erro ao conectar ou operar no servidor FTP: {e}")

"""
import ftplib
import os
from shutil import copyfile
import datetime

# Configurações FTP
FTP_SERVER = '200.17.232.3'
FTP_USER = 'G_Souza'
FTP_PASSWORD = 'Gavet@2000'
FTP_TARGET_FOLDER = '/Public/BSO/Backup/S_SE/'

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
