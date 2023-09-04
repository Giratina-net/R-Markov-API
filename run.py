import json
import gen
from flask_cors import CORS
from flask import Flask,Response

app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/')
def index():
    return Response(json.dumps({}), status=200, mimetype='application/json')

@app.route('/v1/raika', methods=['GET'])
def api():
    raika = gen.run()

    if raika == False:
        return Response(json.dumps({"error":"generate error"}), status=400, mimetype='application/json',content_type='application/json; charset=utf-8')
    
    else:
        return Response(json.dumps({"text":raika},ensure_ascii=False), status=200, mimetype='application/json',content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(port=5000,host="0.0.0.0")