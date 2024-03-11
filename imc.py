print ("Progama para calcular o imc.")
peso = int(input("Informe seu peso: "));
altura = float(input("Informe sua altura: "))
imc = peso / (altura**2)
print ("O seu Imc é ", imc)
if imc >= 25.1 and imc <= 30 :
    print ("Você está em sobrepeso")
elif imc >= 30.1 and imc <= 35 :
    print ("Você está em Obesidade tipo I")    
elif imc >= 35.1 and imc <= 39.9 :
    print ("Você está em Obesidade tipo II")
elif imc >= 40 :
    print ("Você está em Obesidade tipo III")
elif imc >= 22.1 and imc <= 25 :
    print ("Seu peso está normal")
elif imc >= 18.5 and imc<= 22 :
    print ("Está abaixo do peso")
elif imc >= 16.1 and imc <= 18.4 :
    print ("Você está em Desnutrição Moderada")
elif imc <16 :
    print ("Você está em Desnutrição Severa")
