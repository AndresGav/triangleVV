from cmath import sqrt
import math
import unittest



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
    s= ((a+b+c)/2)
    return sqrt(s*(s-a)*(s-b)*(s-c))
    
def AreaIsosceles4(a,B):
    return ((a**2)/2)*math.sin(B)
    
def AreaIsosceles3(a,b):
    return (b * sqrt(a*2 - (b*2/4))/2)

def AreaEquilatero2(a):
    return ((sqrt(3)/4)*a*2)
    
def AreaRectangulo1(a,b):
    return (a*b)/2

class TestUtils(unittest.TestCase):
    def test_area(self):
        self.assertEqual(AreaEscaleno12(5,5,5),-11.986553433289231)
        self.assertEqual(AreaEscaleno11(1,1,45),0.4254517622670592)
        self.assertEqual(AreaEscaleno10(1,1,1),0.42073549240394825)
        self.assertEqual(AreaEscaleno9(5,5,5),-21.12821878904116)
        self.assertEqual(AreaEscaleno8(5,45,45),10.123594940899135)
        self.assertEqual(AreaEscaleno7(5,5,5),-21.12821878904116)
        self.assertEqual(AreaEscaleno6(5,7),17.5)
        self.assertEqual(AreaEscaleno5(5,12,45),463.02915674933473j)
        self.assertEqual(AreaIsosceles4(6,6),-5.0294789675806655)
        self.assertEqual(AreaIsosceles3(6,6),9+0j)
        self.assertEqual(AreaEquilatero2(6),5.196152422706632+0j)
        self.assertEqual(AreaRectangulo1(6,6),18.0)
        




unittest.main()
input("Enter para salir")
    
