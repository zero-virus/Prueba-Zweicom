from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/post', methods=['POST'])
def post():
	print(request.is_json)
	content = request.get_json()
	ant = 0
	pres = 1
	for x in range(content['n']-1):
		act = ant + pres
		ant = pres
		pres = act
	print(ant)
	print(pres)
	resp = {'n-1': ant,'n':act}
	rjson = json.dumps(resp)
	return rjson

app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(debug=True)


