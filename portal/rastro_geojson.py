import netCDF4 as nc
import geojson
import sys
import os

def geojsonfazer(fpath='/home/data/cabral/P-53_2019_ 4_ 2_ 0_ 0_ 0.00000000.nc'):
    # Abra o arquivo NetCDF
    nc_dataset = nc.Dataset(fpath)  # Alterado de nc para nc_dataset

    # Leitura das variáveis
    lons = nc_dataset.variables['longitude'][:]  # Coordenadas de longitude
    lats = nc_dataset.variables['latitude'][:]   # Coordenadas de latitude
    thickness = nc_dataset.variables['Thickness'][:]

    # Criação dos pontos GeoJSON
    features = []
    for lon, lat, thick in zip(lons, lats, thickness):
        point = geojson.Point((lon, lat))
        feature = geojson.Feature(geometry=point, properties={'Thickness': thick})
        features.append(feature)

    # Criação do objeto FeatureCollection GeoJSON
    feature_collection = geojson.FeatureCollection(features)

    dpath = '/home/data/import/modelo_modelo.geojson'
    os.makedirs(os.path.dirname(dpath), exist_ok=True)

    # Salvar em um arquivo
    with open(dpath, 'w') as f:
        geojson.dump(feature_collection, f)

    print('Processo finalizado')


geojsonfazer(sys.argv[1])
