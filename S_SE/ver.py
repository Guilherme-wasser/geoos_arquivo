import xarray as xr

# Caminho para o arquivo NetCDF
file_path = '/opt/geoos/data/UFPR/S_SE/tmp/SUDESTE15_altura_2024-02-26_03-00.nc'

# Usando xarray para abrir o arquivo NetCDF
ds = xr.open_dataset(file_path)
ds1 = ds.variables
# Imprimir informações sobre o arquivo
print(ds)

print(ds1)

# Se você quiser acessar uma variável específica, você pode fazer isso da seguinte maneira:
# variavel = ds['nome_da_variavel']

# Por exemplo, para acessar a temperatura (substitua 'temperatura' pelo nome correto da variável):
# temperatura = ds['temperatura']

# Lembre-se de fechar o arquivo NetCDF quando terminar
ds.close()