def sincronizar(sinfonia):

    #revisamos cada sinfonia
    sincronizado = [sinfonia[0]]

    for i in range(1,len(sinfonia)):

        #creacion de lista silencios
        #aqui ocupe lista por compresion, tu no puedes ocuparlo
        #de ahi te enseño su version en for 
        silencio = ["--" for i in sinfonia[0]]


       

        #inicio nos indica en que parte de la melodia vamos

        #evita que edites partes de la melodia que ya arreglaste

        inicio = 0


        #vemos 1 a 1 las notas del instrumento

        for j in range(len(sinfonia[i])):


            #cambiar hace que cada nota en el instrumento solo 

            #se coloque una ves

            cambiar = True


            #recorremos el silencio

            for k in range(inicio, len(silencio)):


                #revisamos si la nota es igual a la melodia

                # y revisamos si podemos cambiarla

                if sinfonia[0][k] == sinfonia[i][j] and cambiar:

                    

                    #volvemos falso cambiar para que 

                    #solo editemos 1 vez por nota la melodia

                    cambiar = False


                    #cambiamos el silencio por la nota correspondiente

                    silencio[k] = sinfonia[i][j]

                    

                    #cambiamos inicio como la posicion siguiente

                    #a la que acabamos de revisar, asi evitamos casos 

                    #de dobles

                    inicio = k + 1

        

        #como silencio es una lista no podemos agregarla

        #y despues seguir editandola (python cosas)

        #ocupamos .copy() para hacer una lista

        #si no quieres usar .copy() por que te da miedito

        #puedo enseñarte a copiar una lista sin metodos

        sincronizado.append(silencio.copy())

    return sincronizado