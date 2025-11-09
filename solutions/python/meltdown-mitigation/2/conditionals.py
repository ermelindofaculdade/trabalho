"""Funções para prevenir um colapso nuclear."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verifica se a criticidade do reator está equilibrada.

    :param temperature: int ou float - temperatura em kelvin.
    :param neutrons_emitted: int ou float - número de nêutrons emitidos por segundo.
    :return: bool - True se a criticidade estiver equilibrada, False caso contrário.

    Um reator está com criticidade equilibrada se:
    - A temperatura for menor que 800 K,
    - O número de nêutrons emitidos por segundo for maior que 500,
    - O produto da temperatura pelo número de nêutrons for menor que 500000.
    """

    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Avalia a zona de eficiência do reator.

    :param voltage: int ou float - tensão elétrica.
    :param current: int ou float - corrente elétrica.
    :param theoretical_max_power: int ou float - potência teórica máxima (100% de eficiência).
    :return: str - uma das opções: 'green', 'orange', 'red' ou 'black'.

    A eficiência é calculada como:
        (potência_gerada / potência_teórica_máxima) * 100
    onde potência_gerada = voltage * current.

    As faixas de eficiência são:
    - 'green':  eficiência >= 80%
    - 'orange': 60% <= eficiência < 80%
    - 'red':    30% <= eficiência < 60%
    - 'black':  eficiência < 30%
    """

    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    if efficiency >= 60:
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Avalia e retorna o código de status do reator.

    :param temperature: int ou float - temperatura em kelvin.
    :param neutrons_produced_per_second: int ou float - fluxo de nêutrons.
    :param threshold: int ou float - valor limite de referência.
    :return: str - um dos valores: 'LOW', 'NORMAL' ou 'DANGER'.

    O status é determinado pelo produto `temperature * neutrons_produced_per_second`:
    - 'LOW':      produto < 90% do threshold
    - 'NORMAL':   produto dentro de ±10% do threshold (ou seja, entre 90% e 110%)
    - 'DANGER':   produto fora desse intervalo
    """

    product = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold

    if product < lower_bound:
        return 'LOW'
    if product <= upper_bound:
        return 'NORMAL'
    return 'DANGER'