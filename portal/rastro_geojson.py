import netCDF4 as nc
import geojson
import sys
import os
import re
from datetime import datetime, timedelta

def geojsonfazer(fpath):
    # Abra o arquivo NetCDF
    nc_dataset = nc.Dataset(fpath)

    # Leitura das variáveis
    lons = nc_dataset.variables['longitude'][:]
    lats = nc_dataset.variables['latitude'][:]
    thickness = nc_dataset.variables['Thickness'][:]

    # Criação dos pontos GeoJSON
    features = []
    for lon, lat, thick in zip(lons, lats, thickness):
        point = geojson.Point((lon, lat))
        feature = geojson.Feature(geometry=point, properties={'Thickness': thick})
        features.append(feature)

    # Criação do objeto FeatureCollection GeoJSON
    feature_collection = geojson.FeatureCollection(features)

    # Use expressões regulares para extrair a string de data e hora do nome do arquivo
    match = re.search(r'Spill_(\d{4})_?\s*(\d{1,2})_?\s*(\d{1,2})_?\s*(\d{1,2})_?\s*(\d{1,2})\s*.*?\.nc', os.path.basename(fpath))
    if match:
        data_hora_str = '{}_{}_{}_{}_{}'.format(*match.groups())
        
        # Tenta converter a string de data e hora para um objeto datetime
        try:
            data_hora = datetime.strptime(data_hora_str, '%Y_%m_%d_%H_%M')
            # Adiciona 3 horas à data e hora extraídas
            data_hora_ajustada = data_hora + timedelta(hours=3)
            # Ajusta os minutos para serem zero
            data_hora_ajustada = data_hora_ajustada.replace(minute=0, second=0)
            # Formata a data e hora ajustadas para o nome do arquivo
            data_hora_str_ajustada = data_hora_ajustada.strftime('%Y-%m-%d_%H-%M')

        except ValueError as e:
            print(f'Erro ao processar a data e hora do arquivo {fpath}: {e}, utilizando data e hora original para nome do arquivo.')
            data_hora_str_ajustada = data_hora_str

        nome_arquivo_saida = f'modelo_modelo_{data_hora_str_ajustada}.geojson'
        
        # Determinar o caminho de saída com base no nome do arquivo de entrada
        dpath = f'/home/data/import/{nome_arquivo_saida}'
        os.makedirs(os.path.dirname(dpath), exist_ok=True)

        # Salvar em um arquivo
        with open(dpath, 'w') as f:
            geojson.dump(feature_collection, f)

        print(f'Processo finalizado para {fpath}')
    else:
        print(f'Erro: O nome do arquivo {fpath} não segue o padrão esperado e não será processado.')

def processar_todos_arquivos_spill(diretorio):
    # Lista todos os arquivos no diretório especificado
    for arquivo in os.listdir(diretorio):
        # Checa se o arquivo começa com 'Spill_'
        if arquivo.startswith('Spill_'):
            caminho_completo = os.path.join(diretorio, arquivo)
            geojsonfazer(caminho_completo)

# Diretório onde os arquivos .nc estão armazenados
diretorio_nc = '/usr/src/app/Oil_Spill_Tool/res/Run1/'
# Chamando a função para processar todos os arquivos
processar_todos_arquivos_spill(diretorio_nc)
