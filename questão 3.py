# limpar o terminal
import os 
os.system("clear || cls ")


A =  int(input("digite o primeiro número : "))
B =  int(input("digite o segundo número : "))
c = float

if A == B:
    C = A + B 
    print (f"(A) é igual a (B), e o resultado de (c), da soma é: {c}")
else : 
    c = A * B
    print (f" (A) não é igual a (B), e  o resultado de (c) da multiplicação é: {c}")