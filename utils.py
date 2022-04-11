from cmath import sqrt
import math

from numpy import double
from img import *
import os
import math
import os



def AreaEscaleno12(b,c,A):
    return (b*c*math.sin(A))/2
    
def AreaEscaleno11(a,c,B):
    return (a*c*math.sin(B))/2
    
def AreaEscaleno10(a,b,C):
    return (a*b*math.sin(C))/2  

def AreaEscaleno9(c,A,B):
    numerador = (c**2)*math.sin(A)*math.sin(B)
    denominador = 2*math.sin(A+B)
    return numerador/denominador 

def AreaEscaleno8(b,A,C):
    numerador = (b**2)*math.sin(A)*math.sin(C)
    denominador = 2*math.sin(A+C)
    return numerador/denominador 
    
def AreaEscaleno7(a,B,C):
    numerador = (a**2)*math.sin(B)*math.sin(C)
    denominador = 2*math.sin(B+C)
    return numerador/denominador 
    
def AreaEscaleno6(base,h):
    return (base*h)/2 
    
def AreaEscaleno5(a,b,c):
    s= (a+b+c)/2
    return sqrt(s*(s-a)(s-b)(s-c))
    
def AreaIsosceles4(a,c,B):
    return ((a**2)/2)*math.sin(B)
    
def AreaIsosceles3(a,b):
    return (b * sqrt(a*2 - (b*2/4))/2)

def AreaEquilatero2(a):
    return ((sqrt(3)/4)*a*2)
    
def AreaRectangulo1(a,b):
    return (a*b)/2


def menu():
    os.system('cls')
    print("Seleccione el tipo de triangulo:")
    ImgAreaRectangulo()
    # print("\t1 Triangulo Rectangulo")
    ImgAreaEquilatero()
    # print("\t2 Triangulo Equilatero")
    ImgAreaIsosceles()
    # print("\t3 Triangulo Isosceles")
    ImgAreaEscaleno()
    # print("\t4 Triangulo Escaleno")
    print("\t5 Salir")
    
while True:
    menu()
    opcionMenu= input("Insertar la opcion para elegir el tipo de triangulo >>\n")
    if opcionMenu=="1":
        
        print("Ingrese los lados del triangulo")
        a= double(input("Ingrese el valor del lado a: "))
        b= double(input("Ingrese el valor del lado b: "))
        print (AreaRectangulo1(a,b))
        input("\nDe enter para continuar...\n")
      
    elif opcionMenu=="2":
        
        print("\nIngrese el valor del lado del triangulo\n")
        a= double(input("Ingrese el valor del lado a"))
        print (AreaEquilatero2(a))
        input("\nDe enter para continuar...\n")
      
    elif opcionMenu=="3":
        
        def menu():
          os.system('cls')
        
          print("Seleccione el tipo de triangulo:")
          print("\t1 Triangulo por lados a b: ")
          print("\t2 Triangulo por lados a c y angulo B: ")
          print("\t3 Regresar")
        while True:
          menu()
          opcionMenu2= input("Insertar la opcion para elegir el tipo de triangulo >>")
          if opcionMenu2=="1":
            
            print("Ingresar los valores de los lados del triangulo")
            a= double(input("Ingrese el valor del lado a: ")) 
            b= double(input("Ingrese el valor del lado b: "))
            print (AreaIsosceles3(a,b))
            input("\nDe enter para continuar...\n")

          elif opcionMenu2=="2":
            
            print("Ingresar los valores para el calculo")
            a= double(input("Ingresar el valor del lado a: "))
            c= double(input("Ingresar el valor del lado c: "))
            B= double(input("Ingresar el valor del angulo B: "))

            print (AreaIsosceles4(a,c,B))

            input("\nDe enter para continuar...\n")
            

          elif opcionMenu2=="3":
            break #revisar ----------------
          else:
            print("")
            input("Seleccione una opcion")
    elif opcionMenu=="4":
        print("")
        def menu():
          os.system('cls')
          ImaAreaEquilatero1()
          print("Seleccione el tipo de triangulo:")
          print("\t1 Triangulo por lados a b c")
          print("\t2 Triangulo por base y altura")
          print("\t3 Triangulo por lado a y angulos B C")
          print("\t4 Triangulo por lado b y angulos A C")
          print("\t5 Triangulo por lado c y angulos A B")
          print("\t6 Triangulo por lado a b y angulo C")
          print("\t7 Triangulo por lado a c y angulo B")
          print("\t8 Triangulo por lado b c y angulo A")
          print("\t9 Regresar")
        while True:

          menu()
          opcionMenu3= input("Insertar la opcion para elegir el tipo de triangulo >>")
          if opcionMenu3=="1":
            print("")
            print("Ingrese los valores de los lados")
            a= double(input(" Ingrese los valores del lado a: "))
            b= double(input(" Ingrese los valores del lado b: "))
            c= double(input(" Ingrese los valores del lado c: "))
            print (AreaEscaleno5(a,b,c))
            input("\nDe enter para continuar...\n")

          elif opcionMenu3=="2":
            print("")
            print ("Ingrese los valores de la base y la altura del triángulo")
            base = double(input("Ingrese el valor de la base: "))
            h= double(input("Ingrese el valor de la altura: "))

            print (AreaEscaleno6(base,h))

            input("\nDe enter para continuar...\n")
            
          elif opcionMenu3=="3":
            print("")
            print ("Ingrese los valores del los lados a y angulos B C")
            a = double(input("Ingrese el valor del lado a: "))
            B = double(input("Ingrese el valor del angulo B: "))
            C = double(input("Ingrese el valor del angulo C: "))
            print (AreaEscaleno7(a,B,C))
            input("\nDe enter para continuar...\n")
            
          elif opcionMenu3=="4":
            print("")
            print ("Ingrese los valores del los lados b y angulos A C")
            b = double(input("Ingrese el valor del lado b: "))
            A = double(input("Ingrese el valor del angulo A: "))
            C = double(input("Ingrese el valor del angulo C: "))
            print (AreaEscaleno8(b,A,C))
            input("\nDe enter para continuar...\n")

          elif opcionMenu3=="5":
            print("")
            print("Ingrese los valores del los lados c y angulos A B")
            c= double(input("Ingrese el valor del lado c: "))
            A= double(input("Ingrese el valor del angulo A: "))
            B= double(input("Ingrese el valor del angulo B: "))
            print (AreaEscaleno9(c,A,B))
            input("\nDe enter para continuar...\n")
            
          elif opcionMenu3=="6":
            print("")
            print("Ingrese los valores del los lados a b y angulo C")
            a= double(input("Ingrese el valor del lado a: "))
            b = double(input("Ingrese el valor del lado b: "))
            C = double(input("Ingrese el valor del angulo C: "))
            print (AreaEscaleno10(a,b,C))
            input("\nDe enter para continuar...\n")

          elif opcionMenu3=="7":
            print("")
            print("Ingrese los valores del los lados a c y angulo B")
            a= double(input("Ingrese el valor del lado a: "))
            c= double(input("Ingrese el valor del lado c: "))
            B= double(input("Ingrese el valor del angulo B: "))
            print (AreaEscaleno11(a,c,B))
            input("\nDe enter para continuar...\n")

          elif opcionMenu3=="8":
            print("")
            print("Ingrese los valores del los lados b c y angulo A")
            b = double(input("Ingrese el valor del lado b: "))
            c = double(input("Ingrese el valor del lado c: "))
            A= double(input("Ingrese el valor del angulo A: "))
            print (AreaEscaleno12(b,c,A))
            input("\nDe enter para continuar...\n")
            
          elif opcionMenu3=="9":
            break #revisar ----------------
          else:
            print("")
            input("Seleccione una opcion")
    elif opcionMenu=="5":
        break
    else:
        print("")
        input("usted no a ingresado una opcion valida")