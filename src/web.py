from bottle import Bottle, run, view, static_file

app = Bottle()

@app.route('/bootstrap/<filepath:path>')
def bootstrap_static(filepath):
    return static_file(filepath, root='../resources/bootstrap/')

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='../resources/html_static/')

@app.route('/')
@app.route('/test')
@app.route('/test/:name')
@view('test')
def test(name = ''):
    return dict()

@app.route('/test2')
@view('main')
def test2(name = ''):
    return dict()

run(app, host='localhost', port=8080, debug=True, reloader=True)
