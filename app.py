from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

screens = [
    {'id': 0,
     'name': 'Screen 1',
     'status': 'Down'},
    {'id': 1,
     'name': 'Screen 2',
     'status': 'Down'},
    {'id': 2,
     'name': 'Screen 3',
     'status': 'Down'}
]

@app.route('/api/v1/screens/all', methods=['GET'])
def api_all():
    return jsonify(screens)

@app.route('/api/v1/screens/add', methods=['POST'])
def api_add():
    if request.method == 'POST':

        screens.append(request.get_json())
        return "Done"

@app.route('/api/v1/screens/update', methods=['POST'])
def api_update():
    if request.method == 'POST':

        request_data = request.get_json()
        updateId = request_data['id']
        updateName = request_data['name']
        updateStatus = request_data['status']

        d = next(item for item in screens if item['id'] == updateId)
        d['name'] = updateName
        d['status'] = updateStatus

        return "Done"

app.run(debug=True)
