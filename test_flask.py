from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<i><b>hello uncle</b>This is homepage</i>'

@app.route('/products')
def my_products():
    return '<b>Products wala page</b></i>!!!!'


if __name__ == "__main__":

   app.run(port=9574, host='192.168.1.15')