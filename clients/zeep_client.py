import zeep
import os

# URL do WSDL (descrição do serviço SOAP)
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# Inicializando o cliente Zeep
client = zeep.Client(wsdl=wsdl_url)

# Chamada ao método CapitalCity com o código do país 'NZ' (Nova Zelândia)
result = client.service.CapitalCity(sCountryISOCode='NZ')

# Exibindo a resposta
print(f"A capital da Nova Zelândia é: {result}")
