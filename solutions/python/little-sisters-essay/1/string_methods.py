"""Funções para ajudar a editar redações usando manipulação de strings."""


def capitalize_title(title):
    """Converte a primeira letra de cada palavra no título para maiúscula, se necessário.

    :param title: str - string do título que precisa ser formatada no estilo título.
    :return: str - string do título com formatação de título (primeiras letras em maiúsculas).
    """

    return title.title()


def check_sentence_ending(sentence):
    """Verifica o final da frase para confirmar que há um ponto final.

    :param sentence: str - uma frase a ser verificada.
    :return: bool - retorna True se estiver corretamente pontuada com ponto final, False caso contrário.
    """

    return sentence.endswith('.')


def clean_up_spacing(sentence):
    """Verifica se não há espaços em branco no início e no fim da frase.

    :param sentence: str - uma frase a ser limpa de espaços no início e no final.
    :return: str - frase sem espaços extras no início ou no final.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Substitui uma palavra na frase fornecida por uma nova palavra.

    :param sentence: str - frase na qual as palavras serão substituídas.
    :param old_word: str - palavra a ser substituída.
    :param new_word: str - nova palavra que substituirá a antiga.
    :return: str - frase de entrada com as palavras novas no lugar das antigas.
    """

    return sentence.replace(old_word, new_word)