import requests
import xml.dom.minidom
import os

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# Caminho para o arquivo XML
base_dir = os.path.dirname(__file__)
xml_file_path = os.path.join(base_dir, "capital_city.xml")

# Lendo o conteúdo do arquivo XML
with open(xml_file_path, "r", encoding="utf-8") as file:
    payload = file.read()

# requisição
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
}

# Fazendo a requisição POST
response = requests.post(url, headers=headers, data=payload)

# Verificando se foi bem-sucedida
if response.status_code == 200:

    # Parse da resposta XML
    dom = xml.dom.minidom.parseString(response.text)
    
    # Encontrando a capital
    capital = dom.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
    
    # Exibindo o resultado
    print(f"A capital da Nova Zelândia é: {capital}")
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)
