import sys
print("->>[̲̅J̲̅.̲̅L̲̅υ̲̅c̲̅α̲̅s̲̅™̲̅]<<-\n")
determinador=float(input("Digite o x da f(x): "))
pontos=int(input("Numero de pontos: "))
if pontos<=0:
  print("Numero inválido!")
  sys.exit(1)
vet=[]
for i in range(pontos):
    vet1=[]
    x=float(input("x"+str(i)+":" ))
    y=float(input("y"+str(i)+":" ))
    vet1.append(x)
    vet1.append(y)
    vet.append(vet1)
matriz=[]
for i in range(pontos): #fazendo a matriz
    vet1=[]
    for j in range(pontos+1):
        if (j!=pontos):
            vet1.append((vet[i][0])**(pontos-1-j))
        else:
            vet1.append(vet[i][1])
    matriz.append(vet1)

#aplicar gauss
n=pontos
resultado=[0]*n
for i in range(n-1):#n-1 porque ta comparando de duas em duas listas/ zerando a linha abaixo da diag principal
    pivo=matriz[i][i]
    if pivo==0:
        matriz.append(matriz[i])
        del(matriz[i])#mudança de linha joga a linha do pivo para ultima linha
        pivo=matriz[i][i]
    for j in range(i+1,n):
        coeficiente=matriz[j][i]/pivo
        for k in range(n+1):
            matriz[j][k]=matriz[j][k]-coeficiente*matriz[i][k]
    for i in matriz:
        for j in i:
            print(j,end=" | ")
        print()
    print("\n\n")        
termos_ind2=[]
for i in range(n):
    termos_ind2.append(matriz[i][n])
    del(matriz[i][n])
resultado[n-1]=termos_ind2[n-1]/matriz[n-1][n-1]
for i in range(n-1,-1,-1):
    soma=0
    for j in range(1+i,n):
        soma+=matriz[i][j]*resultado[j]
    if matriz[i][i]==0:
        print("Sistema incompatível")
        sys.exit(0)
    else:
        resultado[i]=(termos_ind2[i]-soma)/matriz[i][i]
print("\n")
print("Vetor solução:")
k=1;
somador=0
for i in resultado:
    somador+=((determinador)**(pontos-k))*i
    k+=1
    print("|"+str("%f"%i)+"|")
w="" #escrever a f(x) na tela depois continuar*
k=1
for i in range(pontos):
  if resultado[i]<0:
    w=w[:-1]
    w+=("%f*(%f)**(%d)+"%(resultado[i],determinador,pontos-k))
  else:
    w+=("%f*(%f)**(%d)+"%(resultado[i],determinador,pontos-k))
  k+=1
w=w[:-1]#exclui o ultimo sinal de "+"
print("\nf(%f) = %s"%(determinador,w))
print("\nf(%f) = %f"%(determinador,somador))
