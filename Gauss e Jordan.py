import sys
print("->>[̲̅J̲̅.̲̅L̲̅υ̲̅c̲̅α̲̅s̲̅™̲̅]<<-\n")
print("----Bem Vindo---\n")
a=int(input("Resolver o sistema linear Digite 1-Gauss ou 2-Jordan: "))
matriz=[]
termos_ind=[]
n=int(input("Digite a ordem do sistema: "))
resultado=[0]*n
for i in range(n):
    vet=[]
    for j in range(n):
        vet.append(float(input("digite o coeficiente da icógnita "+str(i+1)+str(j+1)+": ")))
    matriz.append(vet)
for i in range(n):
    termos_ind.append(float(input("digite o "+str(i+1)+"º valor do vetor dos termos independentes: ")))
for i in range(n):
    matriz[i].append(termos_ind[i])
if a==1:
    for i in range(n-1):#n-1 porque ta comparando de duas em duas listas/ zerando a linha abaixo da diag principal
        pivo=matriz[i][i]
        if pivo==0:
            print("Pivo não pode ser zero!")
            sys.exit(0)
        else:
            for j in range(i+1,n):
                coeficiente=matriz[j][i]/pivo
                for k in range(n+1):
                    matriz[j][k]=matriz[j][k]-coeficiente*matriz[i][k]
        for i in matriz:
            for j in i:
                print(j,end=" | ")#matriz com duas casas decimais arredondadas
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
    for i in resultado:
        print("|"+str("%f"%i)+"|")
elif a==2:
    for i in range(n-1):#zerando a linha abaixo da dig principal
        pivo=matriz[i][i]
        if pivo==0:
            print("Pivo não pode ser zero!")
            sys.exit(0)
        else:
            for j in range(i+1,n):
                coeficiente=matriz[j][i]/pivo
                for k in range(n+1):
                    matriz[j][k]=matriz[j][k]-coeficiente*matriz[i][k]
        for i in matriz:
            for j in i:
                print("%f"%j,end=" | ")
            print("\n")
        print("\n")

    for i in range(n-1,0,-1): #zerando a linha acima da diag principal
        pivo=matriz[i][i]
        if pivo==0:
            print("Pivo não pode ser zero!")
            sys.exit(0)
        else:
            for j in range(i-1,-1,-1):
                coeficiente=matriz[j][i]/pivo
                for k in range(n+1):
                    matriz[j][k]=matriz[j][k]-coeficiente*matriz[i][k]
                for t in matriz:
                    for u in t:
                        print("%f"%u,end=" | ")
                    print("\n")
                print("\n\n")
    print("\n")
    print("Vetor solução:")
    for i in range(n):
        print("|"+str("%f"%(matriz[i][n]/matriz[i][i]))+"|")
