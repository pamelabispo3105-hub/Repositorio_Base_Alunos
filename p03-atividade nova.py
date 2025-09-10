# 03 Atividade Nova
# 3 Crie um sistema que regista o nome e 3 notas do aluno depois você vai validar se a média
# do aluno é maior que 7 caso seja maior você deve registrar em um documento o nome dele
# e se ele está aprovado ou reprovado.O sistema deve estar em um loop e deve ser
# encerrado somente se o usuário digitar a opção 0

while True:
   print("\n=== Sistema de notas ===")
   nome = input("Digite o nome do aluno (ou '0'para sair):")
   
   if nome == "0":
     print ('Encerrando o sistema...")
     break

 try:
     nota1 = float(input(Digite a 1ª nota:"))
     nota2 = float(input("Digite a 2ª:"))
     nota3 = float(input("Digite a 3ª:"))
     
     media = (nota1 + nota2 + nota3)n / 3
     print(f"média do aluno {nome}:{media:.2f}")

     if mdeia >= 7:
       print("Situação: Aprovado")

    else:
       print("Situação:Reprovado")
    execpt ValueError:
       print("Erro: Digite apenas números válidos para as notas!")