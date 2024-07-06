#Um professor quer escolher um aluno aleatorio da turma para realizar uma tarefa
#usar a biblioteca  randon
import random
a = input('Digite algo para a lista')
b = input('Digite algo para a lista')
c = input('Digite algo para a lista')
d = input('Digite algo para a lista')
lista = [a,b,c,d]
escolha = random.choice(lista)
print (f'O escolhido foi {escolha} ')
#------------------------------
#mais "avançado" com a esolha de quantos alunos tem na sala

x = int(input('Quantos alunos tem na sala de aula?\n'))
lista = []
for i in range (x):
    nome = input('Digite um nome: ')
    lista.append(nome)
print (lista)
escolha = random.choice(lista)
print(f'O aluno escolhido foi {escolha}')
#------------------------------
# outros randons
import random
escolha = random.randrange(16)
print (escolha)
#------------------------------
import random
lista = ['a','b','c','d']
lista1=lista.copy() #copia uma lista e adiciona ela em uma nova variavel
random.shuffle(lista1) #embaralha os itens de uma lista
print(f'Lista original é {lista}')
print (f'lista embaralhada {lista1}')
# -----------------------------
import random
x = random.random() #imprime um numero aleatorio entre 0 e 1, 0 <= x <1
print (x)
# email laerte: laerte.takeuti@professores.ibmec.edu.br