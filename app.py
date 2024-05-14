from flask import Flask
app = Flask(__name__)

ls_name = 'Welcome...Manickam Vijayabanu'
ls_address = '221 Fannin'
print(ls_name)

@app.route("/")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework!"

