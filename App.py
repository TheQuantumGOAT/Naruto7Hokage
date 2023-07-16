from flask import Flask,request,jsonify, send_file,render_template
import Controller
import test
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


@app.route("/", methods=['GET'])
def index():
    #return 'templates/index.html'
    file_path = 'templates/index.html'
    return render_template('index.html') 

@app.route("/web", methods=['POST'])
def inde():
    URL = request.json['url']
    json_file = {}
    json_file =  Controller.controller(URL)
    api_url = json_file['URL']
    return render_template('index2.html',api_url=api_url,jsonData =json_file['file'] ) 


@app.route("/API",methods= ['POST'])
def convert():
    environment_path = app.root_path
    return {"environment_path":environment_path}
    URL = request.json['URL']
    json_file ={}
    json_file = Controller.controller(URL)
    #json_file = test.fun(URL)

    return json_file
@app.route('/Server_storage/<filename>', methods=['GET'])
def get_file(filename):
    try:
        file_path = f'Server_storage/{filename}'
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e), 404