from flask import Flask
from flask import Response
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<country>')
def profile(country): 
    if(country == '--'):
        return Response(str({}), mimetype='text/json')    
    return Response(str([0.40,0.53,0.7,0.2,0.1]), mimetype='text/json')


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
	