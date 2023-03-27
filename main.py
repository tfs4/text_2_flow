from demo import text_to_flowchart
from additional_viz import viz


if __name__ == '__main__':
    # https://www.allrecipes.com/article/how-to-make-tea/#:~:text=Bring%201%20cup%20of%20fresh,the%20tea%20bags%20or%20infuser.
    text1 = '''
    If you choose to steep loose-leaf tea, you'll need a tea infuser.

    Fill the infuser with the amount of tea specified on the package for how many servings you need.
    Bring fresh, cold water to a rolling boil.
    Once boiling, pour over the tea infuser (or lower the infuser into the pot) and steep according to the timing above based on your tea variety.
    Remove the tea infuser from the cup or pot.
    If desired, finish with milk, your preferred sweetener, or a slice of citrus.
    '''

    text1_title = 'How to Make Loose-leaf Tea'

    # chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://assets.press.princeton.edu/chapters/s012_8215.pdf
    text2 = '''
    The steps of the modeling process are as follows:
    Analyze the problem. We must first study the situation sufficiently to identify the problem pre cisely and understand its fundamental questions clearly. ...
    Formulate a model. ...
    Solve the model. ...
    Verify and interpret the model's solution. ...
    Report on the model. ...
    Maintain the model.
    '''
    text2_title = 'How to Build a Machine Learning Model'

    text3 = '''
    Step 1: Pick a Time for Journaling. ...
    Step 2: Select a Topic to Write About. ...
    Step 3: Journal for a Pre-determined Period. ...
    Step 4: Don't Stop To Edit. ...
    Step 5: Explore Your Thinking. ...
    Step 6: Stop and Tidy Up. ...
    Step 7: Review Your Journal Entries Regularly.
    '''
    text3_title = 'How to Write a Journal'

    # https://www.socialtables.com/blog/event-planning/party-planning-checklist/

    text4 = '''
    Choose a theme. ...
    Determine your budget. ...
    Choose a few date and time options for the event. ...
    Book an event venue. ...
    Arrange entertainment. ...
    Make a guest list. ...
    Order supplies if you're making your own decor.
    '''
    text4_title = 'How to Plan a Party'

    example1 = {text1_title: text1}
    example2 = {text2_title: text2}
    example3 = {text3_title: text3}
    example4 = {text4_title: text4}

    text_to_flowchart(example1)