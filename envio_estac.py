import json
import requests
import time

def get_data():
    url = 'https://rt.ambientweather.net/v1/devices?apiKey=7712e7e6c7464bee8add6bbc83d493d1b999ed19c684474d8f2f9316325225fd&applicationKey=8ecae3ed4c4e407d80535d2dee6ac671a7502d92bd9b4b57b4dde2e6a303719f&lastData=true'
    
    data = requests.get(url).json()

    time.sleep(1)
    
    LOCG01 = data[2]
    LOCG02 = data[0]
    LOCG03 = data[3]

    data_LOCG01 = LOCG01.get('lastData')
    data_LOCG02 = LOCG02.get('lastData')
    data_LOCG03 = LOCG03.get('lastData')

    global data_base_device_LOCG01,data_base_device_LOCG02,data_base_device_LOCG03

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

    return data_base_device_LOCG01,data_base_device_LOCG02,data_base_device_LOCG03

def format_file_path(date_string):
    # Extrai a data e hora da string
    data, hora = date_string.split('T')
    ano, mes, dia = map(int, data.split('-'))
    horas, minutos, segundos = map(int, hora.split('.')[0].split(':'))  # Converte horas, minutos e segundos para inteiros

    if horas >= 24:  # Caso ultrapasse 24 horas, ajusta o dia
        horas -= 24
        dia += 1

    # Verificando e ajustando os meses que têm 31 dias
    if mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31:
        dia = 1
        mes += 1

    # Verificando e ajustando os meses que têm 30 dias
    elif mes in [4, 6, 9, 11] and dia > 30:
        dia = 1
        mes += 1

    # Verificando e ajustando fevereiro levando em consideração os anos bissextos
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  # Ano bissexto
            if dia > 29:
                dia = 1
                mes += 1
        else:
            if dia > 28:
                dia = 1
                mes += 1

    # Se o mês ultrapassa 12, ajusta o ano
    if mes > 12:
        mes = 1
        ano += 1

    # Arredonda minutos para o múltiplo de 5 mais próximo
    minutos = round(minutos / 5) * 5
    if minutos == 60:  # Caso tenha arredondado para 60, ajusta a hora
        minutos = 0
        horas += 1

    global path_formatado
    # Formata a string final
    path_formatado = f"/opt/geoos/data/import/estac_estacoes_{ano}-{mes:02}-{dia:02}_{horas:02}-{minutos:02}.geojson"
    print(path_formatado)
    return path_formatado

# 1. Capture o retorno da função get_data()
data_base_device_LOCG01, data_base_device_LOCG02, data_base_device_LOCG03 = get_data()

def create_geojson_file():
    global data_base_device_LOCG01, data_base_device_LOCG02, data_base_device_LOCG03
    global path_formatado
    
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
                    "nome_estacao": "LOCG01",
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
                "coordinates": [-48.5419, -25.8175]
            }
        },
        {
            "type": "Feature",
            "properties": {
                    "nome_estacao": "LOCG02",
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
                "coordinates": [-48.7066523, -25.4362559]
            }
        }, 
        {
            "type": "Feature",
            "properties": {
                    "nome_estacao": "LOCG03",
                    "data_utc": data_base_device_LOCG03[0],
                    "temperatura_interna": data_base_device_LOCG03[1],
                    "umidade_interna": data_base_device_LOCG03[2],
                    "pressao_relativa_hg": data_base_device_LOCG03[3],
                    "pressao_absoluta_hg": data_base_device_LOCG03[4],
                    "temperatura": data_base_device_LOCG03[5],
                    "bateria_externa_OK_1_Baixo_0": data_base_device_LOCG03[6],
                    "umidade_externa": data_base_device_LOCG03[7],
                    "direcao_vento": data_base_device_LOCG03[8],
                    "velocidade_vento": data_base_device_LOCG03[9],
                    "velocidade_max_vento_em_10min": data_base_device_LOCG03[10],
                    "velocidade_max_vento_no_ultimo_dia": data_base_device_LOCG03[11],
                    "taxa_chuva_por_hora": data_base_device_LOCG03[12],
                    "evento_chuva": data_base_device_LOCG03[13],
                    "chuva_diaria": data_base_device_LOCG03[14],
                    "chuva_mensal": data_base_device_LOCG03[16],
                    "chuva_total": data_base_device_LOCG03[17],
                    "radiacao_solar_watts_p_m2": data_base_device_LOCG03[18],
                    "ultravioleta": data_base_device_LOCG03[19],
                    "bateria_de_co2_1_ok_0_Baixo": data_base_device_LOCG03[20],
                    "sensacao_termica": data_base_device_LOCG03[21],
                    "ponto_orvalho": data_base_device_LOCG03[22],
                    "sensacao_termica_in": data_base_device_LOCG03[23],
                    "ponto_orvalho_interno": data_base_device_LOCG03[24],
                    "ultima_chuva_por_hora": data_base_device_LOCG03[25],
                    "fuso_horario": data_base_device_LOCG03[26],
                    "data_legivel": data_base_device_LOCG03[27]
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-48.3304722, -25.2989478]
            }
        }        
    ]
}

    file_pasta = path_formatado

    # Escrevendo o dicionário 'data' no arquivo
    with open(file_pasta, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    get_data()
    time.sleep(2)
    file_path = format_file_path(data_base_device_LOCG01[27])
    time.sleep(2)
    create_geojson_file()
    print("RODOU!")

main()
