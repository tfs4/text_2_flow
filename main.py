import demo
from additional_viz import viz


if __name__ == '__main__':
    texto = '''
    joão se casou com maria em março de 2020, o casal optou por união estável de bens, três anos depois o casal se mudou para a cobertura de frente para a praia de copacabana de joão, em março de 2022 nasceu josé, primeiro filho do casal, três anos depois o casal decidiu se separar, agora joão terá que pagar uma pensão de cinco mil reais para maria
    '''

    titulo = 'teste'



    example1 = {titulo: texto}


    extraction_df, decision_words = demo.text_to_flowchart(example1)
    #demo.flowchart_generate(extraction_df, decision_words, 'Caso de João e Maria')