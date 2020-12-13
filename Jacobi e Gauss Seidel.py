print("----Bem Vindo---\n")
print("->>[̲̅J̲̅.̲̅L̲̅υ̲̅c̲̅α̲̅s̲̅™̲̅]<<-\n")
a=int(input("Resolver o sistema linear Digite 1-Jacobi ou 2-Gauss-Seidel: "))
if a!=1 and a!=2:
    while(a!=1 and a!=2):
        a=int(input("Resolver o sistema linear Digite 1-Jacobi ou 2-Gauss Seidel: "))
matriz=[]
matriz2=[]
termos_ind=[]
vet_aprox=[]
n=int(input("Digite a ordem do sistema: "))
tolerancia=float(input("Digite a tolerância:"))
interacoes=int(input("Digite o numero de interações:"))
while(interacoes<0):
    interacoes=int(input("Digite o numero de interações:"))
for i in range(n):
    vet_aprox.append(float(input("Digite o xo" +str(i+1)+" valor da aproximação inicial: ")))
print("\n")
matriz2.append(vet_aprox)
resultado=vet_aprox+["-"]
for i in range(n):
    vet=[]
    for j in range(n):
        vet.append(float(input("Digite o coeficiente da icógnita da "+str(i+1)+str(j+1)+": ")))
    matriz.append(vet)
for i in range(n):
    termos_ind.append(float(input("digite o "+str(i+1)+"º valor do vetor dos termos independentes: ")))

# Teste de Convergência
#critério das linhas
maximo=0
for i in range(n):
    soma=0
    for j in range(n):
        if i!=j:
            soma+=abs(matriz[i][j])
    soma=soma/abs(matriz[i][i])
    if maximo<soma:
        maximo=soma
if maximo<1:
    linhas= True
else:
    linhas= False

#critério das colunas
maximo=0
for j in range(n):
    soma=0
    for i in range(n):
        if i!=j:
            soma+=abs(matriz[i][j])
    soma=soma/abs(matriz[j][j])
    if maximo<soma:
        maximo=soma
if maximo<1:
    colunas= True
else:
    colunas= False

for i in range(n):
    matriz[i].append(termos_ind[i])

if a==1: #Solução Jacobi
    if colunas==True or linhas== True:
        cont=0
        print(resultado)
        while(1):
            cont+=1 #contador
            tolera=[]
            vet=[]
            for i in range(n):
                k=0
                for j in range(n):
                    if i!=j:
                        k=k+matriz[i][j]*vet_aprox[j]#aqui que muda! usar o novo valor
                k=1/matriz[i][i]*(matriz[i][j+1]-k)
                vet.append(k)
            for i in range(n):
                tolera.append(abs(vet[i]-vet_aprox[i]))
                vet_aprox[i]=vet[i]
            vet_aprox.append(max(tolera))
            print(vet_aprox)
            if vet_aprox[-1]<=tolerancia or cont==interacoes:
                break
            del vet_aprox[-1]
    else: print("Sistema não converge!")
else: #Solução de Gauss Seidel
    if colunas==True or linhas== True:
        cont=0
        print(resultado)
        while(1):
            cont+=1 #contador
            tolera=[]
            vet=[]
            for i in range(n):
                vet.append(vet_aprox[i])
            for i in range(n):
                k=0
                for j in range(n):
                    if i!=j:
                        k=k+matriz[i][j]*vet_aprox[j]
                k=1/matriz[i][i]*(matriz[i][j+1]-k)
                vet_aprox[i]=k #pegando os valores mais recentes
            for i in range(n):
                tolera.append(abs(vet[i]-vet_aprox[i]))
                vet[i]=vet_aprox[i]
            vet_aprox.append(max(tolera))
            print(vet_aprox)
            if vet_aprox[-1]<=tolerancia or cont==interacoes:
                break
            del vet_aprox[-1]
    else:
        print("Sistema não converge!")
