import sys
print("->>[̲̅J̲̅.̲̅L̲̅υ̲̅c̲̅α̲̅s̲̅™̲̅]<<-\n")
pontos=int(input("Numero de pontos: "))
determinador=float(input("Digite o x da P"+str(pontos-1)+"(x): "))
if pontos<=0:
  print("Numero inválido!")
  sys.exit(1)
vet=[]#contém todos os pontos
vet_final=[]
for i in range(pontos):
    vet1=[]
    vet1.append(float(input("x"+str(i)+":" )))
    vet1.append(float(input("y"+str(i)+":" )))
    vet.append(vet1)
vet1=[]
#a intenção é criar uma matriz com 2 colunas x 'pontos' linhas depois divide uma linha pela outra somando..

#print só das variáveis
for i in range(pontos): #numerador
    k=("y%d"%i)
    for j in range(pontos):
        if j!=i:
            k+=("*(x-x%d)"%(j))
    vet1.append(k)
vet_final.append(vet1)
vet1=[]
for i in range(pontos): #denominador
    k=""
    for j in range(pontos):
        if j!=i:
            k+=("(x%d-x%d)*"%(i,j))
    k=k[:-1] #tira o ultimo sinal de multiplicação
    vet1.append(k)
vet_final.append(vet1)
print()

for j in range(pontos): #Printar
    print(vet_final[0][j])
    print("-"*len(max(vet_final[0][j],vet_final[1][j])),"+")
    print(vet_final[1][j])
    print()
print("\n\n")
vet1=[]
vet_final=[]


#print dos valores das variáveis
for i in range(pontos): #numerador
    k=""
    k=("%f"%vet[i][1])
    for j in range(pontos):
        if j!=i:
            k+=("*(%f-%f)"%(determinador,vet[j][0]))
    vet1.append(k)
vet_final.append(vet1)
vet1=[]

for i in range(pontos): #denominador
    k=""
    for j in range(pontos):
        if j!=i:
            k+=("(%f-%f)*"%(vet[i][0],vet[j][0]))
    k=k[:-1] #tira o ultimo sinal de multiplicação
    vet1.append(k)
vet_final.append(vet1)
somatorio=0
k=""
for j in range(pontos):
    print(vet_final[0][j])
    print("-"*len(max(vet_final[0][j],vet_final[1][j])),"+")
    print(vet_final[1][j])
    somatorio+=eval(vet_final[0][j])/eval(vet_final[1][j])
    if eval(vet_final[0][j])/eval(vet_final[1][j])>=0:
      k+=str(eval(vet_final[0][j])/eval(vet_final[1][j]))+str("+")
    else:
      k=k[:-1]
      k+=str(eval(vet_final[0][j])/eval(vet_final[1][j]))+str("+")
    print()
k=k[:-1]#tirar o ultimo sinal de soma
print("\n\n")
print("P%d(%f)= %s"%((pontos-1),determinador,k))
print("P%d(%f) = %f"%((pontos-1),determinador,somatorio))

