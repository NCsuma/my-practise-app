from flask import Flask, render_template,url_for
from BirdItem import BirdItem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/birds')
def display_birdimage():
    item1 = BirdItem ("Scarlet Tanager","images/Bird1.jpg")
    item2 = BirdItem("Kiwi", "images/Bird2.jpg")
    item3 = BirdItem("Peacock", "images/Bird3.jpg")
    item4 = BirdItem("Rose Crowned Fruit Dove", "images/Bird4.jpg")
    item5 = BirdItem("Barn Owl", "images/Bird5.jpg")
    item6 = BirdItem("Woodpecker", "images/Bird6.jpg")

    birdsgroup1 = [item1,item2,item3]
    birdsgroup2 = [item4,item5,item6]

    return render_template('birds.html',birdsgroup1 = birdsgroup1, birdsgroup2 = birdsgroup2)

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
