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
        p1=input('Desea seguir calculando las probabiilidades?(S/N):')
        if(p1=='S'or p1=='s'):
            p2=int()
        elif(p1=='N'or p1=='n'):
            sigue=False
        else:
            print('Debe introducir una S o una N')

if __name__=='__main__':
    main()
