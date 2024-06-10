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

if(venceu):
 print("Parabéns! Você acertou.\n")
else:
 print("Que pena! Você errou.\n")


print("Número secreto:", numero_secreto)

# texto final
print("Fim de jogo.") 

