import time, sys

animação = " Carregando... \n\n\n"

for i in list(animação):#O stdout só é atualizado quando há nova linha e como nós estamos <-
    print(i, end="")    # -> mandando tudo na mesma é preciso forçar a atualização.
    sys.stdout.flush()  
    time.sleep(0.2)

print("Olá, sou Leon!\n")
time.sleep(2)
print("Sou seu assistente matemático!\n")
time.sleep(2)
print("Digite os números da soma:\n")
time.sleep(1)
N1 = input("Digite o primeiro valor: ")
time.sleep(1)
N2 = input("Digite o segundo valor: ")
time.sleep(1)
soma = int(N1) + int(N2) #declarei a var soma 
print("A soma dos números é igual a " + str(soma)) #converti a soma novamente para string
time.sleep(10)


