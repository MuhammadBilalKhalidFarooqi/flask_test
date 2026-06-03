from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<i><b>hello uncle</b> This is homepage</i>'

@app.route('/user_login', methods = ['POST', 'GET'])
def my_login():
    my_client_data = request.get_json()
    if request.method == 'POST':
        try:
            result = int(my_client_data) + 100
            return jsonify({'status': 'Mission Successful', 'got this:' : result, 'request': 'POST'})
        except:
            return 'big big error bara wala error aya tha!!'
        
    elif request.method == 'GET':
        try:
            return jsonify({'status': 'Mission Successful', 'take this' : my_client_data, 'request': 'GET'})
        except :
            return 'an error, I am sorry for it!!'


@app.route('/<usr>')
def my_user(usr):
    
    return f'<i>You said:<b>{usr}</b> </i>'

if __name__ == "__main__":

   app.run(port=9574, host='192.168.1.15', debug=True)