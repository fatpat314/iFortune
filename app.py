from flask import Flask, render_template

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
    users_favorite_animal = request.args.get('animal')
    print("hello")

    if users_favorite_animal == 'unicorn':
        print("fortune is You'll have  magical day!")
    
    elif condition2:
        pass
    elif condition3:
        pass
    elif condition4:

        # no other fortune applies. return default fortune
        pass

        return render_template('fortune_results.html')
