from flask import Flask, request, jsonify
app = Flask(__name__)

seed = 100

@app.route('/',methods = ['POST'])
def update_seed():
   global seed
   data = request.get_json()
   seed = data["num"]
#    seed = data.get('num', seed)
   return "success"

@app.route('/',methods = ['GET'])
def get_seed():
    return jsonify(seed=seed)

if __name__ == '__main__':
   app.run(debug = True, port=5003, host='0.0.0.0')