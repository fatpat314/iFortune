from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune aand weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune():
    return render_template('index.html')



@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""

    # NAME
    users_name = request.args.get('firstname')

    # SIBLIST
    users_siblist = request.args.get('siblist')

    if users_siblist == '0':
        sib_text = 'is an only child'

    elif users_siblist == '1':
        sib_text = 'has one sibling'

    elif users_siblist == '2':
        sib_text = 'has more siblings'

    else:
        sib_text = 'has a lot of siblings'

    # ANIMALS
    users_favorite_animal = request.args.get('animal')

    if users_favorite_animal == 'Unicorn':
        fortune_text = 'will have a magic day'

    elif users_favorite_animal == 'Narwal':
        fortune_text = 'is not a Unicorn'

    else:
        fortune_text = 'does not like horns'

    #San Francico
    users_cities = request.args.get('city1')

    # if users_cities == 'San Francico' and 'New York' and 'Austin':
    #     city_text = ' and has traveled a lot'

    if users_cities == 'San Francisco':
        city_text = ' and has been to San Francisco'
    else:
        city_text = ''
    #New York
    users_cities = request.args.get('city2')

    if users_cities == 'New York':
        city_text2 = ' and has been to New York'
    else:
        city_text2 = ''

    #Austin
    users_cities = request.args.get('city3')
    if users_cities == 'Austin':
        city_text3 = ' and Austin'
    else:
        city_text3 = ''

    if users_cities == None:
        city_text = ' and needs to get out more'
    # else:
    #     city_text = ' and needs to get out more.'


    return render_template('fortune_results.html', fortune_results = users_name + " " + fortune_text + ", " + sib_text + city_text + city_text2 + city_text3)
