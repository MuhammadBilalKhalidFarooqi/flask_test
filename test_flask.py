from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<i><b>hello uncle</b> This is homepage</i>'

@app.route('/user_login', methods = ['POST', 'GET'])
def my_login():
    if request.method == 'POST':
        my_client_data = request.get_json()
        return jsonify({'status': 'Mission Successful', 'got this:' : my_client_data, 'request': 'POST'})
        
    elif request.method == 'GET':
        return jsonify({'status': 'Mission Successful', 'take this:' : "|PEACE AND LOVE|", 'request': 'GET'})


@app.route('/<usr>')
def my_user(usr):
    
    return f'<i>You said:<b>{usr}</b> </i>'

if __name__ == "__main__":

   app.run(port=9574, host='192.168.1.15')