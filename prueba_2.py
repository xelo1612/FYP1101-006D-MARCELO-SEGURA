import os
productos = {'Escoba':5, 'huevo ': 25, 'leche':9}
menup = ['ver stock', 'añadir nuevo producto', 'ajustar stock', 'eliminar producto', 'salir']
while True:
    for ind in range (len(menup)):
        print(f'{ind + 1}.{menup[ind]}')
    ans = input('¿Que es lo que quiere hacer?\n')
    if ans == '1':
        os.system('cls')
        for a ,b in productos.items():
              print(f'{a}:{b}')
    elif ans == '2':
            os.system('cls')
            while True:
                nom = input('ingres nuevo porducto:\n')
                if nom.replace(' ', '').isalpha():
                    break
            if nom.lower() in productos:
                  os.system('cls')
                  print('error el prducto ya existe')
            else:
                  os.system('cls')
                  productos[nom.lower()] = 0
                  print('el producto se agrego con exito')
    elif ans == '3':
            os.system('cls')
            modificado = input('ingresa el nombre del producto a ajustar:\n')
            newstock = input('ingresa el nuevo stock del preoducto\n')
            productos[newstock]

    elif ans == '4':
            os.system('cls')
            while True:
                  nom = input('ingresa el producto que quieres eliminar:\n')

    elif ans == '5':
            os.system('cls')
            exit('Adios!')
    else:
            os.system
            print('error')





