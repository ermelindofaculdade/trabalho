"""Funções para gerenciar os itens do carrinho de compras de um usuário."""


def add_item(current_cart, items_to_add):
    """Adiciona itens ao carrinho de compras.

    :param current_cart: dict - o carrinho de compras atual.
    :param items_to_add: iterável - itens a serem adicionados ao carrinho.
    :return: dict - o dicionário atualizado do carrinho do usuário.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Cria um carrinho de usuário a partir de uma entrada iterável de anotações.

    :param notes: iterável com itens a serem adicionados ao carrinho.
    :return: dict - dicionário do carrinho de compras do usuário.
    """
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Atualiza o dicionário de ideias de receitas.

    :param ideas: dict - o dicionário de "ideias de receitas".
    :param recipe_updates: iterável - atualizações para a seção de ideias (lista de pares (item, receita)).
    :return: dict - dicionário "ideias de receitas" atualizado.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Ordena o carrinho do usuário em ordem alfabética.

    :param cart: dict - dicionário do carrinho de compras do usuário.
    :return: dict - carrinho do usuário ordenado em ordem alfabética.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combina o pedido do usuário com informações de corredor e refrigeração.

    :param cart: dict - dicionário do carrinho de compras do usuário.
    :param aisle_mapping: dict - dicionário com informações de corredor e se é refrigerado.
    :return: dict - dicionário de preparo pronto para ser enviado à loja.
    """
    fulfillment = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment[item] = [quantity, aisle, refrigeration]
    # A saída deve estar em ordem alfabética reversa (exigência dos testes)
    return dict(sorted(fulfillment.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Atualiza os níveis de estoque da loja com o pedido do usuário.

    :param fulfillment_cart: dict - carrinho de preparo a ser enviado à loja.
    :param store_inventory: dict - estoque disponível na loja.
    :return: dict - estoque da loja atualizado.
    """
    for item, order_details in fulfillment_cart.items():
        ordered_qty = order_details[0]
        if item in store_inventory:
            current_stock = store_inventory[item][0]
            new_stock = current_stock - ordered_qty
            if new_stock <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_stock
    return store_inventory