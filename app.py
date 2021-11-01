from flask import Flask,session
import os
from flask_autoindex import AutoIndex
from flask import render_template,request,url_for, redirect
from gen_ppt import *
from db import *
import time

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
AutoIndex(app, browse_root=os.path.curdir+"\\gen")

@app.route("/gen_file",methods=['post'])
def gen_file():
    user=session.get('user')
    file_name=request.form.get("file_name")
    file_content=request.form.get("file_content")
    file_content=file_content.replace('\r','')
    ppt_txt=open('gen\\users\\'+user+'\\'+file_name+".txt","w",encoding="utf-8")
    ppt_txt.write(file_content)
    ppt_txt.close()
    gen('gen/users/'+user+'/',file_name)
    return redirect("/users/"+user)

@app.route("/gen")
@app.route("/gen/<file_name>")
@app.route("/gen/my/<my_file_name>")
def genfile(file_name='',my_file_name=''):
    user=session.get('user')
    if user==None:
        return redirect('/login')
    file_content=''
    if file_name !='':
        file_content=open('gen\\templates\\'+file_name+".txt","r",encoding="utf-8").read()
    if my_file_name !='':
        file_content=open('gen\\users\\'+user+'\\'+my_file_name+".txt","r",encoding="utf-8").read()
        file_name=my_file_name
    return render_template('gen_file.html',file_name=file_name,file_content=file_content)

@app.route("/regist",methods=['post'])
def regist():
    email=request.form.get("email")
    user=email.split("@")[0]
    pwd=request.form.get("pwd")
    execute_db("insert into users(email,pwd) values ('"+email+"','"+pwd+"')")
    user_folder='gen\\users\\'+user
    if not os.path.exists(user_folder): #创建用户目录
        os.mkdir(user_folder)
    session['user'] = user #存入session
    return redirect("/gen")

@app.route("/help",methods=['get'])
def help():
    return render_template('help.html')

@app.route("/regist",methods=['get'])
def regist_form():
    return render_template('regist.html')

@app.route("/login",methods=['get'])
def login_form():
    return render_template('login.html')

@app.route("/login",methods=['post'])
def login():
    email=request.form.get("email")
    pwd=request.form.get("pwd")
    print("select * from  users where email='"+email+"' and pwd='"+pwd+"'")
    u=query_db("select * from  users where email='"+email+"' and pwd='"+pwd+"'")
    user=email.split("@")[0]
    if u:
        session['user'] = user #存入session
        return redirect("/gen")
    else:
        return redirect("/login")

@app.route("/templates",methods=['get'])
def templates():
    user=session.get('user')
    if user==None:
        return redirect('/login')
    templates=[]
    my_templates=[]
    for file in os.listdir('gen\\templates'):
        templates.append(os.path.splitext(file)[0])
    for file in os.listdir('gen\\users\\'+user):
        if os.path.splitext(file)[1]=='.txt':
            my_templates.append(os.path.splitext(file)[0])
    return render_template('templates.html',templates=templates,my_templates=my_templates)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)