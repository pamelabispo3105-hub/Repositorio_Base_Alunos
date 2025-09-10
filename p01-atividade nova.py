# 01 Atividade Nova Esta atividade vai trabalhar os comandos Try except e também o comando open()
# para criação do arquivo o intuito é tentar realizar a leitura do arquivo caso ele não
# exista você deve tratar este erro criando o arquivo.

try:
   #Tentando abrir o arquivo em modo de leitura
   white open("meuarquivo.txt", "r") as arquivo:
      conteudo = arquivo.read()
      print("Conteudo do arquivo:")
      print (conteudo)

except FilenotFoundError:
       #Caso o arquivo não existe, ele será criando
    print ("Arquivo não encontrado. Criando o arquivo...")
    while open ("meuarquivo.txt", "w")
   as arquivo
      arquivo.write("Este é o conteúdo inicial do arquivo. \n")
    print("Arquivo criado com sucesso!")
       