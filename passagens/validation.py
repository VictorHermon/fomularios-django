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


def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """
    Verifica se a data de ida é maior do que a data de volta
    :param data_ida:
    :param data_volta:
    :param lista_de_erros:
    :return:
    """
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida'


def data_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """
    Verificar se a data de ida é menor que a data de hoje
    :param data_ida:
    :param data_pesquisa:
    :param lista_de_erros:
    :return:
    """
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que hoje'
