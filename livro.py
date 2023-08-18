from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://www.livrariacultura.com.br/livros"
url2 = "https://www.livrariavanguarda.com.br/categorias/livros"

driver.get(url)
html1 = driver.page_source

driver.get(url2)
html2 = driver.page_source

driver.quit()

soup1 = BeautifulSoup(html1, "html.parser")
soup2 = BeautifulSoup(html2, "html.parser")

def livros1():
    livros = soup1.find_all('li', class_="livros slick-slide slick-cloned")
    lista_livros = []
    for livro in livros:
        nome = livro.find('h2', class_='prateleiraProduto__informacao__nome').get_text().strip()
        valor = livro.find('span', class_='prateleiraProduto__informacao__preco--valor').get_text().strip()
        lista_livros.append((nome, valor))
        # print(nome, valor)
    return lista_livros

def livros2():
    livros = soup2.find_all('div', class_='product-item mb-0 mb-md-4')
    lista_livros = []
    for livro in livros:
        nome = livro.find('a', class_='product-item__link-title').get_text().strip()
        valor = livro.find('ins', class_='product-price__current-price').get_text().strip()
        lista_livros.append((nome, valor))
        # print(nome, valor)
    return lista_livros

def buscarLivro():
    livro = input("Qual livro você deseja? ")
    
    lista_livros = livros1() + livros2()
    
    livros_encontrados = []
    
    for nome, valor in lista_livros:
        if livro.lower() in nome.lower():
            livros_encontrados.append((nome, valor))
    
    if livros_encontrados:
        for nome, valor in livros_encontrados:
            print(f"Livro: {nome} | Valor: {valor}")
    else:
        print("Livro não existe no catálogo principal da livraria")
def buscarPorPreco():
    valor_maximo = float(input("Buscar livros com o preço até: "))

    lista_livros = livros1() + livros2()

    livros_abaixo_do_valor = []
    for nome, valor in lista_livros:
        preco = float(valor.replace("R$", "").replace(",", "."))
        if preco <= valor_maximo:
            livros_abaixo_do_valor.append((nome, valor))

    if len(livros_abaixo_do_valor) == 0:
        print("Nenhum livro encontrado abaixo do valor máximo.")
    else:
        print(f"Livros abaixo do valor máximo de R$ {valor_maximo:.2f}:")
        for nome, valor in livros_abaixo_do_valor:
            print(f"Livro: {nome} | Valor: {valor}")

def totalizarLivros():
    lista_livros1 = livros1()
    lista_livros2 = livros2()
    
    total_livros1 = len(lista_livros1)
    total_livros2 = len(lista_livros2)
    
    total_livros = total_livros1 + total_livros2
    total_valor = 0
    
    for _, valor in lista_livros1 + lista_livros2:
        total_valor += float(valor.replace("R$", "").replace(",", "."))
    
    print(f"Total de livros na Livraria Cultura: {total_livros1}")
    print(f"Total de livros na Livraria Vanguarda: {total_livros2}")
    print(f"Total de livros: {total_livros}")
    print(f"Total de valores: R$ {total_valor:.2f}")


def compararLivros():
    livro1 = input("Digite o nome do primeiro livro: ")
    livro2 = input("Digite o nome do segundo livro: ")
    
    lista_livros = livros1() + livros2()
    
    for nome, valor in lista_livros:
        if livro1.lower() in nome.lower():
            preco_livro1 = float(valor.replace("R$", "").replace(",", "."))
        if livro2.lower() in nome.lower():
            preco_livro2 = float(valor.replace("R$", "").replace(",", "."))
    
    diferenca = preco_livro1 - preco_livro2
    print(f"Primeiro livro: '{livro1}' | Valor: R$ {preco_livro1:.2f}")
    print(f"Segundo livro: '{livro2}' | Valor: R$ {preco_livro2:.2f}")
    print(f"Diferença de preço entre '{livro1}' e '{livro2}' é de: R$ {diferenca:.2f}")

def dicionario():
    livros1 = soup1.find_all('li', class_="livros slick-slide slick-cloned")
    livros2 = soup2.find_all('div', class_='product-item mb-0 mb-md-4')
    
    lista_livros = {}
    
    for livro in livros1:
        nome = livro.find('h2', class_='prateleiraProduto__informacao__nome').get_text().strip()
        valor = livro.find('span', class_='prateleiraProduto__informacao__preco--valor').get_text().strip()
        lista_livros[nome] = valor
    
    for livro in livros2:
        nome = livro.find('a', class_='product-item__link-title').get_text().strip()
        valor = livro.find('ins', class_='product-price__current-price').get_text().strip()
        lista_livros[nome] = valor
    
    for nome, valor in lista_livros.items():
        print(f"Livro: {nome} | Valor: {valor}")

while True:
    print('-'*43)
    print("1. Livros da Livraria Cultura")
    print("2. Livros da Livraria Vanguarda")
    print("3. Buscar Livro Especifico")
    print("4. Buscar Livros Por Preço")
    print("5. Total de Livros")
    print("6. Comparar Preço Do Livro")
    print("7. Mostrar Livros Em Formato De Dicionario")
    print("8. SAIR")
    print('-'*43)
    opcao = int(input("Opção: "))
    print('#'*43)

    if opcao == 1:
        lista_livros = livros1()
        for nome, valor in lista_livros:
            print(f"Livro: {nome} | Valor: {valor}")
    elif opcao == 2:
        lista_livros = livros2()
        for nome, valor in lista_livros:
            print(f"Livro: {nome} | Valor: {valor}")
    elif opcao == 3:
        buscarLivro()
    elif opcao == 4:
        buscarPorPreco()
    elif opcao == 5:
        totalizarLivros()
    elif opcao == 6:
        compararLivros()
    elif opcao == 7:
        dicionario()
    else:
        break