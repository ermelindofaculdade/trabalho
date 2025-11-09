"""Funções para rastrear rodadas de pôquer e realizar diversas tarefas com cartas.

Documentação de listas em Python: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Cria uma lista contendo o número da rodada atual e as duas seguintes.

    :param number: int - número da rodada atual.
    :return: list - rodada atual e as duas rodadas subsequentes.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatena duas listas de números de rodadas.

    :param rounds_1: list - primeira lista de rodadas jogadas.
    :param rounds_2: list - segunda lista de rodadas jogadas.
    :return: list - todas as rodadas jogadas combinadas.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Verifica se a lista de rodadas contém o número especificado.

    :param rounds: list - lista de rodadas já jogadas.
    :param number: int - número da rodada a ser verificado.
    :return: bool - True se a rodada foi jogada, False caso contrário.
    """

    return number in rounds


def card_average(hand):
    """Calcula e retorna a média dos valores das cartas na mão.

    :param hand: list - cartas na mão (lista de inteiros).
    :return: float - valor médio das cartas.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Verifica se a média real é igual a pelo menos uma de duas aproximações:
    (1) a média entre a primeira e a última carta, ou
    (2) o valor da carta do meio (mediana, para listas ímpares).

    :param hand: list - cartas na mão.
    :return: bool - True se pelo menos uma das aproximações for igual à média real.
    """

    media_real = card_average(hand)
    media_extremos = (hand[0] + hand[-1]) / 2
    # Para a mediana: assumimos que a lista tem tamanho ímpar (como nos exemplos típicos do exercício)
    carta_do_meio = hand[len(hand) // 2]

    return media_real == media_extremos or media_real == carta_do_meio


def average_even_is_average_odd(hand):
    """Verifica se a média dos valores nas posições pares é igual à média dos valores nas posições ímpares.

    :param hand: list - cartas na mão.
    :return: bool - True se as médias forem iguais, False caso contrário.
    """

    # Índices pares: 0, 2, 4, ...
    pares = hand[::2]
    # Índices ímpares: 1, 3, 5, ...
    impares = hand[1::2]

    if not pares:  # evita divisão por zero (embora o exercício normalmente não passe listas vazias)
        media_pares = 0
    else:
        media_pares = sum(pares) / len(pares)

    if not impares:
        media_impares = 0
    else:
        media_impares = sum(impares) / len(impares)

    return media_pares == media_impares


def maybe_double_last(hand):
    """Dobra o valor da última carta se for um Valete (Jack), representado pelo valor 11.

    :param hand: list - cartas na mão.
    :return: list - mão com o Valete final (se houver) dobrado.
    """

    if hand and hand[-1] == 11:
        hand[-1] = 22
    return hand