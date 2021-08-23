def main():
    #escribe tu código abajo de esta línea
    pass
print('Saldo del mes anterior: ')
ma=float(input())
print('Ingresos: ')
i=float(input())
print('Egresos')
eg=float(input())
print('Número de cheques expedidos: ')
ch=int(input())
sf=((ma+i)-eg)-(13*ch)
sf=sf*0.925
print('El saldo final de la cuenta es: ',sf)
      
if __name__ == '__main__':
    main()
