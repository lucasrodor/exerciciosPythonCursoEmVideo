#faça um programa que tenha uma função notas() que pode receber várias 
#notas de alunos e vai retornar um dicionario com as seguintes informações
#- Quantidade de notas, Maior nota, Menor nota, Média da turmas, Situação (opcional)
#Adicione também as docstring

def notas ( *n, situação = False):
    """Função para analisar várias notas e situação da turma

    Args:
        n : notas dos alunos
        situação : valor opcional com a situação da turma

    Returns:
        retorna um dicionário com o resultado da análise
    """
    result = {}

    result['total'] = len(n)
    result['maior nota'] = max(n)
    result['menor nota'] = min(n)

    media = sum(n)/len(n)
    result['Média'] = media

    if media >= 7:
        situacao = 'BOA'
    elif media < 7 and media < 5:
        situacao = '+/-'
    else:
        situacao = 'RUIM'

    if situação:
        result['Situação'] = situacao
    return result



resp = notas(1,10,8,9,0,4, situação = True)
print(resp)
