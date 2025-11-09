"""Funções para ajudar a jogar e pontuar um jogo de blackjack.

Como jogar blackjack:    https://bicyclecards.com/how-to-play/blackjack/  
Cartas padrão (52 cartas): https://en.wikipedia.org/wiki/Standard_52-card_deck  
"""


def value_of_card(card):
    """Determina o valor de pontuação de uma carta.

    :param card: str - carta recebida.
    :return: int - valor da carta. Veja abaixo os valores:

    1. 'J', 'Q' ou 'K' (cartas de face) = 10
    2. 'A' (ás) = 1
    3. '2' a '10' = valor numérico.
    """

    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determina qual carta tem o valor mais alto na mão.

    :param card_one, card_two: str - cartas recebidas.
    :return: str ou tuple - retorna a carta de maior valor ou uma tupla com ambas se forem iguais.

    Usa as mesmas regras de valor das cartas definidas em value_of_card.
    """

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calcula o valor mais vantajoso para um ás futuro.

    :param card_one, card_two: str - cartas já na mão.
    :return: int - valor do ás a ser usado: 1 ou 11.

    Regra: o ás vale 11 somente se a soma atual (com ás contando como 11) não ultrapassar 21.
    Nota: se houver um ás já na mão, ele é contado como 11 apenas se possível.
    """

    # Se já há um 'A' nas cartas, devemos tratá-lo como 11 ao calcular a soma atual
    def card_value_for_ace_calc(card):
        if card == 'A':
            return 11
        return value_of_card(card)

    current_sum = card_value_for_ace_calc(card_one) + card_value_for_ace_calc(card_two)

    # Se somar 11 ultrapassaria 21, o novo ás deve valer 1
    return 1 if current_sum + 11 > 21 else 11


def is_blackjack(card_one, card_two):
    """Verifica se a mão é um 'blackjack' natural (21 com duas cartas).

    :param card_one, card_two: str - cartas recebidas.
    :return: bool - True se for blackjack, False caso contrário.

    Blackjack = um ás (A) + uma carta de valor 10 (10, J, Q ou K).
    """

    ten_cards = ('10', 'J', 'Q', 'K')
    has_ace = card_one == 'A' or card_two == 'A'
    has_ten = (card_one in ten_cards) or (card_two in ten_cards)
    return has_ace and has_ten


def can_split_pairs(card_one, card_two):
    """Verifica se o jogador pode dividir o par.

    :param card_one, card_two: str - cartas recebidas.
    :return: bool - True se as cartas têm o mesmo valor, permitindo divisão.
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Verifica se o jogador pode fazer 'double down'.

    :param card_one, card_two: str - cartas iniciais.
    :return: bool - True se a soma das cartas for 9, 10 ou 11.
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)