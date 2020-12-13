#resoler p 7
#o progama só roda se já estiver feito o download da bibioteca sympy!
#dica se for interpretado no site repl.it o download da sympy é automatico!
from sys import exit
from math import log,exp,sin,cos,pi
from sympy import diff #obs para usar essa biblioteca precisa fazer o download primeiro do sympy no python
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

#####################Funções###############################
def f(x):
    global k #usando uma variavel global na função
    return eval(k) #eval tranforma uma string em uma expressao
def primeiroxescolhido():
    global k #é do tipo string
    primeira_der=diff(k) #derivar a função em relação a x
    segunda_der=str(diff(primeira_der)) #função da sympy
    x=a
    if f(a)*(eval(segunda_der))>0: # f(a) mult com o ponto na segunda derivada
        return 1
    x=b
    if f(b)*(eval(segunda_der))>0:
        return 2
    else: #caso nao atenda a condição necessaria
        return 3
def derivada_do_x():
    return (diff(k)) #primeira derivada
def devidada_do_x_no_ponto():
    global x
    return eval(str(derivada_do_x()))
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
    print("Quando for usar o log neperiano Digite---> log('x'-número desejado)")
    print("EX: log(9) retorna o log neperiano de 9")
    print("Quando for usar o log na base 10 Digite---> log('x'-número desejado,10)")
    print("EX: log(9,10) retorna o log de 9 na base 10")
    print("\n"*5)   
    k=input("Digite a função: ")
    if f(a)*f(b)<0:#a e b sao intervalos pertencentes a condição
        if primeiroxescolhido()==1:
            x=a
        elif primeiroxescolhido()==2:
            x=b
        else:
            print("A condição não é suficiente para o método de Newton!")
            exit(0) #sys
        if f(x)==0:
            print("A raiz do intervalo dado é: ",x)
        else:
            mat=[]
            cont=0
            while True:
                if cont==0:
                    vet=[cont,a,b,x,f(x),"-"]
                else:
                    vet=[cont,"-","-",x,f(x),"-"]
                mat.append(vet)
                if cont>=1 and abs(mat[cont][3]-mat[cont-1][3])<=tolerancia or interacoes==cont+1: break #abs(f(x))<=tolerancia or abs(mat[cont][3]-mat[cont-1][3])/abs(mat[cont][3]) or 
                x=-f(x)/devidada_do_x_no_ponto()+x
                cont+=1
            for i in range(len(mat)):
                if i!=0:
                    mat[i][5]=abs(mat[i][3]-mat[i-1][3])
            for i in mat:
                print(i)
            print("A raiz do intervalo dado é: ",x)
    else:
        print("Não há raízes neste intervalo!")
