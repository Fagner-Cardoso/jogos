# cabeçalho
print("********************************")
print("*     Jogo da adivinhação      *")
print("********************************")


# definição variável número secreto e quantidade de tentativas 
rodada = 1
total_de_tentativas = 3
numero_secreto = 10


# inicio do loop for
for rodada in range(1, total_de_tentativas + 1):
 
  print("Rodada {} de {} tentativas" .format(rodada, total_de_tentativas))

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
    break
  elif(maior):
    print("Você errou! O seu chute foi maior que o número secreto.\n")
  elif(menor):
    print("Você errou! O seu chute foi menor que o número secreto.\n")


#fim do loop

# texto final
print("Fim de jogo.") 

