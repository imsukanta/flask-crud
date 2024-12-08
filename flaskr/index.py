from flask import Blueprint,render_template,request,redirect,url_for,flash
from flaskr.models import User
from flaskr import db
from sqlalchemy import text
bp=Blueprint("index",__name__)

@bp.route("/",methods=['GET',"POST"])
def index():
    if request.method=='POST':
        if request.form['name']!="" and request.form["email"]!="" and request.form['address']!="":
            user=User(name=request.form['name'],email=request.form["email"],address=request.form['address'])
            db.session.add(user)
            db.session.commit()
            flash("Data added successfully😊","success")
            return redirect(url_for('index.index'))
        else:
            flash("You must fill all the form")
    else:
        print("not allowed")
    try:
        users=db.session.execute(db.select(User)).scalars()
    except:
        flash("Sorry can't fetch data")
    return render_template("index.html",users=users)

@bp.route("/delete/<int:id>")
def delete(id):
    try:
        user=db.get_or_404(User,id)
        db.session.delete(user)
        db.session.commit()
    except:
        pass
    return redirect(url_for('index.index'))

@bp.route('/update/<int:id>',methods=["POST","GET"])
def update(id):
    user=db.get_or_404(User,id)
    if request.method=="POST":
        if request.form['uname'] and request.form['uemail'] and request.form['uaddress']:
            user.name=request.form['uname']
            user.email=request.form['uemail']
            user.address=request.form['uaddress']
            db.session.commit()
        else:
            flash("You must fill",'warning')
        return redirect(url_for('index.index'))
    return render_template('update.html',user=user)