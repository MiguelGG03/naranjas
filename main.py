from clases.operaciones import op


def main():
    lista_final=[]


    #media 200g/desv tipic 30g/pruebas 100
    print('===================================================')
    print('   La funcion del siguiente programa es calcular la')
    print('probabilidad de que una naranja tenga por encima o ')
    print('por debajo de un peso determinado sabiendo que la  ')
    print('media de los pesos de las naranjas es 200 gramos.')
    print('===================================================\n')
    sigue=True
    while(sigue==True):
        p1=input('Desea seguir calculando las probabilidades?(S/N):')
        if(p1=='S'or p1=='s'):
            p2=str(input('Desea que el peso a calcular sea superior o\ninferior a los 200 gramos\n(1) Superior\n(2) Inferior\nRespuesta: '))
            print()
            if(p2=='1'):
                p2_1=int(input('Introduzca un numero entero para marcar el peso:'))
                calculo=200+p2_1
                print('Desea calcular la probabilidad de que sea\nmayor o menor que {}.\n(1)Mayor que {}g\n(2)Menor que {}g'.format(str(calculo),str(calculo),str(calculo)))
                pfr=str(input('-RESPUESTA: '))
                if(pfr=='1'):
                    calc=op.calc_encima_mayor(op,p2_1)
                    print(calc)
                    lista_final.append(calc)
                elif(pfr=='2'):
                    calc=op.calc_encima_menor(op,p2_1)
                    print(calc)
                    lista_final.append(calc)
                else:
                    print('\n\n\nRESPUESTA NO VALIDA')
            elif(p2=='2'):
                p2_2=int(input('Introduzca un numero entero para marcar el peso:'))
                calculo=200-p2_1
                print('Desea calcular la probabilidad de que sea\nmayor o menor que {}.\n(1)Mayor que {}g\n(2)Menor que {}g'.format(str(calculo),str(calculo),str(calculo)))
                pfr=str(input('-RESPUESTA: '))
                if(pfr=='1'):
                    calc=op.calc_debajo_mayor(p2_2)
                    print(calc)
                    lista_final.append(calc)
                elif(pfr=='2'):
                    calc=op.calc_debajo_menor(p2_2)
                    print(calc)
                    lista_final.append(calc)
                else:
                    print('\n\n\nRESPUESTA NO VALIDA')
            else:
                print('La respuesta debe ser un 1 o un 2')        
        elif(p1=='N'or p1=='n'):
            sigue=False
        else:
            print('Debe introducir una S o una N')



    pregunta_final=str(input('Desea imprimir todas las probabilidades calculadas?\n(1/s/S)Si\n(2/n/N)No\n'))
    if(pregunta_final=='1' or pregunta_final=='S' or pregunta_final=='s'):
        print('-HISTORIAL\n===========================')
        for i in lista_final:
            print(i)
        print('===========================')
    elif(pregunta_final=='1' or pregunta_final=='S' or pregunta_final=='s'):
        print('Cerrando programa...')
    else:
        print('Respuesta no valida')


if __name__=='__main__':
    main()
