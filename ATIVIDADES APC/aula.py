#print("True and True")
#print("False and True")
#print("1 == 1 and 2 == 1")
#print("test" == "test")
#print("True and 1 == 1")
#print("1 == 1 or 2 !=1")
#print("False and 0 != 0")
#print("True or 1 == 1")
#print("test" != "testing")
#print("test" == 1)
#print("not (True and False)")
#print("not (True and False)")
#print("not (1 ==1 amd 0 !=1)")
#print("not (10 == 1 or 1000 == 1000)")
#print("not (1 != 10 or 3 == 4)")
#print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
#print( 1 == 1 and (not("testing" == 1 or 1 == 0)))
#print ("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
#print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))

#numero = float(input("Insira um numero"))
#if numero > 0:
    #print("O resultado é positivo")
#else:
    #print("O resultado é negativo")

#sal = float(input("Qual o seu salário?"))
#val = float(input("Qual o valor desejado?"))
#par = float (input("Quantas parcelas desejas fazer?"))
#resultado = 30 / 100 * sal
#parcela = val / par
#if par < resultado:
#    print("Empréstimo negado")
#else:
#    print("Empréstimo concedido")

#num = float (input("Informe o numero "))
#if num % 2 == 0:
#    print("O número é par")
#else:
#    print("O número é ímpar")

#atividade 5
'''

    salario = float(input("Digite seu salário: "))

    if salario <= 1412:
        inss = 0.075
    elif salario <= 2666:
        inss = 0.09
    elif salario <= 4000:
        inss = 0.12
    elif salario >= 7786:
        inss = 0.14
    else:
        inss = 0.14
    desconto = salario * inss
    liq = salario - desconto

    print(f"inss: {desconto}")
    print(f"liquido: {liq}")
'''
#atividade 6
'''
numA = float(input("Valor A: "))
numB = float(input("Valor B: "))

if numA > numB:
    print (f"o valor de A é maior que B: {numB}")
elif numB > numA:
    print (f"o valor de B é maior que A {numA}")
else:
    print(f"ambos os valores são iguais")
'''
#atividade 7
'''
primeiraNota = float(input("Digite sua nota: "))
segundaNota = float(input("Digite sua nota: "))
terceiraNota = float(input("Digite sua nota: "))

soma = (primeiraNota * 2 + segundaNota *3 + terceiraNota * 5) / 10


print ("A sua média é de: ", soma)
'''

#atividade 8
nome = (input("qual seu nome EV:"))

português = float(input( "Qual foi a sua nota em Português: "))
matematica = float(input("Qual foi a sua nota em Matemática: "))
conhecimentosGerais = float(input("Qual foi a sua nota Conhecimentos Gerais: "))


# Português
if português >= 7:
    print("Português: Aprovado")
else:
    print("Português: Reprovado")

# Matemática
if matematica >= 7:
    print("Matemática: Aprovado")
else:
    print("Matemática: Reprovado")

# Conhecimentos Gerais
if conhecimentosGerais >= 7:
    print("Conhecimentos Gerais: Aprovado")
else:
    print("Conhecimentos Gerais: Reprovado")

reprovadas = []
if português < 7:
    reprovadas.append("Português")
if matematica < 7:
    reprovadas.append("Matemática")
if conhecimentosGerais < 7:
    reprovadas.append("Conhecimentos Gerais")

resultado = (português + matematica + conhecimentosGerais) / 3

print("Sua média foi de:", resultado )
# Mostra o resultado
if len(reprovadas) == 0:
    print("Parabéns! Você foi aprovado em todas as matérias.")
else:
    print("Você foi reprovado nas seguintes matérias:", " e ".join(reprovadas))