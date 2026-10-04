import os

# Programa de cadastro de alunos

menu = """
1. Inserir aluno.
2. Listar alunos.
3. Buscar aluno.
4. Remover Aluno.
5. Mostrar média geral dos alunos.
6. Sair.
"""

alunos = []

# Funções das opções:

def inserir_aluno(nome, idade, nota):
    alunos.append({'nome': nome, 'idade': idade, 'nota': nota})

    return True


def listar_alunos():
    limpar_terminal()
    print(separador())
    print("O sistema retornou: \n")
    for aluno in alunos:
        print(formatar_aluno(aluno))
    print(separador())


def buscar_aluno(nome):
    for aluno in alunos:
        if aluno['nome'] == nome:
            return aluno

    return False


def remover_aluno(nome):
    for index, aluno in enumerate(alunos):
        if aluno['nome'] == nome:
            alunos.pop(index)

            return True

    return False


def obter_media():
    notas = []
    media = 0

    for aluno in alunos:
        notas.append(aluno['nota'])

    for nota in notas:
        media += int(nota)

    return media / len(notas)


def formatar_aluno(aluno):
    return f"Aluno: {aluno['nome']}, {aluno['idade']} anos, com nota {aluno['nota']}"


def separador():
    return '*'*10


def limpar_terminal():
    os.system('cls||clear')


def validar_input(input):
    if not input.isdigit():
        mensagem("Por favor, digite um número!")
        return

    if len(input) > 1:
        mensagem("Opção inválida!")
        return

    if int(input) > 6 or int(input) < 1:
        mensagem("Opção inválida!")
        return
    
    return input 


def mensagem(texto):
    limpar_terminal()
    
    if texto == True:
        return

    print(separador())
    print("O sistema retornou: \n")
    print(texto)
    print(separador())


while True:
    print('\nSISTEMA ESCOLAR V1.0')
    print(menu)
    print(separador())

    opcao = validar_input(input('Digite o número de uma opção: '))
    
    if opcao == '6': # Sair.
        mensagem("Até a próxima!")
        break

    if opcao == '1': # Inserir Aluno
        nome = input('Digite o nome do aluno: ')
        idade = input('Digite a idade do aluno: ')
        nota = input('Digite a nota do aluno: ')

        if inserir_aluno(nome, idade, nota):
            mensagem("Aluno inserido com sucesso!")

    if opcao == '2': # Listar Alunos
        listar_alunos()

    if opcao == '3': # Buscar Aluno
        nome = input('Digite o nome do aluno a ser pesquisado: ')

        aluno = buscar_aluno(nome)

        if aluno:
            mensagem("Aluno encontrado! \n" + formatar_aluno(aluno))
        else: mensagem("Aluno não encontrado!")

    if opcao == '4':
        nome = input('Digite o nome do aluno a ser removido: ')

        if remover_aluno(nome):
            mensagem("Aluno removido com sucesso!")
        else:
            mensagem("Aluno não encontrado!")


    if opcao == '5':
        media = obter_media()

        limpar_terminal()
        mensagem(f"A média dos alunos é: {media}")
