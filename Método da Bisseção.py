from math import exp as e,sin as sen, cos, log as ln, log10 as log
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
def f(x):
    global k #usando uma variavel global na função
    return eval(k) #eval tranforma uma string em uma expressao
if a>b:
    print("Não há raízes neste intervalo!")
else:
    print("Observações quando for digitar a função:")
    print("Quando for elevar algum expoente, Digite---> base**('x'-número desejado)")
    print("EX: 2**(3) retorna 2 elevado a 3 que é 8!")
    print("Quando for usar o número de euler Digite---> e('x'-número desejado)")
    print("EX: e(5) retorna o número de euler elevado a 5")
    print("Quando for usar o seno Digite---> sen('x'-número desejado)")
    print("EX: sen(5) retorna o seno de 5")
    print("Quando for usar o cosseno Digite---> cos('x'-número desejado)")
    print("EX: con(8) retorna o cosseno de 8")
    print("Quando for usar o log neperiano Digite---> ln('x'-número desejado)")
    print("EX: ln(9) retorna o log neperiano de 9")
    print("Quando for usar o log na base 10 Digite---> log('x'-número desejado)")
    print("EX: log(9) retorna o log na base 10 de 9")
    print("\n"*5)
    k=input("Digite a função: ")
    if f(a)*f(b)<0:#a e b sao intervalos
        x=(a+b)/2
        if f(x)==0:
            print("A raiz do intervalo dado é: ",x)
        else:
            mat=[] #usada para printar todo result na tela
            cont=0 #usado para saber a quant de interações
            ok=0 #usar na condição de parada
            while True:
                vet=[cont,a,b,x,f(x),"-"]
                temp=0
                if f(x)<0:
                    temp=a
                    a=x
                    if f(temp)>=0:
                        b=temp
                else:
                    temp=b
                    b=x
                    if f(temp)<0:
                        a=temp
                cont+=1
                mat.append(vet)
                if ok==1: break
                if interacoes==cont or abs(b-a)/2<=tolerancia: #o professor quer adotar somente a terceira condição e a segunda condição mas as outras duas sao corretas.  or abs((b-a)/x)<=tolerancia abs(f(x))<=tolerancia  or 
                    ok=1 #condição de parada
                x=(a+b)/2
            for i in range(len(mat)):
                if i!=0:
                    mat[i][5]=abs(mat[i][3]-mat[i-1][3])
            mat.insert(0,list(['interação','A','B','X','F(X)','TOLERÂNCIA']))
            for i in mat:
                print(i)
            print("A raiz do intervalo dado é: ",x)
    else:
        print("Não há raízes neste intervalo!")
