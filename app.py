from flask import Flask


#create flask app

app = Flask(__name__)

# creating the first route for index page
@app.route("/")
def index():
    return f'homepage' 


if __name__=='__main__':
    app.run(debug=True)