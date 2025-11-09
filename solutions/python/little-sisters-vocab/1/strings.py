"""Funções para criar, transformar e adicionar prefixos a strings."""


def add_prefix_un(word):
    """Adiciona o prefixo 'un' à palavra fornecida.

    :param word: str - contém a palavra raiz.
    :return: str - palavra raiz com o prefixo 'un' adicionado no início.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """Transforma uma lista contendo um prefixo e palavras em uma string formatada.

    :param vocab_words: list - lista de palavras de vocabulário, sendo o primeiro item o prefixo.
    :return: str - string com o prefixo seguido pelas palavras com o prefixo aplicado,
                    separadas por ' :: '.

    Esta função recebe uma lista `vocab_words` e retorna uma string no formato:
    'prefixo :: prefixopalavra1 :: prefixopalavra2 :: ...'.

    Por exemplo: ['en', 'close', 'joy', 'lighten']
    produz a string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefixo = vocab_words[0]
    palavras_com_prefixo = [prefixo + palavra for palavra in vocab_words[1:]]
    return " :: ".join([prefixo] + palavras_com_prefixo)


def remove_suffix_ness(word):
    """Remove o sufixo 'ness' da palavra, ajustando a ortografia quando necessário.

    :param word: str - palavra da qual o sufixo será removido.
    :return: str - palavra sem o sufixo 'ness' e com ajuste ortográfico, se aplicável.

    Por exemplo: "heaviness" se torna "heavy", e "sadness" se torna "sad".
    """

    if word.endswith("ness"):
        raiz = word[:-4]  # Remove os 4 caracteres finais: 'ness'
        # Se a raiz terminar com 'i', troca por 'y' (ex: 'heavi' → 'heavy')
        if raiz.endswith("i"):
            return raiz[:-1] + "y"
        else:
            return raiz
    return word  # Retorna a palavra original se não terminar com 'ness'


def adjective_to_verb(sentence, index):
    """Transforma um adjetivo extraído de uma frase em um verbo.

    :param sentence: str - frase que contém a palavra a ser transformada.
    :param index: int - índice da palavra na frase que será transformada.
    :return: str - verbo formado a partir do adjetivo, geralmente com o sufixo 'en'.

    Por exemplo: ("It got dark as the sun set.", 2) retorna "darken".
    """

    # Remove espaços em branco no início e no fim
    frase_limpa = sentence.strip()
    # Remove pontuação final comum (., !, ?, etc.)
    if frase_limpa and frase_limpa[-1] in ".,!?;":
        frase_limpa = frase_limpa[:-1]

    palavras = frase_limpa.split()
    adjetivo = palavras[index].strip()

    # Transforma o adjetivo em verbo adicionando 'en'
    return adjetivo + "en"