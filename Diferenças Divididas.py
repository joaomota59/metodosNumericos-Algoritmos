import sys
print("->>[̲̅J̲̅.̲̅L̲̅υ̲̅c̲̅α̲̅s̲̅™̲̅]<<-\n")
pontos=int(input("Numero de pontos: "))
determinador=float(input("Digite o x da P"+str(pontos-1)+"(x): "))
casas=int(input("Numero de casas decimais: "))
if pontos<=0:
  print("Numero inválido!")
  sys.exit(1)
vet=[]#contém todos os pontos
vet_final=[] # contem os deltas (as diferenças)
k=[] # guarda todos os xi iniciais
k1=[]# guarda todos os yi iniciais
for i in range(pontos):
    vet1=[]
    vet1.append(float(input("x"+str(i)+":" )))
    vet1.append(float(input("y"+str(i)+":" )))
    vet.append(vet1)
    k.append(vet1[0])#contem os valores de x
    k1.append(vet1[1]) #contem os valores de y
vet_final.append(k1)
cont=0
while cont!=pontos-1: #ultima etapa de diferenças // menos dois pq cont começa do zero
  vet1=[]
  if cont==0: #primeira diferença dividida da tabela
    for i in range(pontos-1):# tanto de diferenças do inicio
          vet1.append((vet[i+1][1]-vet[i][1])/(k[i+1]-k[i]))
    vet_final.append(vet1)
  else:
    for i in range(len(vet_final[cont])-1):
      vet1.append((vet_final[cont][i+1]-vet_final[cont][i])/(k[cont+i+1]-k[i])) #cont+1 no caso em baixo seria a diferença
    vet_final.append(vet1)
  cont+=1
matrix=[]
for i in range(len(vet_final)):
	aux=[]
	for j in range(len(vet_final[i])):
		aux.append(vet_final[j][i])
	matrix.append(aux)
# fazer esse append no final como um extend
cont=0
print("\tTabela das diferenças divididas\n")
for i in matrix:
    print(round(k[cont],casas),end=" ")
    for j in range(len(i)):
        print(round(i[j],casas),end=" ")
    cont+=1
    print()
k=""
for i in range(pontos):
  if i==0:
    print("P(x) = yo",end=" ")
  else:
    k+=("(x-x%d)"%(i-1))
    print("+",k+str(("Δ%dyo"%(i-1))),end=" ")
print()
