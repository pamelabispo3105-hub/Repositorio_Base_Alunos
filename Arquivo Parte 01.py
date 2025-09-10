# Exercício Parte 01.PythonFinalizationError

#lista inicial
nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial", nomes)

#Adicionando elementos 
nomes.append ("Carlos")# Adiciona ao final 
print ("Após append:", nomes )

nomes. insert(1, "Fernanda") # Insere "Fernanda" na posição 1
print ("Após insert:",nomes)

# Modificando elementos 
nomes [2] - "Paulo" #Modifica o elementos no índice 2
print ("Após modificação:", nomes)

#Removendo elementos 
del nomes [3] #Remove o elementos no índice 3 
print("após remove:", nomes)

nomes.remove ("Maria") #Remove a primeira de "Maria"
print ("Após remove:", nomes)

removido = nomes.pop(2) #Remove e retorna o elemento no índice 2
print(f"Após pop (removido  {removido}  nomes")
      
nomes =[1,24,5,] 
#Escazia a lista 
print('Após clear:", nomes')
