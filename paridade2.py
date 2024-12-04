#challenge
#main() tem a responsabilidade de interação com o usr
def main():
   num = int(input("Diga a sua idade: "))
   if eh_par(num):
      print("Sua idade é par")
   else:
       print("Sua idade é ímpar")

#eh_par(num) tem a responsabilidade de verificar se um número é par
def eh_par (num):
   #PROCESSAMENTO: Verificar se o número informado é par
   return True if num % 2 == 0 else False 

main()