from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<i><b>hello uncle</b>This is homepage</i>'

@app.route('/user_login', methods = ['POST', 'GET'])
def my_login():
    if request.method == 'POST':
        return f'<i>You said: <b> POST </b> </i>'
        
    elif request.method == 'GET':
        return f'<i>You said: <b> GET </b> </i>'


@app.route('/<usr>')
def my_user(usr):
    
    return f'<i>You said:<b>{usr}</b> </i>'

if __name__ == "__main__":

   app.run(port=9574, host='192.168.1.15')