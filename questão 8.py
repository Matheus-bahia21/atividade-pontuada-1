# limpar o terminal
import os 
os.system("clear || cls ")

cd = (input(""" 
verde
azul                    
amarelo
vermelho 
            
digite a cor de um cd da sua escolha :"""))

match cd: 
    case "verde" |"VERDE" :
        print("valor: - R$10,00 .")
    case "azul" |"AZUL" :
        print("valor: - R$20,00 .")  
    case "amarelo" |"AMARELO" :
        print("valor: - R$30,00 .")      
    case "vermelho" |"VERMELHO" :
        print("valor: - R$40,00 .")        
    case _:
        print("opção invalida  ")    