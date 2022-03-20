def origem_destino_iguais(origem, destino, lista_de_errros):
    """
    Verifica sem a origem e o destino são iguais
    :param origem:
    :param destino:
    :param lista_de_errros:
    :return:
    """
    if origem == destino:
        lista_de_errros['destino'] = 'Origem e destino não podem ser iguais'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """
    Verifica se possui algum digito numero no campo informado
    :param valor_campo:
    :param nome_campo:
    :param lista_de_erros:
    :return:
    """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'
