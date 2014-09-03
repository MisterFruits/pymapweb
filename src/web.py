from bottle import Bottle, run, view, static_file
import pymap

app = Bottle()

@app.route('/bootstrap/<filepath:path>')
def bootstrap_static(filepath):
    return static_file(filepath, root='../resources/bootstrap/')

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='../resources/html_static/')

@app.route('/')
@app.route('/:username/:account')
@view('main')
def main(username = '', account = ''):
    context = dict()
    context['accounts'] = [pymap.get_random_account() for el in range(4)]
    return context

@app.route('/test2')
@view('main')
def test2(name = ''):
    return dict()

run(app, host='localhost', port=8080, debug=True, reloader=True)
