from demo import text_to_flowchart
from additional_viz import viz


if __name__ == '__main__':
    text1 = '''
     Se você optar por infundir chá de folhas soltas, precisará de um infusor de chá. Encha o infusor com a quantidade de chá especificada na embalagem para quantas porções você precisa. Leve água fresca e fria para ferver. Depois de ferver, despeje sobre o infusor de chá (ou abaixe o infusor na panela) e deixe em infusão de acordo com o tempo acima com base na sua variedade de chá. Remova o infusor de chá da xícara ou bule.
     Se desejar, finalize com leite, adoçante de sua preferência ou uma rodela de frutas cítricas.
    '''

    text1_title = 'teste'



    example1 = {text1_title: text1}


    text_to_flowchart(example1)