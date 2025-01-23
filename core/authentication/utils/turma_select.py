def select_course_by_turma(turma: str) -> str:
    """
    Retorna o curso associado à turma fornecida.

    :param turma: A turma para a qual o curso será determinado.
                  (tipo 'str')
    :return: O curso associado à turma fornecida. 
             Retorna uma string que indica o curso correspondente.
    """
    CURSO_MAPPING = {
        'info': 'informatica',
        'agro': 'agropecuaria',
        'quimi': 'quimica'
    }

    for curso_prefix, curso_name in CURSO_MAPPING.items():
        if curso_prefix in turma:
            return curso_name
            
    raise ValueError(f"Turma '{turma}' não encontrada.")
