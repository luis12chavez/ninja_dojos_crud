from flask import render_template,redirect,request,session

from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def main_pg():
    dojos = Dojo.show_all()
    print(dojos)
    return render_template('/dojos.html', dojos = dojos)

@app.route('/dojos', methods = ['POST'])
def add_dojo():
    data = {
        "name" : 
    }
    Dojo.create_dojo(data)
    return redirect('/')