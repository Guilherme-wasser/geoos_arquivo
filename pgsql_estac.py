import requests
import time
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
    LOCG03 = data[3]

    data_LOCG01 = LOCG01.get('lastData')
    data_LOCG02 = LOCG02.get('lastData')
    data_LOCG03 = LOCG03.get('lastData')

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
    
    dateutc_LOCG03 = data_LOCG03.get('dateutc')
    tempinf_LOCG03 = data_LOCG03.get('tempinf')
    humidityin_LOCG03 = data_LOCG03.get('humidityin')
    baromrelin_LOCG03 = data_LOCG03.get('baromrelin')
    baromabsin_LOCG03 = data_LOCG03.get('baromabsin')
    tempf_LOCG03 = data_LOCG03.get('tempf')
    battout_LOCG03 = data_LOCG03.get('battout')
    humidity_LOCG03 = data_LOCG03.get('humidity')
    winddir_LOCG03 = data_LOCG03.get('winddir')
    windspeedmph_LOCG03 = data_LOCG03.get('windspeedmph')
    windgustmph_LOCG03 = data_LOCG03.get('windgustmph')
    maxdailygust_LOCG03 = data_LOCG03.get('humidity')
    hourlyrainin_LOCG03 = data_LOCG03.get('hourlyrainin')
    eventrainin_LOCG03 = data_LOCG03.get('eventrainin')
    dailyrainin_LOCG03 = data_LOCG03.get('dailyrainin')
    weeklyrainin_LOCG03 = data_LOCG03.get('weeklyrainin')
    monthlyrainin_LOCG03 = data_LOCG03.get('monthlyrainin')
    totalrainin_LOCG03 = data_LOCG03.get('totalrainin')
    solarradiation_LOCG03 = data_LOCG03.get('solarradiation')
    uv_LOCG03 = data_LOCG03.get('uv')
    batt_co2_LOCG03 = data_LOCG03.get('batt_co2')
    feelsLike_LOCG03 = data_LOCG03.get('feelsLike')
    dewPoint_LOCG03 = data_LOCG03.get('dewPoint')
    feelsLikein_LOCG03 = data_LOCG03.get('feelsLikein')
    dewPointin_LOCG03 = data_LOCG03.get('dewPointin')
    lastRain_LOCG03 = data_LOCG03.get('lastRain')
    tz_LOCG03 = data_LOCG03.get('tz')
    date_LOCG03 = data_LOCG03.get('date')

    temperatura_LOCG03 = (((tempf_LOCG03) - 32)*(5/9))
    feelsLike_LOCG03_ = (((feelsLike_LOCG03) - 32)*(5/9))

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

    data_base_device_LOCG03 = (dateutc_LOCG03,
                        tempinf_LOCG03,
                        humidityin_LOCG03,
                        baromrelin_LOCG03,
                        baromabsin_LOCG03,
                        temperatura_LOCG03,
                        battout_LOCG03,
                        humidity_LOCG03,
                        winddir_LOCG03,
                        windspeedmph_LOCG03,
                        windgustmph_LOCG03,
                        maxdailygust_LOCG03,
                        hourlyrainin_LOCG03,
                        eventrainin_LOCG03,
                        dailyrainin_LOCG03,
                        weeklyrainin_LOCG03,
                        monthlyrainin_LOCG03,
                        totalrainin_LOCG03,
                        solarradiation_LOCG03,
                        uv_LOCG03,
                        batt_co2_LOCG03,
                        feelsLike_LOCG03_,
                        dewPoint_LOCG03,
                        feelsLikein_LOCG03,
                        dewPointin_LOCG03,
                        lastRain_LOCG03,
                        tz_LOCG03,
                        date_LOCG03)    

    return data_base_device_LOCG01, data_base_device_LOCG02,data_base_device_LOCG03

def programa():              

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

    inserir_dados_no_SQL_LOCG03 = """INSERT INTO database_guaraquecaba (
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
    cursor.execute(inserir_dados_no_SQL_LOCG03, data_base_device_LOCG03)
    connect_to.commit()
    print("DADOS ARMAZENADOS COM SUCESSO")
 

# 1. Capture o retorno da função get_data()
data_base_device_LOCG01, data_base_device_LOCG02,data_base_device_LOCG03 = get_data()

get_data()
time.sleep(2)
print|("DEU BOA")
programa()
time.sleep(2)
