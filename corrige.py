import lista05 as L05

def teste_mini_calculadora():
    try:
        falhou = False
        if L05.mini_calculadora(30,200,90) != (20,9) : falhou = True
        if L05.mini_calculadora(5,62,5)  != 'IMPOSSIVEL' : falhou = True
        if L05.mini_calculadora(100,31,29)  != (31,29) : falhou = True
        if falhou:
            print('Funcao mini_calculadora NÃO está OK')
            return(0)
        else:
            print('Funcao mini_calculadora está OK')
            return(3.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_acoes_bolsa():
    try:
        falhou = False
        if L05.acoes_bolsa([3,1,-2,-3,5]) != 1 : falhou = True
        if L05.acoes_bolsa([-2,1,-2,1,0,-3]) != 0 : falhou = True
        if L05.acoes_bolsa([-1,-2,-3,-4,-5,-6,-7,-8]) != -10 : falhou = True
        if falhou:
            print('Funcao acoes_bolsa NÃO está OK')
            return(0)
        else:
            print('Funcao acoes_bolsa está OK')
            return(3.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_auto_estrada():
    try:
        falhou = False
        if L05.auto_estrada (5, 'DAPCD') != 5 : falhou = True
        if L05.auto_estrada (8, 'AACCAAPP') != 12 : falhou = True
        if L05.auto_estrada (14, 'ADCCPPPPPAADCP') != 21 : falhou = True
        if falhou:
            print('Funcao auto_estrada NÃO está OK')
            return(0)
        else:
            print('Funcao auto_estrada está OK')
            return(3.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_vestibular():
    try:
        falhou = False
        if L05.vestibular(7,'AEDBCCE','ADDCCBE') != 4 : falhou = True
        if L05.vestibular(5,'ABCDE','ABCDE') != 5 : falhou = True
        if L05.vestibular(10,'ABCDEABCDE','BCDEABCDEA') != 0 : falhou = True
        if falhou:
            print('Funcao vestibular NÃO está OK')
            return(0)
        else:
            print('Funcao vestibular está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_telefone():
    try:
        falhou = False
        if L05.telefone('PIPOCA') != '747622' : falhou = True
        if L05.telefone('FALE-SBC') != '3253-722' : falhou = True
        if falhou:
            print('Funcao telefone NÃO está OK')
            return(0)
        else:
            print('Funcao telefone está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_qtd_competidores():
    try:
        falhou = False
        if L05.qtd_competidores (3, 100, [(50,50),(100,0),(49,50)]) != 2 : falhou = True
        if L05.qtd_competidores (4, 235, [(100,134),(0,0),(200,200),(150,150)]) != 2 : falhou = True
        if falhou:
            print('Funcao qtd_competidores NÃO está OK')
            return(0)
        else:
            print('Funcao qtd_competidores está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)


def nota_da_prova():
  nota =  teste_mini_calculadora()
  nota += teste_acoes_bolsa()
  nota += teste_auto_estrada()
  nota += teste_vestibular()
  nota += teste_telefone()
  nota += teste_qtd_competidores()
  print("Seu somatorio de pontos:",nota)

nota_da_prova()
