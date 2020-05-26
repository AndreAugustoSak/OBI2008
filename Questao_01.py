# O principal prêmio da Olimpíada Brasileira de Informática é o convite para os cursos de programação oferecidos no
# Instituto de Computação da Unicamp, com todas as despesas pagas pela Fundação Carlos Chagas, patrocinadora
# da OBI. São convidados apenas os competidores que atingem um certo número mínimo de pontos, consideradas as
# duas fases de provas. Você foi contratado pela Coordenação da OBI para fazer um programa que, dados os
# números de pontos obtidos por cada competidor em cada uma das fases, e o número mínimo de pontos para ser
# convidado, determine quantos competidores serão convidados para o curso na Unicamp. Você deve considerar que
# - todos os competidores participaram das duas fases;
# - o total de pontos de um competidor é a soma dos pontos obtidos nas duas fases.
# Por exemplo, se a pontuação mínima para ser convidado é 435 pontos, um competidor que tenha obtido 200 pontos
# na primeira fase e 235 pontos na segunda fase será convidado para o curso na Unicamp. Já um competidor que
# tenha obtido 200 pontos na primeira fase e 234 pontos na segunda fase não será convidado.
# Você deve escrever uma função chamada qtd_competidores que recebe três argumentos. O primeiro argumento é
# um número inteiro N representando o número de competidores, o segundo é um número inteiro P representando o
# número mínimo de pontos para ser convidado, o terceiro argumento é uma lista de tamanho N, onde cada elemento
# da lista é uma tupla de dois números X e Y indicando a pontuação de um competidor em cada uma das fases.
# Sua função deve retornar um único número inteiro indicando o número de competidores que serão convidados a
# participar do curso na Unicamp.

def qtd_competidores(N, P, lista):
    aceitos = 0
    for c in range(N):
        competidor = lista[c]
        fase1 = competidor[0]
        fase2 = competidor[1]
        total = fase1 + fase2
        if total >= P:
            aceitos += 1
    return aceitos

print(qtd_competidores(3, 100, [(50,50),(100,0),(49,50)]))

