import random

print("\nJuego de Dos Donde una Persona Escribe la Cierta Cantidad de Palabras Para que el Otro Jugador Adivine con tan solo 5 Intentos.")

Desicion=0
Letra=""

try:

    while Desicion==0:
        print("\n     -----> PREGUNTAS")

        Palabras=[]

        CantP=int(input("\nIngresa la Cantidad de Palabras que Quieres Ingresar: "))
        
        Cont=0
        print("\n")
        #Ciclo que permite Almacenar las Palabras Introducidas por el Teclado
        while Cont<CantP:
            Palabra=input(("Ingresa Palabra: "))
            Palabras.append(Palabra)
            Cont+=1
        
            Adivina = random.choice(Palabras)

        Oportunidades=5
        
        Aciertos=[]
        Fallos=[]
        
        while Oportunidades>0:
            print("\nTotal de Oportunidades: ",Oportunidades)
            print("Letras Errones Tratadas: ",Fallos)
            print("Letras Acertadas Tratadas: ",Aciertos)
            print("\n")
            for Letra in Adivina:
                if Letra in Aciertos:
                    print(Letra, end=' ')
                else:
                    print('*', end=' ')

            if all(Letra in Aciertos for letra in Adivina):
                Oportunidades=0

            Letra=input("\n\nIngresa una letra: ")
            
            if Letra in Aciertos or Letra in Fallos:
                print("\n     -----> Ya Haz Intentado con es Letra!")
            elif Letra in Adivina:
                print("\n     -----> Letra acertada! Sigue Asi!")
                Aciertos.append(Letra)
            else:
                print("\n     -----> Recorcholis! Esa Letra no se Encuentra!")
                Fallos.append(Letra)
                Oportunidades-=1
        if all(Letra in Aciertos for letra in Adivina):
            print("\nHaz Ganado! La palabra es: ",Adivina)
        else:
            print("\n     -----> Has Perdido!!")
            print("\nLa palabra era: ",Adivina)

        Desicion=int(input("\nQuieres Volver a Intentarlo (Si-0 / No-1)? "))
        if Desicion!=1 and Desicion!=0:
            print("\nRespuesta NO Valida!")

except ValueError:
    print("\n     -----> Introduce Solo Datos Numericos Por favor.\n")
finally:
    print("     -----> Hasta la Proxima...\n")
