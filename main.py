from clases.naranjas import op


def main():
    print('===================================================')
    print('   La funcion del siguiente programa es calcular la')
    print('probabilidad de que una naranja tenga por encima o ')
    print('por debajo de un peso determinado sabiendo que la  ')
    print('media de los pesos de las naranjas es 200 gramos.')
    print('===================================================\n\n\n')
    sigue=False
    while(sigue==True):
        temp=0
        p1=input('Desea seguir calculando las probabilidades?(S/N):')
        if(p1=='S'or p1=='s'):
            p2=str(input('Desea que el peso a calcular sea superior o\ninferior a los 200 gramos\n(1) Superior\n(2) Inferior\nRespuesta: '))
            print()
            print()
            if(p2=='1'):
                p2_1=int(input('Introduzca un numero entero para marcar el peso:'))
            elif(p2=='2'):
                p2_2=int(input('Introduzca un numero entero para marcar el peso:'))
            else:
                print('La respuesta debe ser un 1 o un 2')        
        elif(p1=='N'or p1=='n'):
            sigue=False
        else:
            print('Debe introducir una S o una N')

if __name__=='__main__':
    main()
