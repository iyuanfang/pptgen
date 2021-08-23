from flask import Flask
import os.path
from flask_autoindex import AutoIndex
from flask import render_template,request,url_for, redirect
from gen_ppt import *
import time

app = Flask(__name__)
AutoIndex(app, browse_root=os.path.curdir+"\\gen")

@app.route("/gen_file",methods=['post'])
def genfile():
    file_name=request.form.get("file_name")
    file_content=request.form.get("file_content")
    file_content=file_content.replace('\r','')
    ppt_txt=open('gen/'+file_name+".txt","w",encoding="utf-8")
    ppt_txt.write(file_content)
    ppt_txt.close()
    gen(file_name)
    return redirect('/')

@app.route("/edit")
@app.route("/edit/<file_name>")
def editfile(file_name=''):
    file_content=''
    if file_name =='':
        file_name='first' #载入模板
    file_content=open('gen/'+file_name+".txt","r",encoding="utf-8").read()
    return render_template('edit_file.html',file_name=file_name,file_content=file_content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)