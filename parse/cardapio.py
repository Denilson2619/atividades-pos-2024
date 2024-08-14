from xml.dom.minidom import parse

# Caminho para o arquivo de teste
file_path = "C:/Users/patom/OneDrive/Desktop/Repositório/atividades-pos-2024/parse/cardapio.xml"

try:
    dom = parse(file_path)
except Exception as e:
    print(f"Erro ao carregar o XML: {e}")
    exit()

cardapio = dom.documentElement
pratos_cardapio = cardapio.getElementsByTagName("prato")

for prato in pratos_cardapio:
    prato_id_cardapio = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f"Prato {prato_id_cardapio}: {nome}")

try:
    prato_id = int(input("DIGITE O ID DO PRATO/CARDAPIO: ")) - 1  # Ajuste para índice zero baseado
    prato = pratos_cardapio[prato_id]
except (ValueError, IndexError):
    print("ID do prato inválido.")
    exit()

Descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
ingredientes = prato.getElementsByTagName("ingrediente")
ingredientes = [ingrediente.firstChild.nodeValue for ingrediente in ingredientes]
preco_do_prato = prato.getElementsByTagName("preco")[0].firstChild.nodeValue
calorias_do_prato = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue

print(f"Nome do Prato: {nome}")
print(f"Descrição do Prato: {Descricao}")
print(f"Ingredientes:")
print(f"\n".join(ingredientes))
print(f"Preço do Prato: R${preco_do_prato}")
print(f"Calorias do Prato: {calorias_do_prato} Kilocaloria")
print(f"Tempo de Preparo: {tempoPreparo}")
