def select_course_by_turma(turma: str) -> str:
    """
    Retorna o curso associado à turma fornecida.

    :param turma: A turma para a qual o curso será determinado.
                  (tipo 'str')
    :return: O curso associado à turma fornecida. 
             Retorna uma string que indica o curso correspondente.
    """
    if turma in ['1info1', '1info2', '1info3', '2info1', '2info2', '2info3', '3info1', '3info2', '3info3']:
        return 'informatica'
    elif turma in ['1agro1', '1agro2', '1agro3', '2agro1', '2agro2', '2agro3', '3agro1', '3agro2', '3agro3']:
        return 'agropecuaria'
    elif turma in ['1quimi', '2quimi', '3quimi']:
        return 'quimica'
    else:
        raise ValueError(f"Turma '{turma}' não encontrada.")
