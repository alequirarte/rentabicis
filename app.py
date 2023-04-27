
from passlib.hash import sha256_crypt
from flask import Flask, render_template, request, redirect, session

from funciones import lee_diccionario_csv,graba_diccionario_id, lee_diccionario_csv_id
import datetime
import random



archivo_usuarios = 'usuarios.csv'
archivo_citas = 'agenda.csv'
diccionario_usuarios = lee_diccionario_csv(archivo_usuarios)
diccionario_citas = lee_diccionario_csv_id(archivo_citas)





logeado = False
first_login = False
confirmacion = False
id = 0

lista_atencion = ['1 hora','2 horas','3 horas','4 horas','5 horas']

app = Flask(__name__)
app.secret_key = "klNmsS679SDqWpñl"

@app.route("/")
def index():
    
    if logeado == True or session.get('usuario') in diccionario_usuarios:
        return render_template("index.html")
    else:
        return render_template("index.html")
            


@app.route("/", methods=['GET','POST'])
def ingresar():
    logeado = False
    if "logged_in" in session:
        if session["logged_in"] == True:
            logeado = True

    if logeado == False:        
        if request.method == 'GET':
            msg = ''
            return render_template('/',mensaje=msg)
        else:
            if request.method == 'POST':
                usuario = request.form['usuario']

                if usuario in diccionario_usuarios:
                    password_db = diccionario_usuarios[usuario]['password'] # password guardado
                    password_forma = request.form['password'] #password presentado
                    verificado = sha256_crypt.verify(password_forma,password_db)
                    if (verificado == True):
                        session['usuario'] = usuario
                        session['logged_in'] = True
                        first_login = True
                        logeado = True
                        return render_template("index.html", first = first_login)
                    else:
                        msg = f'El password de {usuario} no corresponde'
                        return render_template('index.html',mensaje=msg)
                else:
                        msg = f'{usuario} no se encuentra registrado'
                        return render_template('index.html',mensaje=msg)
                    
    else:
        msg = 'YA ESTA LOGEADO'
        return render_template('index.html')
    

@app.route('/logout', methods=['GET','POST'])
@app.route('/logout/', methods=['GET','POST'])
def logout():

    if request.method == 'GET':
        session.clear()
        session["logged_in"] = False
        return redirect('/')
 
    


@app.route("/citas/", methods=['GET','POST'])
def citas():
     num = random.randint(1,50)
     if request.method == 'GET':
        hoy_completo = datetime.datetime.today()
        fecha_hoy  = datetime.datetime.strftime(hoy_completo,"%Y-%m-%d")
        
        return render_template("agendar.html", lista=lista_atencion, hoy=fecha_hoy)
     else:
        if request.method == 'POST':
            
            valor = request.form['enviar']
            if valor == 'Agendar':
                numbici =  num
                horas  =  request.form['horas']
                fecha    =  request.form['fecha']
                usuario =  session['usuario']
                diccionario_citas = lee_diccionario_csv_id(archivo_citas)
                id = len(diccionario_citas)
                if id not in diccionario_citas:
                        diccionario_citas[id] = {
                            'id': id,
                            'numbici': numbici,
                            'horas'  : horas,
                            'fecha': fecha,
                            'usuario':usuario
                        }
                id = id+1
                graba_diccionario_id(diccionario_citas,'id',archivo_citas)
                confirmacion = True
            return render_template("index.html", confi = confirmacion)


@app.route("/lista_citas/", methods=['GET'])
def lista_citas():
    if request.method == 'GET':
        dic_citas = lee_diccionario_csv_id(archivo_citas)
        return render_template("lista_agenda.html",dicc_citas=dic_citas)
      



if __name__ == "__main__":
    app.run(debug=True)
    session['logged_in'] = False