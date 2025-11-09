"""Funções que ajudam o engenheiro da locomotiva a acompanhar o trem."""


def get_list_of_wagons(*args):
    """Retorna uma lista de vagões.

    :param args: número arbitrário de IDs de vagões.
    :return: list - lista com os IDs dos vagões na ordem fornecida.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Corrige a lista de vagões movendo os dois últimos para o final e inserindo os vagões faltantes após a locomotiva.

    A locomotiva é sempre o primeiro vagão (índice 0). Os dois últimos vagões são temporariamente removidos,
    a locomotiva é mantida no início, seguida pelos vagões faltantes, e depois o restante da lista original,
    terminando com os dois vagões que foram removidos no início.

    :param each_wagons_id: list - lista original de IDs de vagões (incluindo a locomotiva em first).
    :param missing_wagons: list - lista de vagões faltantes a serem inseridos logo após a locomotiva.
    :return: list - lista de vagões corrigida.
    """
    a, b, locomotiva, *resto = each_wagons_id
    return [locomotiva] + missing_wagons + resto + [a, b]


def add_missing_stops(route, **stops):
    """Adiciona paradas faltantes ao dicionário de rota.

    :param route: dict - dicionário com informações da rota (ex: {'código': 'L1', 'destino': 'Marte'}).
    :param stops: número arbitrário de paradas nomeadas como `stop_1`, `stop_2`, etc.
    :return: dict - dicionário de rota atualizado com uma nova chave 'stops' contendo uma lista das paradas.
    """
    # Extrai os valores das paradas em ordem (stop_1, stop_2, ...) e os coloca em uma lista
    stops_list = [stops[key] for key in sorted(stops.keys())]
    route_updated = route.copy()
    route_updated["stops"] = stops_list
    return route_updated


def extend_route_information(route, more_route_information):
    """Estende as informações da rota com dados adicionais.

    :param route: dict - as informações originais da rota.
    :param more_route_information: dict - informações extras a serem mescladas.
    :return: dict - dicionário combinado com todas as chaves dos dois dicionários.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Reorganiza as linhas do depósito de vagões para agrupar por cor/tipo.

    Cada linha representa uma cor/tipo (ex: vermelho, azul, verde). Cada elemento é um vagão (ID, cor).
    A função reorganiza para que cada nova linha contenha todos os vagões da mesma posição nas listas originais.

    Exemplo:
        Entrada: [[(1, "red"), (2, "blue")], [(3, "red"), (4, "blue")]]
        Saída:   [[(1, "red"), (3, "red")], [(2, "blue"), (4, "blue")]]

    :param wagons_rows: list[list[tuple]] - lista de linhas de vagões.
    :return: list[list[tuple]] - lista de colunas reorganizadas (agora agrupadas por posição).
    """
    # Transpõe a matriz: converte linhas em colunas
    return [list(coluna) for coluna in zip(*wagons_rows)]