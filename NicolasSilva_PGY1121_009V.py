#DATOS

from random import randint


menu = 0
afiliado = {}
valorcert = randint(1000, 1500)




#RUT
def rut():
  valida = True
  while valida:
    try:
      rut = int(input('Ingrese el Rut del afiliado sin guion ni puntos: '))
      if 5000000 <= rut <= 999999999:
        valida = False
      else:
        print('Numero de Rut invalido')
    except:    
        print('El Rut ingresado no debe tener digito verificador ni puntos')

  valida = True
  return rut

#NOMBRES
def name():
  name = input('Ingrese los Nombres del afiliado: ').upper()
  return name


#APELLIDOS
def last():
  last = input('Ingrese los Apellidos del afiliado: ').upper()
  return last

#EDAD
def years():
  valida = True
  while valida:
    try:
      years = int(input('Ingrese edad: '))
      if 18<= years <= 99:
        valida = False
      else:
         print('Anos invalidos')
    except:    
      print('La edad debe ser mayor a 18 anos y menor a 99 anos')
  valida = True
  return years

#ESTADO CIVIL
def estcivil():
    valida = True
    while valida:
        estcivil = input('Ingrese estado civil "C = Casado,S = Soltero,V = Viudo:  ').upper()
        try:
            if len(estcivil) == 1 and (estcivil in('c','C','s','S','V','v')):
                valida = False
            else:
                print('Debe ingresar solo caracter que sea (S/C/V)')
        except:
            print('El estado civil ingresado no es valido verifique el dato a ingresar')
    valida = True
    return estcivil


#GENERO
def gender():
    valida = True
    while valida:
        gender = input('Ingrese genero (F/M):  ')
        try:
            if len(gender) == 1 and (gender in('f','F','M','m')):
                valida = False
            else:
                print('Debe ingresar solo caracter que sea (F/M)')
        except:
            print('El genero ingresado no es valido verifique el dato a ingresar')
    valida = True
    return gender

#FECHA DE AFILIACION
def date():
  date = input('Ingrese Fecha de afiliacion: DD/MM/YY ')
  return date


#BUSCAR CERTIFICADO CON FUNCION 

def consulta():
  valida = True
  while valida:
    try:
      rut_consulta = input('\nIngrese el rut a consultar: ')
      print(f'\nEl rut consultado tiene los siguientes datos: ')
      print(afiliado[f'{rut_consulta}'])
      valida = False

    except:
      print('Registro no encontrado')

  valida = True
  return consulta

#IMPRIMIR CERTIFICADO
def certificado():
  valida = True
  while valida:
    try:
        rut_consulta = input('\nIngrese el rut del certificado a imprimir: ')
        print('\nCERTIFICADO DE AFILIADOS VIGENTES\n')
        for key, value in afiliado.items():
            print('Rut',key,'\nEl Valor del certificado:', valorcert)
        for variable, valores in value.items():
            print(variable, ' :', valores)
        valida = False

    except:
      print('Registro no encontrado')

  valida = True
  return certificado

#INICIO

print('Bienvenido a sistema de Registro de afiliacion de la ciudad de Santiago de Chile')

#MENU

while menu != 4:
    print('\nMenu Isapre Vida y Salud DuocUC ')
    print('\n1 Registar afiliado')
    print('\n2 Buscar afiliado')
    print('\n3 Imprimir Certificado')
    print('\n4 Salir')
    menu = int(input('\nIngrese la opcion deseada: '))


    #REGISTRO AFILIADO
    if menu == 1:
        print('\nOpcion 1 Registrar afiliado')

        confirma = input('\nDesea ingresar un afiliado?: S/N:  ')
        while confirma == 'S' or confirma == 's':
          rut_d = rut()
          nombre = name()
          apellido = last()
          anos = years()
          estado_civil = estcivil()
          genero = gender()
          fecha = date()
          afiliado[f'{rut_d}'] = {'NOMBRES': nombre,'APELLIDOS': apellido,'FECHA DE INGRESO': fecha,'ANOS': anos,'ESTADO CIVIL': estado_civil,'GENERO': genero,'FECHA': fecha}
          print(afiliado)
          confirma = input('\nDesea ingresar un afiliado?: S/N ')


    #BUSCAR afiliado
    if menu == 2:
      print('\nHas ingresado a la opcion consultar afiliado')
      consulta()

    if menu == 3:
      print('\nHas ingresado a la opcion Certificado')
      certificado()

    #MENU SALIDA
    elif menu == 4:
      print("\nHa salido del sistema")
      break

    #Opcion invalida
    else:
      print("\nIngrese opcion valida")
      continue