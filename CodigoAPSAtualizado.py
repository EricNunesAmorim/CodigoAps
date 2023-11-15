import math
print('''Programa para calcular quanto está sendo roubado de créditos de carbono na amazonia''')
try:
  while True:
    print('''
    CALCULO PARA REPOSIÇÃO DE DESMATAMENTO
    ''')
 
    print('''    ===================================
    |       1 - Um hectare            |
    |       2 - Cinco hectares        |
    |       3 - Dez hectares          |
    |       4 - Cinquenta Hectares    |
    |       5 - Cem Hectares          |
    ===================================
    | cada hectare são 565 arvores     |
    ===================================
    ''')
    opcarvore = int(input("\nDigite uma opção de quantia de arvores para calcular: "))
    if opcarvore == 1:
        co2 = 734.5
    elif opcarvore == 2:
        co2 = 3672.5
    elif opcarvore == 3:
        co2 = 7345
    elif opcarvore == 4:
        co2 = 36725
    elif opcarvore == 5:
        co2 = 73450
    elif opcarvore >=6:
        print('   essa opção não e válida')
        break
    idadearvore = int(input("\nQual a idade das arvores desmatadas em média? (em meses): "))
    if opcarvore == 1:
        qtdarvore = 565
    elif opcarvore == 2:
        qtdarvore = 5 * 565
    elif opcarvore == 3:
        qtdarvore = 10 * 565
    elif opcarvore == 4:
        qtdarvore = 50 * 565
    elif opcarvore == 5:
        qtdarvore = 100 * 565
    roubototal = math.floor(co2 * idadearvore)
    roubocredito = math.floor(roubototal/1000)
    arvdesmatadas = int(input("\nQuantas árvores foram desmatadas em média? :"))
    arvdiferença = qtdarvore - arvdesmatadas
    metacredito = int(input("\nQual a meta da sua empresa em créditos de carbono?: "))
    dividacredito = metacredito - roubocredito
    if dividacredito >= 1:
      print (f"\nas {arvdiferença:,} arvores roubaram {roubototal:,} kg co² no total e conseguiram {roubocredito:.0f} créditos de carbono, mas faltam {dividacredito:.0f} créditos de carbono para sua empresa antigir a meta")
    elif dividacredito <=0:
      print (f"\nas {arvdiferença:,} arvores roubaram {roubototal:,} kg co² no total e conseguiram {roubocredito:.0f} créditos de carbono, e sua empresa atingiu a meta de crédito de carbono")
    x = input('\nDigite algo para fazer outra consulta ou enter para encerrar: ')
    if x == "":
      break
    else:
      continue
  print ('''  ============================
  |  Você saiu do programa.  |
  ============================''')
except ValueError:
    print('Favor, digite Apenas números!')
except:
    print('Você digitou algo que não estava nas opções')
