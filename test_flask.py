from flask import Flask

app = Flask(__name__)

@app.route('/homa')
def homepage():
    return '<i><b>hello uncle</b></i>'

@app.route('/products')
def my_products():
    return '<b>Products wala page</b></i>!!!!'


if __name__ == "__main__":

   app.run(port=9574, host='192.168.1.15')