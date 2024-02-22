import requests
import time
import schedule
import psycopg2 as db
import subprocess
from ftplib import FTP
import os
import json


def get_data():
    url = 'https://rt.ambientweather.net/v1/devices?apiKey=7712e7e6c7464bee8add6bbc83d493d1b999ed19c684474d8f2f9316325225fd&applicationKey=8ecae3ed4c4e407d80535d2dee6ac671a7502d92bd9b4b57b4dde2e6a303719f&lastData=true'
    data = requests.get(url).json()

    LOCG01 = data[2]
    LOCG02 = data[0]

    data_LOCG01 = LOCG01.get('lastData')
    data_LOCG02 = LOCG02.get('lastData')

    dateutc_LOCG01 = data_LOCG01.get('dateutc')
    tempinf_LOCG01 = data_LOCG01.get('tempinf')
    humidityin_LOCG01 = data_LOCG01.get('humidityin')
    baromrelin_LOCG01 = data_LOCG01.get('baromrelin')
    baromabsin_LOCG01 = data_LOCG01.get('baromabsin')
    tempf_LOCG01 = data_LOCG01.get('tempf')
    battout_LOCG01 = data_LOCG01.get('battout')
    humidity_LOCG01 = data_LOCG01.get('humidity')
    winddir_LOCG01 = data_LOCG01.get('winddir')
    windspeedmph_LOCG01 = data_LOCG01.get('windspeedmph')
    windgustmph_LOCG01 = data_LOCG01.get('windgustmph')
    maxdailygust_LOCG01 = data_LOCG01.get('humidity')
    hourlyrainin_LOCG01 = data_LOCG01.get('hourlyrainin')
    eventrainin_LOCG01 = data_LOCG01.get('eventrainin')
    dailyrainin_LOCG01 = data_LOCG01.get('dailyrainin')
    weeklyrainin_LOCG01 = data_LOCG01.get('weeklyrainin')
    monthlyrainin_LOCG01 = data_LOCG01.get('monthlyrainin')
    totalrainin_LOCG01 = data_LOCG01.get('totalrainin')
    solarradiation_LOCG01 = data_LOCG01.get('solarradiation')
    uv_LOCG01 = data_LOCG01.get('uv')
    batt_co2_LOCG01 = data_LOCG01.get('batt_co2')
    feelsLike_LOCG01 = data_LOCG01.get('feelsLike')
    dewPoint_LOCG01 = data_LOCG01.get('dewPoint')
    feelsLikein_LOCG01 = data_LOCG01.get('feelsLikein')
    dewPointin_LOCG01 = data_LOCG02.get('dewPointin')
    lastRain_LOCG01 = data_LOCG01.get('lastRain')
    tz_LOCG01 = data_LOCG01.get('tz')
    date_LOCG01 = data_LOCG01.get('date')

    temperatura_LOCG01 = (((tempf_LOCG01) - 32)*(5/9))
    feelsLike_LOCG01_ = (((feelsLike_LOCG01) - 32)*(5/9))

    dateutc_LOCG02 = data_LOCG02.get('dateutc')
    tempinf_LOCG02 = data_LOCG02.get('tempinf')
    humidityin_LOCG02 = data_LOCG02.get('humidityin')
    baromrelin_LOCG02 = data_LOCG02.get('baromrelin')
    baromabsin_LOCG02 = data_LOCG02.get('baromabsin')
    tempf_LOCG02 = data_LOCG02.get('tempf')
    battout_LOCG02 = data_LOCG02.get('battout')
    humidity_LOCG02 = data_LOCG02.get('humidity')
    winddir_LOCG02 = data_LOCG02.get('winddir')
    windspeedmph_LOCG02 = data_LOCG02.get('windspeedmph')
    windgustmph_LOCG02 = data_LOCG02.get('windgustmph')
    maxdailygust_LOCG02 = data_LOCG02.get('humidity')
    hourlyrainin_LOCG02 = data_LOCG02.get('hourlyrainin')
    eventrainin_LOCG02 = data_LOCG02.get('eventrainin')
    dailyrainin_LOCG02 = data_LOCG02.get('dailyrainin')
    weeklyrainin_LOCG02 = data_LOCG02.get('weeklyrainin')
    monthlyrainin_LOCG02 = data_LOCG02.get('monthlyrainin')
    totalrainin_LOCG02 = data_LOCG02.get('totalrainin')
    solarradiation_LOCG02 = data_LOCG02.get('solarradiation')
    uv_LOCG02 = data_LOCG02.get('uv')
    batt_co2_LOCG02 = data_LOCG02.get('batt_co2')
    feelsLike_LOCG02 = data_LOCG02.get('feelsLike')
    dewPoint_LOCG02 = data_LOCG02.get('dewPoint')
    feelsLikein_LOCG02 = data_LOCG02.get('feelsLikein')
    dewPointin_LOCG02 = data_LOCG02.get('dewPointin')
    lastRain_LOCG02 = data_LOCG02.get('lastRain')
    tz_LOCG02 = data_LOCG02.get('tz')
    date_LOCG02 = data_LOCG02.get('date')

    temperatura_LOCG02 = (((tempf_LOCG02) - 32)*(5/9))
    feelsLike_LOCG02_ = (((feelsLike_LOCG02) - 32)*(5/9))

    data_base_device_LOCG01 = (dateutc_LOCG01,
                        tempinf_LOCG01,
                        humidityin_LOCG01,
                        baromrelin_LOCG01,
                        baromabsin_LOCG01,
                        temperatura_LOCG01,
                        battout_LOCG01,
                        humidity_LOCG01,
                        winddir_LOCG01,
                        windspeedmph_LOCG01,
                        windgustmph_LOCG01,
                        maxdailygust_LOCG01,
                        hourlyrainin_LOCG01,
                        eventrainin_LOCG01,
                        dailyrainin_LOCG01,
                        weeklyrainin_LOCG01,
                        monthlyrainin_LOCG01,
                        totalrainin_LOCG01,
                        solarradiation_LOCG01,
                        uv_LOCG01,
                        batt_co2_LOCG01,
                        feelsLike_LOCG01_,
                        dewPoint_LOCG01,
                        feelsLikein_LOCG01,
                        dewPointin_LOCG01,
                        lastRain_LOCG01,
                        tz_LOCG01,
                        date_LOCG01)

    data_base_device_LOCG02 = (dateutc_LOCG02,
                        tempinf_LOCG02,
                        humidityin_LOCG02,
                        baromrelin_LOCG02,
                        baromabsin_LOCG02,
                        temperatura_LOCG02,
                        battout_LOCG02,
                        humidity_LOCG02,
                        winddir_LOCG02,
                        windspeedmph_LOCG02,
                        windgustmph_LOCG02,
                        maxdailygust_LOCG02,
                        hourlyrainin_LOCG02,
                        eventrainin_LOCG02,
                        dailyrainin_LOCG02,
                        weeklyrainin_LOCG02,
                        monthlyrainin_LOCG02,
                        totalrainin_LOCG02,
                        solarradiation_LOCG02,
                        uv_LOCG02,
                        batt_co2_LOCG02,
                        feelsLike_LOCG02_,
                        dewPoint_LOCG02,
                        feelsLikein_LOCG02,
                        dewPointin_LOCG02,
                        lastRain_LOCG02,
                        tz_LOCG02,
                        date_LOCG02)
    
    return data_base_device_LOCG01, data_base_device_LOCG02

def programa():
    url = 'https://rt.ambientweather.net/v1/devices?apiKey=7712e7e6c7464bee8add6bbc83d493d1b999ed19c684474d8f2f9316325225fd&applicationKey=8ecae3ed4c4e407d80535d2dee6ac671a7502d92bd9b4b57b4dde2e6a303719f&lastData=true'
    data = requests.get(url).json()

    LOCG01 = data[2]
    LOCG02 = data[0]

    data_LOCG01 = LOCG01.get('lastData')
    data_LOCG02 = LOCG02.get('lastData')

    dateutc_LOCG01 = data_LOCG01.get('dateutc')
    tempinf_LOCG01 = data_LOCG01.get('tempinf')
    humidityin_LOCG01 = data_LOCG01.get('humidityin')
    baromrelin_LOCG01 = data_LOCG01.get('baromrelin')
    baromabsin_LOCG01 = data_LOCG01.get('baromabsin')
    tempf_LOCG01 = data_LOCG01.get('tempf')
    battout_LOCG01 = data_LOCG01.get('battout')
    humidity_LOCG01 = data_LOCG01.get('humidity')
    winddir_LOCG01 = data_LOCG01.get('winddir')
    windspeedmph_LOCG01 = data_LOCG01.get('windspeedmph')
    windgustmph_LOCG01 = data_LOCG01.get('windgustmph')
    maxdailygust_LOCG01 = data_LOCG01.get('humidity')
    hourlyrainin_LOCG01 = data_LOCG01.get('hourlyrainin')
    eventrainin_LOCG01 = data_LOCG01.get('eventrainin')
    dailyrainin_LOCG01 = data_LOCG01.get('dailyrainin')
    weeklyrainin_LOCG01 = data_LOCG01.get('weeklyrainin')
    monthlyrainin_LOCG01 = data_LOCG01.get('monthlyrainin')
    totalrainin_LOCG01 = data_LOCG01.get('totalrainin')
    solarradiation_LOCG01 = data_LOCG01.get('solarradiation')
    uv_LOCG01 = data_LOCG01.get('uv')
    batt_co2_LOCG01 = data_LOCG01.get('batt_co2')
    feelsLike_LOCG01 = data_LOCG01.get('feelsLike')
    dewPoint_LOCG01 = data_LOCG01.get('dewPoint')
    feelsLikein_LOCG01 = data_LOCG01.get('feelsLikein')
    dewPointin_LOCG01 = data_LOCG02.get('dewPointin')
    lastRain_LOCG01 = data_LOCG01.get('lastRain')
    tz_LOCG01 = data_LOCG01.get('tz')
    date_LOCG01 = data_LOCG01.get('date')

    temperatura_LOCG01 = (((tempf_LOCG01) - 32)*(5/9))
    feelsLike_LOCG01_ = (((feelsLike_LOCG01) - 32)*(5/9))

    dateutc_LOCG02 = data_LOCG02.get('dateutc')
    tempinf_LOCG02 = data_LOCG02.get('tempinf')
    humidityin_LOCG02 = data_LOCG02.get('humidityin')
    baromrelin_LOCG02 = data_LOCG02.get('baromrelin')
    baromabsin_LOCG02 = data_LOCG02.get('baromabsin')
    tempf_LOCG02 = data_LOCG02.get('tempf')
    battout_LOCG02 = data_LOCG02.get('battout')
    humidity_LOCG02 = data_LOCG02.get('humidity')
    winddir_LOCG02 = data_LOCG02.get('winddir')
    windspeedmph_LOCG02 = data_LOCG02.get('windspeedmph')
    windgustmph_LOCG02 = data_LOCG02.get('windgustmph')
    maxdailygust_LOCG02 = data_LOCG02.get('humidity')
    hourlyrainin_LOCG02 = data_LOCG02.get('hourlyrainin')
    eventrainin_LOCG02 = data_LOCG02.get('eventrainin')
    dailyrainin_LOCG02 = data_LOCG02.get('dailyrainin')
    weeklyrainin_LOCG02 = data_LOCG02.get('weeklyrainin')
    monthlyrainin_LOCG02 = data_LOCG02.get('monthlyrainin')
    totalrainin_LOCG02 = data_LOCG02.get('totalrainin')
    solarradiation_LOCG02 = data_LOCG02.get('solarradiation')
    uv_LOCG02 = data_LOCG02.get('uv')
    batt_co2_LOCG02 = data_LOCG02.get('batt_co2')
    feelsLike_LOCG02 = data_LOCG02.get('feelsLike')
    dewPoint_LOCG02 = data_LOCG02.get('dewPoint')
    feelsLikein_LOCG02 = data_LOCG02.get('feelsLikein')
    dewPointin_LOCG02 = data_LOCG02.get('dewPointin')
    lastRain_LOCG02 = data_LOCG02.get('lastRain')
    tz_LOCG02 = data_LOCG02.get('tz')
    date_LOCG02 = data_LOCG02.get('date')

    temperatura_LOCG02 = (((tempf_LOCG02) - 32)*(5/9))
    feelsLike_LOCG02_ = (((feelsLike_LOCG02) - 32)*(5/9))

    data_base_device_LOCG01 = (dateutc_LOCG01,
                        tempinf_LOCG01,
                        humidityin_LOCG01,
                        baromrelin_LOCG01,
                        baromabsin_LOCG01,
                        temperatura_LOCG01,
                        battout_LOCG01,
                        humidity_LOCG01,
                        winddir_LOCG01,
                        windspeedmph_LOCG01,
                        windgustmph_LOCG01,
                        maxdailygust_LOCG01,
                        hourlyrainin_LOCG01,
                        eventrainin_LOCG01,
                        dailyrainin_LOCG01,
                        weeklyrainin_LOCG01,
                        monthlyrainin_LOCG01,
                        totalrainin_LOCG01,
                        solarradiation_LOCG01,
                        uv_LOCG01,
                        batt_co2_LOCG01,
                        feelsLike_LOCG01_,
                        dewPoint_LOCG01,
                        feelsLikein_LOCG01,
                        dewPointin_LOCG01,
                        lastRain_LOCG01,
                        tz_LOCG01,
                        date_LOCG01)

    data_base_device_LOCG02 = (dateutc_LOCG02,
                        tempinf_LOCG02,
                        humidityin_LOCG02,
                        baromrelin_LOCG02,
                        baromabsin_LOCG02,
                        temperatura_LOCG02,
                        battout_LOCG02,
                        humidity_LOCG02,
                        winddir_LOCG02,
                        windspeedmph_LOCG02,
                        windgustmph_LOCG02,
                        maxdailygust_LOCG02,
                        hourlyrainin_LOCG02,
                        eventrainin_LOCG02,
                        dailyrainin_LOCG02,
                        weeklyrainin_LOCG02,
                        monthlyrainin_LOCG02,
                        totalrainin_LOCG02,
                        solarradiation_LOCG02,
                        uv_LOCG02,
                        batt_co2_LOCG02,
                        feelsLike_LOCG02_,
                        dewPoint_LOCG02,
                        feelsLikein_LOCG02,
                        dewPointin_LOCG02,
                        lastRain_LOCG02,
                        tz_LOCG02,
                        date_LOCG02)


    inserir_dados_no_SQL_LOCG01 =  """INSERT INTO database_matinhos (
                                        data_utc,
                                        temperatura_interna,
                                        umidade_interna,
                                        pressao_relativa_hg,
                                        pressao_absoluta_hg,
                                        temperatura,
                                        bateria_externa_OK_1_Baixo_0,
                                        umidade_externa,
                                        direcao_vento,
                                        velocidade_vento,
                                        velocidade_max_vento_em_10min,
                                        velocidade_max_vento_no_ultimo_dia,
                                        taxa_chuva_por_hora,
                                        evento_chuva,
                                        chuva_diaria,
                                        chuva_semanal,
                                        chuva_mensal,
                                        chuva_total,
                                        radiacao_solar_watts_p_m2,
                                        ultravioleta,
                                        bateria_de_co2_1_ok_0_Baixo,
                                        sensacao_termica,
                                        ponto_orvalho,
                                        sensacao_termica_in,
                                        ponto_orvalho_interno,
                                        ultima_chuva_por_hora,
                                        fuso_horario,
                                        data_legivel
                                        )
                                        
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    inserir_dados_no_SQL_LOCG02 = """INSERT INTO database_antonina (
                                        data_utc,
                                        temperatura_interna,
                                        umidade_interna,
                                        pressao_relativa_hg,
                                        pressao_absoluta_hg,
                                        temperatura,
                                        bateria_externa_OK_1_Baixo_0,
                                        umidade_externa,
                                        direcao_vento,
                                        velocidade_vento,
                                        velocidade_max_vento_em_10min,
                                        velocidade_max_vento_no_ultimo_dia,
                                        taxa_chuva_por_hora,
                                        evento_chuva,
                                        chuva_diaria,
                                        chuva_semanal,
                                        chuva_mensal,
                                        chuva_total,
                                        radiacao_solar_watts_p_m2,
                                        ultravioleta,
                                        bateria_de_co2_1_ok_0_Baixo,
                                        sensacao_termica,
                                        ponto_orvalho,
                                        sensacao_termica_in,
                                        ponto_orvalho_interno,
                                        ultima_chuva_por_hora,
                                        fuso_horario,
                                        data_legivel
                                        ) 
                                    
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    # Inserir dados no banco de dados
    connect_to = db.connect(host='localhost',
                                database='dados',
                                user='postgres',
                                password='585957@#',
                                port='5432'
                                )   

    cursor = connect_to.cursor()
    cursor.execute(inserir_dados_no_SQL_LOCG02, data_base_device_LOCG02)
    cursor.execute(inserir_dados_no_SQL_LOCG01, data_base_device_LOCG01)
    connect_to.commit()
    print("DADOS ARMAZENADOS COM SUCESSO")

    # Fazendo o dump do banco de dados
    dump_file_name = "backup_" + time.strftime("%Y%m%d%H%M%S") + ".dump"  # Adicionando um nome dinâmico com base na data/hora para o arquivo de dump

    # Define a senha através da variável de ambiente
    os.environ['PGPASSWORD'] = '585957@#'

    # Comando corrigido
    dump_command = f"pg_dump -h localhost -p 5432 -U postgres -F c -b -v -f {dump_file_name} dados"

    try:
        subprocess.run(dump_command, shell=True, check=True)
        print("Backup realizado com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao fazer o backup!")
        exit()

    # Limpando a variável de ambiente após o uso
    os.environ['PGPASSWORD'] = ''

    # Enviando o dump para FTP (use seus detalhes do servidor FTP)
    ftp_server = "200.17.232.3"
    ftp_username = "G_Souza"
    ftp_password = "Gavet@2000"
    remote_directory = "/Temp/Est_Meteo"

    ftp = FTP(ftp_server)
    ftp.login(user=ftp_username, passwd=ftp_password)
    ftp.cwd(remote_directory)

    with open(dump_file_name, 'rb') as f:
        ftp.storbinary('STOR ' + dump_file_name, f)

    ftp.quit()
    os.remove(dump_file_name)  # Remover arquivo de dump após o envio 

# 1. Capture o retorno da função get_data()
data_base_device_LOCG01, data_base_device_LOCG02 = get_data()

def create_geojson_file():
    global data_base_device_LOCG01, data_base_device_LOCG02
    data = {
        "type": "FeatureCollection",
        "name": "estac",
        "crs": { 
            "type": "name", 
            "properties": { 
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84" 
            } 
        },
        "features": [ 
            {
                "type": "Feature",
                "properties": {
                    "data_utc": data_base_device_LOCG01[0],
                    "temperatura_interna": data_base_device_LOCG01[1],
                    "umidade_interna": data_base_device_LOCG01[2],
                    "pressao_relativa_hg": data_base_device_LOCG01[3],
                    "pressao_absoluta_hg": data_base_device_LOCG01[4],
                    "temperatura": data_base_device_LOCG01[5],
                    "bateria_externa_OK_1_Baixo_0": data_base_device_LOCG01[6],
                    "umidade_externa": data_base_device_LOCG01[7],
                    "direcao_vento": data_base_device_LOCG01[8],
                    "velocidade_vento": data_base_device_LOCG01[9],
                    "velocidade_max_vento_em_10min": data_base_device_LOCG01[10],
                    "velocidade_max_vento_no_ultimo_dia": data_base_device_LOCG01[11],
                    "taxa_chuva_por_hora": data_base_device_LOCG01[12],
                    "evento_chuva": data_base_device_LOCG01[13],
                    "chuva_diaria": data_base_device_LOCG01[14],
                    "chuva_mensal": data_base_device_LOCG01[16],
                    "chuva_total": data_base_device_LOCG01[17],
                    "radiacao_solar_watts_p_m2": data_base_device_LOCG01[18],
                    "ultravioleta": data_base_device_LOCG01[19],
                    "bateria_de_co2_1_ok_0_Baixo": data_base_device_LOCG01[20],
                    "sensacao_termica": data_base_device_LOCG01[21],
                    "ponto_orvalho": data_base_device_LOCG01[22],
                    "sensacao_termica_in": data_base_device_LOCG01[23],
                    "ponto_orvalho_interno": data_base_device_LOCG01[24],
                    "ultima_chuva_por_hora": data_base_device_LOCG01[25],
                    "fuso_horario": data_base_device_LOCG01[26],
                    "data_legivel": data_base_device_LOCG01[27]
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [-25.6723, -48.5111]
                }
            },
            {
                "type": "Feature",
                "properties": {
                    "data_utc": data_base_device_LOCG02[0],
                    "temperatura_interna": data_base_device_LOCG02[1],
                    "umidade_interna": data_base_device_LOCG02[2],
                    "pressao_relativa_hg": data_base_device_LOCG02[3],
                    "pressao_absoluta_hg": data_base_device_LOCG02[4],
                    "temperatura": data_base_device_LOCG02[5],
                    "bateria_externa_OK_1_Baixo_0": data_base_device_LOCG02[6],
                    "umidade_externa": data_base_device_LOCG02[7],
                    "direcao_vento": data_base_device_LOCG02[8],
                    "velocidade_vento": data_base_device_LOCG02[9],
                    "velocidade_max_vento_em_10min": data_base_device_LOCG02[10],
                    "velocidade_max_vento_no_ultimo_dia": data_base_device_LOCG02[11],
                    "taxa_chuva_por_hora": data_base_device_LOCG02[12],
                    "evento_chuva": data_base_device_LOCG02[13],
                    "chuva_diaria": data_base_device_LOCG02[14],
                    "chuva_mensal": data_base_device_LOCG02[16],
                    "chuva_total": data_base_device_LOCG02[17],
                    "radiacao_solar_watts_p_m2": data_base_device_LOCG02[18],
                    "ultravioleta": data_base_device_LOCG02[19],
                    "bateria_de_co2_1_ok_0_Baixo": data_base_device_LOCG02[20],
                    "sensacao_termica": data_base_device_LOCG02[21],
                    "ponto_orvalho": data_base_device_LOCG02[22],
                    "sensacao_termica_in": data_base_device_LOCG02[23],
                    "ponto_orvalho_interno": data_base_device_LOCG02[24],
                    "ultima_chuva_por_hora": data_base_device_LOCG02[25],
                    "fuso_horario": data_base_device_LOCG02[26],
                    "data_legivel": data_base_device_LOCG02[27]
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [-26.6723, -49.5111]
                }
            }
        ]
    }

    file_path = '/home/guile/teste2/estac.geojson'
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

get_data()
time.sleep(2)
print|("DEU BOA")
programa()
time.sleep(2)
print|("DEU BOA")
create_geojson_file()
