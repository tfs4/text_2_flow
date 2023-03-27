from demo import text_to_flowchart
from additional_viz import viz


if __name__ == '__main__':
    texto = '''
     Se você optar por infundir chá de folhas soltas, precisará de um infusor de chá. Encha o infusor com a quantidade de chá especificada na embalagem para quantas porções você precisa. Leve água fresca e fria para ferver. Depois de ferver, despeje sobre o infusor de chá (ou abaixe o infusor na panela) e deixe em infusão de acordo com o tempo acima com base na sua variedade de chá. Remova o infusor de chá da xícara ou bule.
     Se desejar, finalize com leite, separar de João adoçante de sua preferência ou uma rodela de frutas cítricas.
    '''

    titulo = 'teste'



    example1 = {titulo: texto}


    text_to_flowchart(example1)