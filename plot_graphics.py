import matplotlib.pyplot as plt
import numpy as np

def plota_grafico(result_selection, result_insertion, result_bubble, result_shell, result_bucket):
    plt.title('Gráfico de desempenho')
    plt.ylabel('Tempo')
    plt.xlabel('Iteração')
    plt.plot(result_selection, color='pink')
    plt.plot(result_insertion, color='blue')
    plt.plot(result_bubble, color='red')
    plt.plot(result_shell, color='green')
    plt.plot(result_bucket, color='yellow')

    plt.show()
