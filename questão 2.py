# limpar o terminal
import os 
os.system("clear || cls ")


Nome = str(input("digite seu nome "))
sexo = str(input("digite seu sexo : "))
estado_civil = str(input("digite seu estado civil : "))



match estado_civil:
     case "solteiro" | "solteira " :
      print("\nExibindo dados .....")    
      print (f"nome : {Nome}") 
      print (f"sexo : {sexo}") 
      print (f"estado civil : {estado_civil}") 
     case "casado" | "casada" :
         tempo_de_casado = input("digite o seu tempo de casado em anos ")
         print("\nExibindo dados .....")    
         print (f"nome : {Nome}") 
         print (f"sexo : {sexo}") 
         print (f"estado_civil : {estado_civil}")  
         print (f"tempo de casado: {tempo_de_casado}") 
     case _: 
      ("opção invalida !") 