from flask import Flask, render_template, request, redirect

from divers import Diver

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/divers')


@app.route('/divers')
def divers():
    return render_template("divers.html",divers=Diver.get_all())


@app.route('/diver/new')
def new():
    return render_template("new_diver.html")

@app.route('/diver/create',methods=['POST'])
def create():
    print(request.form)
    Diver.save(request.form)
    return redirect('/divers')


if __name__=="__main__":
    app.run(debug=True)