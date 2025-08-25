n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
nr = [n1+n2, n1-n2, n1*n2,n1/n2]
nnr = ["Soma:","Subtração:","Multiplicação:","Divisão:"]
for c in range (0, 4):
    print(nnr[c],nr[c])
