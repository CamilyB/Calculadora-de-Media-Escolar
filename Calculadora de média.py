alunos = []

while True:
    nome = input("Digite o nome do aluno(a) (ou 'sair' para encerrar): ")
    if nome.lower() == "sair": #.lower() faz com que todo o conteúdo escrito pelo usúario seja lido em minúsculo, .upper() em maiúsculo
        break

    notas = []

    print("Digite as notas do aluno(a) (digite 'fim' para encerrar as notas).")

    while True:
        entrada = input("Nota: ")
        if entrada.lower() == "fim":
            break
        try:  #é usado para tentar executar o código
            nota = float(entrada)
            notas.append(nota)
        except ValueError:  #em vez de travar o programa pede para informar um valo válido
            print("Digite um número válido ou 'fim'. ")

    if len(notas) == 0:  #retorna a quantidade de elementos na lista, ou a quantidade de letras de um elemento da lista
        print("Nenhuma nota informada. Aluno(a) não registrado.")
        continue

    media = sum(notas) / len(notas)    #sum faz a soma de todos os números da lista
    situacao = "Aprovado" if media >= 6 else "Reprovado"

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)
    print(f"Aluno(a) {nome} cadastrado com sucesso!")

print("\n RESULTADO")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas do aluno(a): {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")    #.2f usado apenas para mostrar 2 casas decimais (.1f, uma casa, .3f, três casas, .0f, sem casas)
    print(f"Situacao: {aluno['situacao']}\n")