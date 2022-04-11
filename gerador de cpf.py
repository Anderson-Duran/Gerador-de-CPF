def gerador_de_cpf():
    from random import randint

    cpf = []
    # GERANDO OS PRIMEIROS 9 DIGITOS CPF
    for i in range(9):
        i = randint(0, 9)
        cpf.append(i)

    # GERANDO O 1º DIGITO DO CPF
    soma = 0
    valor = 0
    p = len(cpf) + 1

    for n in cpf:
        soma += p * n
        p -= 1

    if soma % 11 == 0 or soma % 11 == 1:
        cpf.append(0)


    else:
        r = 11 - soma % 11
        cpf.append(r)

    # GERANDO 2º DIGITO DO CPF
    soma = 0
    valor = 0
    p = len(cpf)

    for n in cpf[1:]:
        soma += p * n
        p -= 1

    if soma % 11 == 0 or soma % 11 == 1:
        cpf.append(0)

    else:
        r = (11) - soma % 11
        cpf.append(r)
    print('=' * 33)
    c = 0
    print(f" O CPF gerado foi", end=' ')
    for n in cpf:
        print(n, end='')
        if c == 2 or c == 5:
            print('.', end='')
        if c == 8:
            print('-', end='')
        c += 1
    print()
    print('=' * 33)


def linha():
    print(f'=' * 40)


linha()
print(f'{"GERADOR DE NÚMERO DE CPF":^40}')
linha()
while True:
    resposta = str(input("Deseja gerar um número de CPF [S/N]? ")).capitalize()[0]
    if resposta in "S":
        gerador_de_cpf()
        while True:
            resposta = str(input(('Deseja gerar mais um número de CPF [S/N]? '))).capitalize()[0]
            if resposta in "S":
                gerador_de_cpf()
            elif resposta in "N":
                break
            else:
                print("Resposta inválida!\nDigite apenas sim ou não!")
        break
    elif resposta in "N":
        break
    else:
        print("Resposta digitada inválida!\nDigite apenas sim ou não!")
linha()
print(f"{' OBRIGADO POR UTILIZAR O NOSSO PROGRAMA!':^40}")
linha()
