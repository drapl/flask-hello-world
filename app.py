from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',screensVar=screens)

screens = [
    {'id': 0,
     'name': 'Screen 1',
     'status': 'Down'},
    {'id': 1,
     'name': 'Screen 2',
     'status': 'Down'},
    {'id': 2,
     'name': 'Screen 3',
     'status': 'Down'},
    {'id': 3,
     'name': 'Screen 4',
     'status': 'Down'},
    {'id': 4,
     'name': 'Screen 5',
     'status': 'Down'},
    {'id': 5,
     'name': 'Screen 6',
     'status': 'Down'},
    {'id': 6,
     'name': 'Screen 7',
     'status': 'Down'},
    {'id': 7,
     'name': 'Screen 8',
     'status': 'Down'}
]
    


@app.route('/api/v1/screens/all', methods=['GET'])
def api_all():
    return jsonify(screens)

@app.route('/api/v1/screens/add', methods=['POST'])
def api_add():
    if request.method=='POST':
        addId = request.args['id']
        addName = request.args['name']
        addStatus = request.args['status']
        addDict = {'id':id,'name': addName,'screen':addStatus}
        screens.append(addDict)


app.run()
