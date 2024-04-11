print("Semana No.10: Ejercicio 1") 
mes=int(input("Ingrese un número entre 1 y 12:")) 
if mes<1 or mes>12:
    print("Error: el número debe de estar entre 1 y 12") 
else: 
    #Valindando con if
    if mes==1: 
        print("Mes: Enero")
    elif mes==2: 
        print("Mes: Febrero") 
    elif mes==3: 
        print("Mes: Marzo") 
    elif mes==4: 
        print("Mes: Abril")  
    elif mes==5: 
        print("Mes: Mayo") 
    elif mes==6: 
        print("Mes: Junio") 
    elif mes==7: 
        print("Mes: Julio") 
    elif mes==8: 
        print("Mes: Agosto") 
    elif mes==9: 
        print("Mes: Septiembre") 
    elif mes==10: 
        print("Mes: octubre") 
    elif mes==11: 
        print("Mes: noviembre") 
    elif mes==12: 
        print("Mes: diciembre")

print("Semana No. 10: Ejercicio 2")

a=int(input("Ingrese el primer número:"))
b=int(input("Ingrese el segundo número:"))
c=int(input("Ingrese el tercer número:"))

print("El número mayor es:")
if a<=0 or b<=0 or c<=0:
    print("Error: El número debe ser mayor a cero")

if a>b:
    if a>c:
        print(a)
    else: 
        if a==c:
            print(a,"y",c)
        else:
            print(c)
elif a==b:
    if a>c :
        print(a,"y",b)
    elif a==c:
        print(a,b,"y",c)
else:
        print(c)
if b>c:
    print(a,"y",b)
elif b==c:
    print(a,b,"y",c)  
else:
    print(c)