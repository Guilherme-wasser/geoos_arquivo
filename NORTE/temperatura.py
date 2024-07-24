#importar bibliotecas e modulos
from datetime import datetime, timedelta
import subprocess
import netCDF4 as nc
import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import time
import docker
import shutil
import os


def temperatura():

    #função para buscar a hora dentro do arquivo a ser tratado
    def achar_hora():
            ds = xr.open_dataset('/opt/geoos/data/UFPR/NORTE/WaterProperties_2_Surface.nc')
            dt = ds['time'].values
            formatted_dates_dict = {}

            for i, np_datetime in enumerate(dt, start=1):
                py_datetime = pd.to_datetime(str(np_datetime))
                print(f"Original datetime: {py_datetime}")  # imprimindo datetime original

                py_datetime += timedelta(hours=3)  # adicionando 3 horas
                print(f"Adjusted datetime: {py_datetime}")  # imprimindo datetime após adição das horas

                date_str = py_datetime.strftime("%Y-%m-%d_%H-%M")
                formatted_dates_dict[f"data{i:02}"] = date_str
                print(f"data{i:02}: {date_str}")  # imprimindo o resultado

            return formatted_dates_dict

    def encontrar_nomes_bandas(host_directory):
        arquivos = os.listdir(host_directory)

        for arquivo in arquivos:
            if arquivo.endswith(".nc"):
                caminho_arquivo = os.path.join(host_directory, arquivo)
                dataset = nc.Dataset(caminho_arquivo, 'r+')
                variaveis = dataset.variables.keys()
                bandas = [variavel for variavel in variaveis if variavel.startswith("Band")]

                if bandas:
                    print("Arquivo: {}".format(arquivo))
                    for banda in bandas:
                        print("Banda encontrada: {}".format(banda))
                        data = xr.open_dataset(caminho_arquivo)
                        dst = dataset.variables[banda]
                        dt = data[banda]
                        reverso = dt.sel(lat=slice(None, None, -1))
                        dst[:] = reverso
                        print("Banda {} rotacionada com sucesso!".format(banda))

                        dataset.close()
                        arquivo_destino = '/opt/geoos/data/import/{}'.format(arquivo)
                        shutil.move(caminho_arquivo, arquivo_destino)
                        print('Arquivo {} movido para {}'.format(arquivo, arquivo_destino))

    #primeira função a ser declarada, entrada no docker e criação do arquivo contendo as bandas de interesse
    def processo_gerar_arquivos_com_nomes():
            print("Primeira função iniciada, declarando variáveis e listando id_docker, entrando no container e executando comandos")
            host_directory = '/opt/geoos/data/UFPR/NORTE/tmp/'
            formatted_dates_dict = achar_hora()

            output1 = subprocess.check_output(['docker', 'ps', '-a']).decode('utf-8')
            lines = output1.split('\n')

            id_docker = None
            for line in lines:
                if "guilewasser/pglang:latest" in line:
                    id_docker = line.split()[0]
                    break

            if id_docker:
                print("ID do contêiner Docker:", id_docker)
            else:
                print("Nenhum contêiner Docker correspondente encontrado.")
                return  # Encerra a função se o contêiner não for encontrado

            client = docker.from_env()
            container = client.containers.get(id_docker)

            nome2 = "AMPA1"
            nome3 = "temperatura"
            command = 'gdalwarp -t_srs EPSG:4326 NETCDF:"/home/data/UFPR/NORTE/WaterProperties_2_Surface.nc":temperature /home/data/UFPR/NORTE/{}_{}.nc'.format(nome2,nome3)
            first_task = container.exec_run(command)
            first_task_output = first_task.output.decode('utf-8')
            first_task_exit_code = first_task.exit_code

            print("Saída da primeira tarefa:")
            print(first_task_output)

            if first_task_exit_code == 0:
                print("A primeira tarefa foi concluída com sucesso.")
            else:
                print("A primeira tarefa falhou. Código de saída:", first_task_exit_code)

            bandas = 25  
            print("Entrando no Looping")

            time.sleep(0.01)

            for banda in range(1, bandas+1):
                data_variada_formatada = formatted_dates_dict[f"data{banda:02}"]
                nome = "{}_{}_{}".format(nome2,nome3, data_variada_formatada)
                banda_nome = 'Band{}'.format(banda)
                command2 = 'gdalwarp -t_srs EPSG:4326 NETCDF:"/home/data/UFPR/NORTE/{}_{}.nc":{} /home/data/UFPR/NORTE/tmp/{}.nc'.format(nome2,nome3, banda_nome, nome)
                nc_file_path = '/home/data/UFPR/NORTE/tmp/{}.nc'.format(nome)
                print("Este é o arquivo",nc_file_path)
                exec_01 = container.exec_run(command2)
                time.sleep(0.01)
                saida01_exec_01 = exec_01.output.decode('utf-8')
                saida_exec_01 = exec_01.exit_code
                print("Executando permissões")
                exec_02 = 'chmod 777 {}'.format(nc_file_path)
                time.sleep(0.01)
                print("Executando permissões")
                exec_03 = container.exec_run(exec_02)
                saida01_exec_03 = exec_03.output.decode('utf-8')
                saida_exec_03 = exec_03.exit_code
                time.sleep(0.01)
                print("terminando as permissões")
                if banda == 25:
                    encontrar_nomes_bandas(host_directory)
                    break

            subprocess.run(['docker', 'exec', '-it', id_docker, 'bash', '-c', 'exit'])
            time.sleep(0.01)

    processo_gerar_arquivos_com_nomes()  

temperatura()



