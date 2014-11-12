from bottle import Bottle, run, view, static_file, template
import pymap, test_pymap

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
    accounts = [test_pymap.get_random_account() for el in range(4)]
    return dict(accounts=accounts, selectedaccount=accounts[2])

@app.route('/test2')
@view('main')
def test2(name = ''):
    return dict()

# @app.route('/hello')
# @app.route('/hello/<name>')
@view('test2')
def hello(name='World'):
    return dict(name=name)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
