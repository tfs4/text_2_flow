import demo
from additional_viz import viz


if __name__ == '__main__':
    texto = '''
    João e maria se casaram em março de 2020, o casal optou por união estável de bens, três anos depois o casal se mudou para a cobertura de frente para a praia de 
    copacabana de joão, em março de 2022 nasceu josé, primeiro filho do casal, três anos depois o casal decidiu se separar, agora joão terá que pagar uma pensão 
    de cinco mil reais para maria, o juiz decidiu que joão tem que pagar 10 mil reais de penção
    '''

    titulo = 'teste'



    example1 = {titulo: texto}


    extraction_df = demo.text_to_flowchart(example1)
    demo.flowchart_generate(extraction_df, 'Caso de João e Maria')