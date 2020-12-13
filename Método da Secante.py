from math import log,exp,sin,cos
print("->>[̲̅J̲̅.̲̅L̲̅υ̲̅c̲̅α̲̅s̲̅™̲̅]<<-\n")
tolerancia=float(input("Digite a tolerância: "))
a=float(input("Digite o limite inferior: "))
b=float(input("Digite o limite superior: "))
interacoes=int(input("O método possue quantidade predefinida de interações? 1-Sim 2-Nao:"))
if interacoes==1:
    interacoes=int(input("Quantas interacoes? "))
else:
    interacoes=-1
print("\n"*5)

#####################Função###############################
def f(x):
    global k #usando uma variavel global na função
    return eval(k) #eval tranforma uma string em uma expressao
##########################################################    


if a>b:
    print("Não há raízes neste intervalo!")
else:
    print("Observações quando for digitar a função:")
    print("Quando for elevar algum expoente, Digite---> base**('x'-número desejado)")
    print("EX: 2**(3) retorna 2 elevado a 3 que é 8!")
    print("Quando for usar o número de euler Digite---> exp('x'-número desejado)")
    print("EX: exp(5) retorna o número de euler elevado a 5")
    print("Quando for usar o seno Digite---> sin('x'-número desejado)")
    print("EX: sin(5) retorna o seno de 5")
    print("Quando for usar o cosseno Digite---> cos('x'-número desejado)")
    print("EX: cos(8) retorna o cosseno de 8")
    print("Quando for usar o log neperiano(ln) Digite---> log('x'-número desejado)")
    print("EX: log(9) retorna o log neperiano de 9")
    print("Quando for usar o log na base 10 Digite---> log('x'-número desejado,10)")
    print("EX: log(9,10) retorna o log de 9 na base 10")
    print("\n"*5)
    x0=float(input("Digite o x0: "))
    x1=float(input("Digite o x1: "))
    k=input("Digite a função: ")
    mat=[]
    cont=0
    while True:
        if cont==0:
            vet=[cont,a,b,x0,f(x0),"-"]
        elif cont==1:
            vet=[cont,a,b,x1,f(x1),"-"]
        else:
            x=mat[cont-1][3]-((mat[cont-2][3]-mat[cont-1][3])*f(mat[cont-1][3]))/(f(mat[cont-2][3])-f(mat[cont-1][3]))
            vet=[cont,"-","-",x,f(x),"-"]
        mat.append(vet)
        if cont>1 and abs(mat[cont][3]-mat[cont-1][3])<=tolerancia or interacoes==cont+1: break #or abs(f(x))<=tolerancia or abs(mat[cont][3]-mat[cont-1][3])/abs(mat[cont][3])
        cont+=1
    for i in range(len(mat)):
        if i>1:
            mat[i][5]=abs(mat[i][3]-mat[i-1][3])
    for i in mat:
        print(i)
    print("A raiz do intervalo dado é: ",x)
