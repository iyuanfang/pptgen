from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>生成文件列表：</h1>"

@app.route("/genfile/")
def genfile():
    return "<h1>生成文件列表1：</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000,debug=True)