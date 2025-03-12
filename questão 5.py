# limpar o terminal
import os 
os.system("clear || cls ")

a = float(input("digite o número a : "))
b = float(input("digite o número b : "))
resultado = float
operacao = (input(""" 
+ adição 
- - subitração 
* - multiplicação 
/ - divisão 
                                             
digite uma operação de sua escolha :"""))

match operacao :
    case "+" | "adição" :
        resultado = a + b
        print(f"o resultado da soma entre (a) e (b) é : {resultado}") 
    case "-" |"subtração":
        resultado = a - b 
        print(f"o resultado da subtração entre (a) e (b) é : {resultado}")   
    case "*" | "multiplicação":
        resultado = a * b
        print(f"o resultado da multiplicação entre (a) e (b) é : {resultado}") 
    case "/" | "divisão":
        resultado = a / b
        print(f"o resultado da divisão entre (a) e (b) é : {resultado}") 
    case _: 
        print ("operação invalida.") 

