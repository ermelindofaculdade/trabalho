"""Funções para organizar e calcular as notas dos alunos em provas."""


def round_scores(student_scores):
    """Arredonda todas as notas fornecidas dos alunos.

    :param student_scores: list - lista de notas (float ou int) dos alunos.
    :return: list - lista de notas arredondadas para o inteiro mais próximo.
    """

    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Conta o número de alunos reprovados no grupo fornecido.

    :param student_scores: list - lista de notas inteiras dos alunos.
    :return: int - quantidade de alunos com nota menor ou igual a 40.
    """

    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Determina quantas das notas fornecidas estão entre as melhores, com base no limite (threshold).

    :param student_scores: list - lista de notas inteiras.
    :param threshold: int - valor mínimo para ser considerado uma nota "excelente".
    :return: list - lista de notas que são maiores ou iguais ao limite.
    """

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Cria uma lista de limites inferiores para cada faixa de nota por conceito (D, C, B, A).

    :param highest: int - valor da nota máxima da prova.
    :return: list - lista com os limites inferiores para D, C, B e A.

    Exemplo: se a nota máxima for 100 e a nota mínima para aprovação for 41 (ou seja, <=40 = reprovado),
    então o intervalo útil é de 41 a 100 (60 pontos). Dividimos esse intervalo em 4 partes iguais.

    Com highest = 100:
        intervalo = (100 - 40) // 4 = 15
        D: 41 a 55  → limite inferior = 41
        C: 56 a 70  → limite inferior = 56
        B: 71 a 85  → limite inferior = 71
        A: 86 a 100 → limite inferior = 86

    Resultado: [41, 56, 71, 86]
    """

    interval = (highest - 40) // 4
    return [41 + i * interval for i in range(4)]


def student_ranking(student_scores, student_names):
    """Organiza o ranking, nome e nota dos alunos em ordem decrescente de desempenho.

    :param student_scores: list - lista de notas em ordem decrescente.
    :param student_names: list - lista de nomes correspondentes, também em ordem decrescente por nota.
    :return: list - lista de strings no formato ["<posição>. <nome>: <nota>"].
    """

    return [
        f"{rank}. {name}: {score}"
        for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1)
    ]


def perfect_score(student_info):
    """Retorna o nome e a nota do primeiro aluno que tirou nota perfeita (100).

    :param student_info: list - lista de listas no formato [<nome do aluno>, <nota>].
    :return: list - primeira sublista [<nome>, 100] encontrada, ou [] se ninguém tirou 100.
    """

    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []