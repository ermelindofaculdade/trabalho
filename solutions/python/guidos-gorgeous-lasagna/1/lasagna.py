"""Funções usadas na preparação da deliciosa lasanha de Guido.

Conheça Guido, o criador da linguagem Python:
https://en.wikipedia.org/wiki/Guido_van_Rossum

Esta é uma docstring de módulo, usada para descrever a funcionalidade
do módulo e de suas funções e/ou classes.
"""

# Constantes
EXPECTED_BAKE_TIME = 40  # tempo esperado de forno, em minutos
PREPARATION_TIME = 2    # tempo de preparo por camada, em minutos


def bake_time_remaining(elapsed_bake_time):
    """Calcula o tempo restante de cozimento.

    :param elapsed_bake_time: int - tempo já decorrido no forno (em minutos).
    :return: int - tempo restante de cozimento (em minutos), baseado em 'EXPECTED_BAKE_TIME'.

    Esta função recebe o número de minutos que a lasanha já passou no forno
    e retorna quantos minutos ainda faltam para terminar o cozimento,
    considerando o tempo total esperado definido em EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calcula o tempo total de preparo da lasanha.

    :param number_of_layers: int - número de camadas da lasanha.
    :return: int - tempo total de preparo (em minutos), baseado em 'PREPARATION_TIME'.

    Esta função calcula quantos minutos são necessários para montar a lasanha,
    multiplicando o número de camadas pelo tempo de preparo por camada.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula o tempo total decorrido desde o início do preparo até o momento atual.

    :param number_of_layers: int - número de camadas da lasanha.
    :param elapsed_bake_time: int - tempo já passado no forno (em minutos).
    :return: int - tempo total decorrido (em minutos), incluindo preparo e cozimento.

    Esta função retorna o tempo total gasto até agora: o tempo de preparo
    (montagem das camadas) mais o tempo que a lasanha já passou no forno.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time