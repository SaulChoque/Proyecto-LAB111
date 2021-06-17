import random
def binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

def Ejercicio_1():
    print("""
    ###################################################################
    ##            HAS SELECCIONADO EL EJERCICIO NRO 1                ##
    ## ------------------------------------------------------------- ##
    ## Funcion para hallar la suma de todos los digitos del numero   ##
    ## hasta que quede solo un digito.                               ##
    ## Ejemplo: Si num=123456789                                     ##
    ## entonces 1+2+3+4+5+6+7+8+9 = 45; 4+6=9                        ##
    ###################################################################

    I N T R O D U C E   U N    N U M E R O
    """)
    a=list(str(input()))
    a = list(map(int, a))
    for i in a:
        print("+", end="")
        print(i, end="")
    s=sum(a)
    print("=",s)
    if s>9:
        a=list(str(s))
        for i in a:
            print("+", end="")
            print(i, end="")
        s = list(map(int, a))
        s=sum(s)
        print("=",s)

def Ejercicio_2():
    print("""
    ###################################################################
    ##            HAS SELECCIONADO EL EJERCICIO NRO 2                ##
    ## ------------------------------------------------------------- ##
    ## Funcion para generar la siguiente serie para n terminos:      ##
    ##        0,0,1,0,0,1,0,0,2,0,0,3,0,0,5,0,0,8,0,0                ##
    ###################################################################

    I N T R O D U C E   U N    N U M E R O
    """)
    a=0
    b=1
    c=0
    n=int(input())
    print("""
    L A   S E R I E   E S:
    """)
    for i in range(0, n, 1):
        if c<2:
            print("0", end=",")
            c+=1
        else:
            fn=a+b
            a=b
            b=fn
            print(a, end=",")
            c=0

def Ejercicio_3():
    print("""
    ###################################################################
    ##            HAS SELECCIONADO EL EJERCICIO NRO 3                ##
    ## ------------------------------------------------------------- ##
    ## Funcion para generar diez numeros enteros aleatorios en forma ##
    ## ascendente, comprendidos entre 1 y 10000, ambos inclusive, y  ##
    ## mostrar en pantalla el equivalente binario de cada numero.    ##
    ###################################################################

    L O S    N U M E R O S    S O N
    """)
    a=[]
    for i in range(10):
        a.append(random.randrange(1, 10000))
    a.sort()
    for i in a:
        b=binario(i)
        print(i,"=",b)


def Ejercicio_4():
    print("""
    ####################################################################
    ##            HAS SELECCIONADO EL EJERCICIO NRO 4                 ##
    ## -------------------------------------------------------------  ##
    ## Funcion para generar un vector donde el tamano debe ser        ##
    ## definido por teclado y almacenar en las posiciones impares del ##
    ## vector con los multiplos de un numero introducido por          ##
    ## teclado. Ejemplo, si se define un vector de tamano 10 y se     ##
    ## elige el numero 3, el vector debe contener:                    ##
    ## [0, 3, 2, 6, 4, 9, 6, 12, 8, 15]                               ##
    ####################################################################

    I N T R O D U C E   U N    N U M E R O
    """)
    n=int(input())
    m=int(input())
    a=[]; b=True
    for i in range(n):
        if b==True:
            a.append(i)
            b=False
        else:
            a.append(m)
            b=True
            m+=3
    print("""
    E L   V E C T O R   E S:
    """)            
    print(a)

def Acercade():
    print("""
    ####################################################################
    ##                 P R O Y E C T O   F I N A L                    ##
    ## -------------------------------------------------------------  ##
    ## Nombres y Apellidos: Saul Mijael Choquehuanca Huanca           ##
    ## C.I.: 10062315 L.P.                                            ##
    ## Docente: lic. Carlos Mullisaca Choque                          ##
    ## Correo Facultativo: schoquehuancah@fcpn.edu.bo                 ##
    ## Correo Electronico: saulchoque123@gmail.com                    ##
    ##                                                                ##
    ####################################################################
    """)

def error():
	print('error')

switch= {
	1: Ejercicio_1,
	2: Ejercicio_2,
	3: Ejercicio_3,
	4: Ejercicio_4,
    5: Acercade,
}


print("""
##############################################################################################################################
####    ⠀⠀⠀														  ####
####    ██████╗░██████╗░░█████╗░██╗░░░██╗███████╗░█████╗░████████╗░█████╗░    ███████╗██╗███╗░░██╗░█████╗░██╗░░░░░	  ####
####    ██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝██║████╗░██║██╔══██╗██║░░░░░	  ####
####    ██████╔╝██████╔╝██║░░██║░╚████╔╝░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║    █████╗░░██║██╔██╗██║███████║██║░░░░░	  ####
####    ██╔═══╝░██╔══██╗██║░░██║░░╚██╔╝░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║    ██╔══╝░░██║██║╚████║██╔══██║██║░░░░░	  ####
####    ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝    ██║░░░░░██║██║░╚███║██║░░██║███████╗	  ####
####    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░    ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝ 	  ####
#### 															  ####
#### ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⢀⣀⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀   .██▄██ █▀▀ █▄░█ █░░█                                                      	  ####
####    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠉⠉⠉⠉⠉⠉⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀   .█░▀░█ █▀▀ █▀██ █░░█                                                             ####
####    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀   .▀░░░▀ ▀▀▀ ▀░░▀ ░▀▀░                                                             ####
####    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⣠⣶⠛⠛⠛⠛⠛⠛⠳⣦⡀⠀⠘⣿⡄⠀⠀   .                                                             	 		  ####
####    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⢹⣿⣦⣀⣀⣀⣀⣀⣠⣼⡇⠀⠀⠸⣷⠀⠀     ▄ (1)  Ejercicio 1     //SUMA 1+2+3+4+5...                                     ####
####    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠉⠛⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⣿⡄⣠                                                                      	 	  ####
####    ⠀⠀⢀⣀⣀⣀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀     ▄ (2)  Ejercicio 2     //SERIE 0,0,1,0,0,1,0,0,2...                            ####
####    ⠿⠿⠟⠛⠛⠉⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀                                                                        	 	  ####
####    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀     ▄ (3)  Ejercicio 3     //NUMEROS ALEATORIOS Y BINARIOS                         ####
####    ⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀                 	                                                                  ####
####    ⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀     ▄ (4)  Ejercicio 4     //VECTOR [0,3,2,6,4,9,6,12,8,15] 		          ####
####    ⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀                                                                          	  ####
####    ⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣠⡶⠶⠿⠿⠿⠿⢷⣦⠀⠀⠀⠀⠀⠀⠀⣿⠀     ▄ (5)  Acerca de       //DATOS DEL ESTUDIANTE                                  ####
####    ⠀⠀⣀⣀⣀⠀⣸⡇⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⠀                                                                    	          ####
####    ⣠⡿⠛⠛⠛⠛⠻⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⣿⠀                                                                    	          ####
####    ⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⢀⣤⣤⣴⣿⠀⠀⠀⠀⠀⠀⠀⣿⠀                                                                    	          ####
####    ⠈⠙⢷⣶⣦⣤⣤⣤⣴⣶⣾⠿⠛⠁⢀⣶⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀                                                                  	          ####
####    ⢷⣶⣤⣀⠉⠉⠉⠉⠉⠄⠀⠀⠀⠀⠈⣿⣆⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡾⠃⠀                                                                  	 	  ####
####    ⠀⠈⠉⠛⠿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣿⣾⣿⡿⠿⠟⠋⠁⠀⠀⠀                                                17/06/2021                          ####
####                                                                                                             	  ####
##############################################################################################################################
""")
print(""" 
I N T R O D U C E   L A   O P C I O N
""")
sw=int(input())
switch.get(sw, error)()
