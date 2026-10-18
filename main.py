"""
Mega-Seninha
"""

ARQUIVO_ENTRADA = "APOSTAS.TXT"
ARQUIVO_SAIDA = "GANHADORES.TXT"


def formatar_cpf(cpf):
    """
    Recebe um CPF sem pontuação
    e retorna o CPF formatado.
    """

    cpf_formatado = (
        cpf[0:3] + "." +
        cpf[3:6] + "." +
        cpf[6:9] + "-" +
        cpf[9:11]
    )

    return cpf_formatado


def comparar_aposta(numeros_sorteados, numeros_apostados):
    """
    Compara os seis números da aposta
    com os seis números sorteados.
    """

    indice = 0
    acertou_todos = True

    while indice < 6:

        if numeros_apostados[indice] != numeros_sorteados[indice]:
            acertou_todos = False

        indice = indice + 1

    return acertou_todos


def processar_apostas():
    """
    Lê o arquivo de entrada, verifica os ganhadores
    e grava o resultado no arquivo de saída.
    """

    arquivo_entrada = open(ARQUIVO_ENTRADA, "r", encoding="utf-8")
    arquivo_saida = open(ARQUIVO_SAIDA, "w", encoding="utf-8")

    # Primeira linha contém os números sorteados
    linha_sorteio = arquivo_entrada.readline()

    numeros_sorteados = linha_sorteio.strip().split()

    # Próxima linha contém o primeiro CPF
    linha_cpf = arquivo_entrada.readline()

    quantidade_ganhadores = 0

    while linha_cpf != "":

        cpf = linha_cpf.strip()

        # A linha seguinte contém os seis números escolhidos
        linha_aposta = arquivo_entrada.readline()

        numeros_apostados = linha_aposta.strip().split()

        ganhou = comparar_aposta(
            numeros_sorteados,
            numeros_apostados
        )

        if ganhou == True:
# Após isso, ele formata o cpf do ganhador com a pontuação.
            cpf_formatado = formatar_cpf(cpf)

            arquivo_saida.write(
                cpf_formatado + "\n"
            )

            quantidade_ganhadores = quantidade_ganhadores + 1

        # Lê o próximo CPF
        linha_cpf = arquivo_entrada.readline()

    arquivo_entrada.close()
    arquivo_saida.close()

    print("Processamento concluído.")
    print(
        "Quantidade de ganhadores:",
        quantidade_ganhadores
    )
    print(
        "Arquivo",
        ARQUIVO_SAIDA,
        "criado com sucesso."
    )


processar_apostas()