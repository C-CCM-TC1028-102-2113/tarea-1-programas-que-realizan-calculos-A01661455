def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    pass
print('Dame el número de mensajes: ')
m=int(input())
print('Dame el número de megas ')
meg=float(input())
print('Dame el número de minutos: ')
mi=int(input())

cm=((m*0.80)+(meg*0.80)+(mi*0.80))
cm=round(cm,2)

print('Es costo mensual es de: ',cm)

if __name__ == '__main__':
    main()
