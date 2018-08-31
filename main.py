import random
import time
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from shell_sort import shell_sort
from bucket_sort import bucket_sort
from plot_graphics import plota_grafico

def execute():
    print("Escolha um contexto para trabalhar: ")
    print("(1) - Analisar desempenho individual")
    print("(2) - Analisar comparativo de desempenho")
    print("(0) - Sair")

    option = input()

    if option == '0':
        return
    else:
        menu_inicial[option]()

def analisar_individualmente():
    print("Escolha um algoritmo para executar no vetor aleatório: ")
    print("(1) - Analisar Selection Sort")
    print("(2) - Analisar Insertion Sort")
    print("(3) - Analisar Bubble Sort")
    print("(4) - Analisar Shell sort")
    print("(5) - Analisar Bucket Sort")
    print("(0) - Sair")

    option = input()

    limit = 1000

    array = cria_elementos(limit, limit**2)

    if option == '0':
        return
    else:
        result = menu[option](array)
        print(result)

def analisar_contexto():
    print("Gerando relatório de dados...")

    lista_selection = []
    lista_insertion = []
    lista_bubble = []
    lista_shell = []
    lista_bucket = []

    i = 0

    limit = 1000

    while i < 50:

        array = cria_elementos(limit, limit**2)

        inicio = time.time()
        menu['1'](array)
        fim = time.time()

        lista_selection.append(fim - inicio)

        inicio = time.time()
        menu['2'](array)
        fim = time.time()

        lista_insertion.append(fim - inicio)

        inicio = time.time()
        menu['3'](array)
        fim = time.time()

        lista_bubble.append(fim - inicio)

        inicio = time.time()
        menu['4'](array)
        fim = time.time()

        lista_shell.append(fim - inicio)

        inicio = time.time()
        menu['5'](array)
        fim = time.time()

        lista_bucket.append(fim - inicio)

        i += 1

    plota_grafico(lista_selection, lista_insertion, lista_bubble, lista_shell, lista_bucket)

def cria_elementos(quantidade, limite):
    array = random.sample(range(limite), quantidade)
    return array

def imprime_lista(array):
    print(array)

menu_inicial = {
    '1': analisar_individualmente,
    '2': analisar_contexto
}

menu = {
    '1': selection_sort,
    '2': insertion_sort,
    '3': bubble_sort,
    '4': shell_sort,
    '5': bucket_sort
}

execute()
