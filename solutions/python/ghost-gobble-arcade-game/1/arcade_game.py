"""Funções para implementar as regras do clássico jogo de arcade Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verifica se o Pac-Man pode comer um fantasma ao estar com pílula de poder ativa.

    :param power_pellet_active: bool - o jogador está com uma pílula de poder ativa?
    :param touching_ghost: bool - o jogador está tocando um fantasma?
    :return: bool - é possível comer o fantasma?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verifica se o Pac-Man marcou pontos ao comer uma pílula de poder ou um ponto.

    :param touching_power_pellet: bool - o jogador está tocando uma pílula de poder?
    :param touching_dot: bool - o jogador está tocando um ponto?
    :return: bool - o jogador marcou pontos?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Determina se o jogador perdeu o jogo (GAME OVER) ao tocar um fantasma sem pílula de poder.

    :param power_pellet_active: bool - o jogador está com uma pílula de poder ativa?
    :param touching_ghost: bool - o jogador está tocando um fantasma?
    :return: bool - o jogador perdeu o jogo?
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Verifica se o jogador venceu o jogo ao comer todos os pontos.

    Mesmo que o jogador esteja tocando um fantasma, ele vence desde que tenha comido
    todos os pontos e **não** tenha perdido (ou seja, a derrota não deve ocorrer).

    :param has_eaten_all_dots: bool - o jogador "comeu" todos os pontos?
    :param power_pellet_active: bool - o jogador está com uma pílula de poder ativa?
    :param touching_ghost: bool - o jogador está tocando um fantasma?
    :return: bool - o jogador venceu o jogo?
    """
    # Só vence se comeu todos os pontos E não perdeu (ou seja, não está tocando fantasma sem poder)
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)