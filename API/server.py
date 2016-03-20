from flask import Flask
from flask import Response
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<country>')
def profile(country): 
    if(country == 'SL'):
	    return Response(str([[0.40,0.53,0.7,0.19,0.4,0.8,0.6,0.4,0.66,0.54,0.11,0.56,0.4,0.6,0.99,0.77],
[0.34,0.43,0.57,0.1,0.25,0.68,0.54,0.25,0.51,0.44,0.0,0.46,0.35,0.55,0.8,0.63],
[0.24,0.35,0.41,0.05,0.17,0.49,0.41,0.15,0.41,0.34,0.0,0.36,0.27,0.45,0.75,0.56],
[0.14,0.23,0.27,0.00,0.10,0.38,0.24,0.05,0.21,0.14,0.0,0.16,0.10,0.30,0.69,0.15]]), mimetype='text/json')

if __name__ == "__main__":
    app.debug = True
    app.run()

	# data = {
	# 	'IN':{
	# 		"--": 
	# 		"Up": 
	# 		"Mh": 
	# 		"Bi": 
	# 		"Wb": 
	# 		"Mp": 
	# 		"Tn": 
	# 		"Rj": 
	# 		"Ka": 
	# 		"Gj": 
	# 		"Ap": 
	# 		"Od": 
	# 		"Ts": 
	# 		"Kl": 
	# 		"Jk": 
	# 		"As": 
	# 		"Pn": 
	# 		"Ch": 
	# 		"Hr": 
	# 		"Jk": 
	# 		"Uk": 
	# 		"Hp": 
	# 		"Tr": 
	# 		"Mg": 
	# 		"Mn": 
	# 		"Ng": 
	# 		"Ga": 
	# 		"Ar": 
	# 		"Mz": 
	# 		"Sk": 
	# 		"Dl": 
	# 	},

	# 	'PK':{
	# 		"--": 
	# 		"Ba": 
	# 		"Kh": 
	# 		"Pu": 
	# 		"Si": 
	# 		"Ca": 
	# 		"Tr": 
	# 		"Az": 
	# 		"Gi": 
	# 	},

	# 	'SL':{
	# 		'--': 
	# 		'Bm': 
	# 		'Ko': 
	# 		'Po': 
	# 		'To': 
	# 		'Ka': 
	# 		'Ke': 
	# 		'Kn': 
	# 		'Kl': 
	# 		'Bo': 
	# 		'Bn': 
	# 		'Pu': 
	# 		'Mo': 
	# 		'Wu': 
	# 		'Wr': 
	# 	}
	# }
	