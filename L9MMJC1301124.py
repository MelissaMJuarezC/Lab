print("Ejercicio 1: operaciones aritméticas")
#Captura de datos
n1=int(input("ingrese un número: "))
n2=int(input("Ingrese otro numero: "))

#Operaciones a realizar:
total=n1+n2
diferencia=n1-n2
producto=n1*n2
cocientereal=n1/n2
cocienteentero=n1//n2
residuo=n1%n2
potencia=n1**n2
#print("suma:",total)
print(n1,"+",n2,"=",total)
print(n1,"-",n2,"=",diferencia)
print(n1,"*",n2,"=",producto)
print(n1,"/",n2,"=",cocientereal)
print(n1,"//",n2,"=",cocienteentero)
print(n1,"%",n2,"=",residuo)
print(n1,"**",n2,"=",potencia)
print()

igualdad=n1==n2
mayorque=n1>n2
menorque=n1<n2
distinto=n1!=n2

print(n1,"es igual a",n2,"=",igualdad)
print(n1,"es mayor a",n2,"=",mayorque)
print(n1,"es menor a",n2,"=",menorque)
print(n1,"es igual a",n2,"=",distinto)

print()
print("Ejercicio 3: jerarquia de operadores")
a=int(input("Ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
c=int(input("ingrese el tercer número"))

i=a*b+c
ii=a*(b+c)
iii=a/(b+c)
iv=((3*a)+(2*b))//(c**2)

print("a*b+c=",i)
print("a(b+c)=",ii)
print("a/(b+c)=",iii)
print("3a+2b)/c**2=",iv)

print("Melissa María Juárez Cruz - 1301124")
n1 = float(input("Ingrese una cantidad en metros:  "))
print("Resultado")
#Operaciones
kilometros = n1/1000
millas = (n1/1000)/1.60934
pies = n1*3.28084
pulgadas = pies*12
#Representación
print("Millas : ",round(millas,2))
print("Kilómetros : ",round(kilometros,2))
print("Pies : ",round(pies,2))
print("Pulgadas : ",round(pulgadas,2))

print()
print("Melissa María Juárez Cruz - 1301124")
n2 = float(input("Ingrese otra cantidad en metros:  "))
print("Resultado")
#Operaciones
yardas = n2*1.09361
pies1 = n2*3.28084
pulgadas1 = pies1*12
#Representación
print("Yardas : ",yardas)
print("Pies : ", pies1)
print("Pulgadas : ",pulgadas1)