#biblioteca para fazer o produto cartesiano
import itertools 

#função para união de dois conjuntos
def realizar_uniao(conjuntoA, conjuntoB):
    return conjuntoA.union(conjuntoB)

#função para intersecção de dois conjuntos
def realizar_interseccao(conjuntoA, conjuntoB):
    return conjuntoA.intersection(conjuntoB)

#função para diferença  entre dois conjuntos
def realizar_diferenca(conjuntoA, conjuntoB, sequencia):
    if sequencia:    
        diffAB = conjuntoA.difference(conjuntoB)
        if diffAB:
            return diffAB
        else:
            return "Conjunto A é um subconjunto de B."

    else:
        diffBA = conjuntoB.difference(conjuntoA)
        if diffBA:
            return diffBA
        else:
            return "Conjunto B é um subconjunto de A."

#função para calcular o produto cartesiano de dois conjuntos
def resolver_produto_cartesiano(conjuntoA, conjuntoB):
    cartesiano = itertools.product(conjuntoA, conjuntoB)
    return list(cartesiano)

#função que determina se um conjunto é subconjunto de outro
def verificar_conjunto(conjuntoA, conjuntoB, sequencia):
    if sequencia:
        return conjuntoA.issubset(conjuntoB)
    else:
        return conjuntoB.issubset(conjuntoA)

#função de execução do código
def __main__():
    conjuntoA = []
    conjuntoB = []
    print(f'\n------------ OPERAÇÕES COM CONJUNTOS -----------\n'
          f'\nPara começarmos, informe os seguintes valores:\n')
    
    #recolhimento de dados para criação dos conjuntos
    tamanhoA = int(input(f'\nTamanho de A: '))
    tamanhoB = int(input(f'Tamanho de B: '))
    for cont in range(tamanhoA):
        conjuntoA.append(float(input(f'Digite os valores do conjunto A: ')))
    for cont in range(tamanhoB):
        conjuntoB.append(float(input(f'Digite os valores do conjunto B: ')))
    A = set(conjuntoA)
    B = set(conjuntoB)

    while True:
        rep = True
        menu = int(input(f'\n[1] - União\n'
                         f'[2] - Intersecção\n'
                         f'[3] - Diferença\n'
                         f'[4] - Produto cartesiano\n'
                         f'[5] - Verificação de subconjunto (A ⊆ B)\n'
                         f'[6] - Verificação de subconjunto (B ⊆ A)\n'
                         f'[7] - Alteração dos conjuntos\n'
                         f'[8] - Sair\n'
                         f'\nSelecione uma opção: '))
        if menu == 1:
            uniao = realizar_uniao(A, B)
            print(f'\nUnião (A u B):\n', uniao)

        elif menu == 2:
            interseccao = realizar_interseccao(A, B)
            print(f'\nIntersecção (A ∩ B):\n', interseccao)


        elif menu == 3:
            while rep:
                escolha = int(input(f'\nQual operação você deseja realizar?\n'
                                    f'[1] - A - B\n'
                                    f'[2] - B - A\n'
                                    f'Selecione: '))
                
                #sistema de verificação da sequência dos conjuntos na operação
                if escolha == 1:
                    sequencia = True
                    rep = False

                elif escolha == 2:
                    sequencia = False
                    rep = False
                else:
                    print(f'\nOpção inválida. Tente novamente!\n')

            #sequencia = True: A - B
            #sequencia = False: B - A
            diff = realizar_diferenca(A, B, sequencia)
            if sequencia:
                print(f'\nDiferença (A - B):\n', diff)
               
            else:
                print(f'\nDiferença (B - A):\n', diff)

        elif menu == 4:
            prod = resolver_produto_cartesiano(A, B)
            print(f'\nProduto cartesiano (A x B):\n', prod)

        elif menu == 5:
            #sistema similar ao de verificação na operação de diferença
            a_e_b = True
            verif = verificar_conjunto(A, B, a_e_b)
            if verif:
                print(f'\nO conjunto {A}, é um subconjunto de {B}\n')
            else:
                print(f'\nA não é um subconjunto de B.\n')

        elif menu == 6:
            a_e_b = False
            verificar_conjunto(A, B, a_e_b)
            if verif:
                print(f'\nO conjunto {B}, é um subconjunto de {A}\n')
            else:
                print(f'\nB não é um subconjunto de A.\n')

        elif menu == 7:
            #recolhimento de dados idêntico ao primeiro, porém, para adicionar novos valores aos conjuntos
            novo_conjuntoA = []
            novo_conjuntoB = []
            tamanhoA = int(input('Tamanho de A: '))
            tamanhoB = int(input('Tamanho de B: '))
            for cont in range(tamanhoA):
                novo_conjuntoA.append(float(input(f'Digite os valores do novo conjunto A: ')))
            for cont in range(tamanhoB):
                novo_conjuntoB.append(float(input(f'Digite os valores do novo conjunto B: ')))
            A = set(novo_conjuntoA)
            B = set(novo_conjuntoB)

        elif menu == 8:
            print(f'Agradecemos pelo acesso!\n')
            break

        else:
            print('Opção inválida, tente novamente.')

__main__()