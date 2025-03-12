# limpar o terminal
import os 
os.system("clear || cls ")

nome_do_luno = input ("digite o nome do aluno : ")
primeira_nota = float(input("digite a priemira nota do aluno : "))
segunda_nota =float(input("digite a segunda nota do aluno : "))
reultado = float


media = (primeira_nota + segunda_nota) / 2 

if media >= 6:
    print ("\nexibindo resultado ... ")
    print (f"media {media}")
    print ("aprovado !")

elif media >= 4:
    print ("\nexibindo resultado ... ")
    print (f"media {media}")
    print ("recuperação !")
else:
     print ("\nexibindo resultado ... ")
     print (f"media {media}")
     print ("reprovado !")    