# cabeçalho
print("********************************")
print("*     Jogo da adivinhação      *")
print("********************************")


# definição variável número secreto 

numero_secreto = 10


# área de imput 

chute = int(input("Digite o número escolhido:\n"))
print("O número digitado foi:", chute)

# variáveis de estado do jogo

venceu = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

# condicional do jogo

if(venceu):
 print("Parabéns! Você acertou.\n")
elif(maior):
 print("Você errou! O seu chute foi maior que o número secreto.\n")
elif(menor):
 print("Você errou! O seu chute foi menor que o número secreto.\n")



# texto final
print("Fim de jogo.") 

