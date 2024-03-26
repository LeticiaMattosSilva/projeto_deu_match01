# Lista para armazenar os candidatos
candidatos = [
    {'nome': 'João Souza Silva', 'nota_entrevista': 8.5, 'nota_tst_teorico': 4, 'teste_pratico': 5.5, 'nota_soft': 10},
    {'nome': 'Maria Lúcia Santana', 'nota_entrevista': 10, 'nota_tst_teorico': 7, 'teste_pratico': 8.5, 'nota_soft': 7.5},
    {'nome': 'Pedro de Assis Souza', 'nota_entrevista': 5, 'nota_tst_teorico': 10, 'teste_pratico': 8, 'nota_soft': 4},
    {'nome': 'Wanda Costa Nascimento', 'nota_entrevista': 5, 'nota_tst_teorico': 6, 'teste_pratico': 5.5, 'nota_soft': 8},
    {'nome': 'Carine Almeida de Jesus', 'nota_entrevista': 7, 'nota_tst_teorico': 5, 'teste_pratico': 9, 'nota_soft': 6}
]

# Função que filtra os candidatos
def filtrar_candidatos(nome, nota_entrevista, nota_tst_teorico, teste_pratico, nota_soft):

                #lista para armazenar resultados
                candidatos_filtrados = []

                #aqui a função passa por cada item da lista verificando se está o critério, se sim ela deposita na lista
                for candidato in candidatos:
                    if (candidato['nota_entrevista'] >= nota_entrevista and
                            candidato['nota_tst_teorico'] >= nota_tst_teorico and
                            candidato['teste_pratico'] >= teste_pratico and
                            candidato['nota_soft'] >= nota_soft):

                        candidatos_filtrados.append(candidato)
                return candidatos_filtrados


#laço de repetição infinito
while True:
    print('-=-'*20)
    print('O que você deseja fazer?')
    print('1. Inserir novo candidato.\n2. Filtrar candidatos pela nota.\n3. Sair')
    print('-=-' * 20)

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Digite o nome do(a) candidato(a): ')
        nota_entrevista = float(input('Qual a nota da entrevista? '))
        nota_tst_teorico = float(input('Qual a nota do teste teórico? '))
        teste_pratico = float(input('Qual a nota no teste prático? '))
        nota_soft = float(input('Qual a nota de soft skills?'))

        candidato = {'nome': nome, 'nota_entrevista': nota_entrevista, 'nota_tst_teorico': nota_tst_teorico,
                     'teste_pratico': teste_pratico, 'nota_soft': nota_soft}

        candidatos.append(candidato)
        
        print('-=-' * 20)
        print('\n***** Candidato inserido no banco de dados. *****\n')
        print('-=-' * 20)

    elif opcao == '2':
            nota_entrevista = float(input("Digite a nota mínima na entrevista: "))
            nota_tst_teorico = float(input("Digite a nota mínima no teste teorico: "))
            teste_pratico = float(input("Digite a nota mínima no teste prático: "))
            nota_soft = float(input("Digite a nota mínima em soft skills: "))

            #aqui candidatos filtrados recebe o resultado da função com os parametros digitados no input
            candidatos_filtrados = filtrar_candidatos(candidatos, nota_entrevista, nota_tst_teorico, teste_pratico, nota_soft)

            if candidatos_filtrados: #se candidatos_filtrados for true imprime

                print('-=-' * 20)
                print("\nCandidatos com notas iguais ou superiores às informadas:\n")


                for candidato in candidatos_filtrados: #forma para receber os resultados e imprimir
                    print(
                        f"Nome: {candidato['nome']}\nNota da entrevista: {candidato['nota_entrevista']}, "
                        f"Nota do teste teórico: {candidato['nota_tst_teorico']}, "
                        f"Nota teste prático: {candidato['teste_pratico']}, Nota em soft skills: {candidato['nota_soft']}\n")
                print('-=-' * 20)

            else: #se acima for false vem pra cá e imprime

                print('-=-' * 20)
                print('\n***** Não há candidados dentro dos requisitos solicitados. *****\n')
                print('-=-' * 20)

    elif opcao == '3':
        print('Programa encerrado')
        break

    else:
        print('-=-' * 20)
        print('\n***** Opção inválida. Por favor, escolha outra opção. *****\n')
        print('-=-' * 20)
