import os
from colorama import Fore,Style,Back
from time import sleep
"""
    bibliotecas utilizadas:
    colorama - usado pra colorir o codigo |link da documentação: https://pypi.org/project/colorama/
    os - usado pra limpar o terminal outras funções |link da documentação https://docs.python.org/pt-br/3/library/os.html 
    time - usado pra criar funções de tempo 
"""
i = ""
while i != "N":
    try:
        print(Fore.MAGENTA+'=============calculadora em python============='+Fore.RESET)
        ex = input(Fore.GREEN+ 'digite a expressão: '+Fore.RESET)
        sleep(1)
        print('===============================================')
        print(f'{ex} = {eval(ex)}')
        print('===============================================')
        sleep(1)
        i = input(Fore.GREEN + 'deseja continuar? [S/N]: '+ Fore.RESET).upper()
    except:
        sleep(1)
        os.system('cls')
        print(Fore.RED+ 'ops,parece que voce digitou uma expressão invalida'+Fore.RESET)
        i = input(Fore.GREEN + 'deseja continuar? [S/N]: '+ Fore.RESET).upper()
        sleep(1)
os.system('cls')
print(Fore.GREEN+"programa finalizado."+Fore.RESET)
    