import netCDF4 as nc
import geojson

def geojsonfazer():
    # Abra o arquivo NetCDF
    nc_dataset = nc.Dataset('/home/data/UFPR/spill/P-53_2019_ 4_ 2_ 0_ 0_ 0.00000000.nc')  # Alterado de nc para nc_dataset

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

    # Salvar em um arquivo
    with open('/home/data/import/spill_oleo.geojson', 'w') as f:
        geojson.dump(feature_collection, f)

    print('Processo finalizado')

geojsonfazer()
