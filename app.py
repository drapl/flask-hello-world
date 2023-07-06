from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

screens = [
    {'id': 0,
     'name': 'Screen 1',
     'status': 'Down'},
    {id: 1,
     'name': 'Screen 2',
     'status': 'Down'},
    {id: 2,
     'name': 'Screen 3',
     'status': 'Down'}
]

@app.route('/api/v1/screens/all', methods=['GET'])
def api_all():
    return jsonify(screens)

app.run()
