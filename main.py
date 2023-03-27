from demo import text_to_flowchart
from additional_viz import viz


if __name__ == '__main__':
    text1 = '''
    If you choose to steep loose-leaf tea, you'll need a tea infuser.

    Fill the infuser with the amount of tea specified on the package for how many servings you need.
    Bring fresh, cold water to a rolling boil.
    Once boiling, pour over the tea infuser (or lower the infuser into the pot) and steep according to the timing above based on your tea variety.
    Remove the tea infuser from the cup or pot.
    If desired, finish with milk, your preferred sweetener, or a slice of citrus.
    '''

    text1_title = 'teste'



    example1 = {text1_title: text1}


    text_to_flowchart(example1)