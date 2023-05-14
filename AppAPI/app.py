#librerias
import flask

#declaracion de objetos
app = flask.Flask(__name__)

#declaracion de funciones
@app.route('/')
def home():
    return "<p>Que mira?</p>"

@app.route('/funcion1',methods=['GET','POST'])
def funcionApi1():
    if flask.request.method == 'POST':
        return "<p>POST</p>"
    else:
        return "<p>GET</p>"

#declaracion del main
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
