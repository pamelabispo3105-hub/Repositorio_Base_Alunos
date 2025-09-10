# 02 Atividade Nova
# 2 Agenda de Contatos
# Implemente um programa que crie e gerencie um arquivo chamado contatos.txt.
Cada contato deve ter nome, telefone e e-mail.
O programa deve:
Permitir cadastrar novos contatos.
Exibir todos os contatos cadastrados.
OBS: Neste caso só iremos usar o os comandos de With , open e os modos de leitura
e escrita da função open()

def cadastrar_contato ():
   nome = input ("Digite o nome :")
   telefone = input ("Digite o telefone :")
   email = input ("Digite o e-mail:")

   # Gravando mo arquivo
   while open ('Contatos.txt", "a") as arquivo:
          arquivo.write(f"{nome},{telefone} , {email}\n")
    print ("Contato cadatrado com sucesaso!\n")


def listar_contatos():
    try:
       while open ("Contatos.txt","r")
       as arquivo:
       contatos =
arquivo.readlines()
              if len (*contatos) == 0:
                 print ("=== Lista de contatos ===")
                 for contato in
contatos:
                 nome, telefone,
email = contato.strip(). split (",")
                 print(f"nome)
{nome} | Telefone: {telefone} | Email: {email}")
                 print ()
        execpt FileNotFoundError:
            print("Ainda não há contatos cadastrados.\n")

# Menu principal
while True:
    print("1 - Cadrastrar novo contato")
    print("2 - Listar contatos")
    print("0 - Sair")
    opcao = input ("Escolha uma opção:")

    if opcao == "1":
       cadrastrar_contato()
    elif opcao == "2":
       Listar_contatos()
    elif opcao == "0":
       print ("Saindo...")
       break
else:
    print("Opcao inválida!\n")