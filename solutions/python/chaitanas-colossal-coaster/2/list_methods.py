"""Funções para gerenciar e organizar filas na montanha-russa de Chaitana."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Adiciona uma pessoa à fila 'expressa' ou 'normal', dependendo do tipo de ingresso.

    :param express_queue: list - nomes na fila de embarque rápido (Fast-track).
    :param normal_queue: list - nomes na fila normal.
    :param ticket_type: int - tipo de ingresso. 1 = expresso, 0 = normal.
    :param person_name: str - nome da pessoa a ser adicionada à fila.
    :return: list - a fila (atualizada) à qual o nome foi adicionado.
    """

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue, friend_name):
    """Procura um nome na fila e retorna sua posição (índice).

    :param queue: list - nomes na fila.
    :param friend_name: str - nome do amigo a ser localizado.
    :return: int - índice em que o nome do amigo foi encontrado.
    """

    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Insere o nome de quem chegou atrasado em um índice específico da fila.

    :param queue: list - nomes na fila.
    :param index: int - índice onde o novo nome será inserido.
    :param person_name: str - nome a ser inserido.
    :return: list - fila atualizada com o novo nome.
    """

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove a pessoa malvada da fila pelo nome fornecido.

    :param queue: list - nomes na fila.
    :param person_name: str - nome da pessoa malvada.
    :return: list - fila atualizada com o nome da pessoa malvada removido.
    """

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Conta quantas vezes o nome fornecido aparece na fila.

    :param queue: list - nomes na fila.
    :param person_name: str - nome que deseja contar ou rastrear.
    :return: int - número de vezes que o nome aparece na fila.
    """

    return queue.count(person_name)


def remove_the_last_person(queue):
    """Remove a pessoa na última posição da fila e retorna seu nome.

    :param queue: list - nomes na fila.
    :return: str - nome que foi removido do final da fila.
    """

    return queue.pop()


def sorted_names(queue):
    """Ordena os nomes da fila em ordem alfabética e retorna o resultado.

    :param queue: list - nomes na fila.
    :return: list - cópia da fila ordenada em ordem alfabética.
    """

    return sorted(queue)