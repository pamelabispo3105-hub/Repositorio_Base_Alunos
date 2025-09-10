# Atividade While Lição 3
# input esta errado no caso precisa dos paresenteses 
# o break eu só uso quando quero parar a execuçao do codigo
# EXPLICAÇAO DO CODIGO: WHILE TORNA O CODIGO UM LOOP OUS EJA FICA SE REPETINDO ATÉ QUE ELE VEJA A PALAVRA BREAK, depois eu capturo a nota da pessoa usando o input e guardo dentro da variavel nota e faço a validaçao se a nota foir menor que 0 ou maior que 10 eu peço para o usuario diigtar de novo
# tem maneiras mais simples de fazer se precisar me chama
while True:
    nota = float (input("Digite uma "))
    
    if 0 <= nota >= 10:
     print (f"Voce digitou uma nota válida: {nota}")
     break
    else:
     print ("Valor inválido1 Tente novamente.")
     nota=input('digite de novo')
