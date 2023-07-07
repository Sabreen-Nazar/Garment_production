
import pickle
from flask import Flask , request , app , jsonify ,url_for ,render_template
from flask_cors import cross_origin
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
#print("all imported")

app = Flask(__name__)
#print("app created")

# Load the model

model_gb = pickle.load(open("gradient_model.pkl","rb"))
scalar = pickle.load(open('scaling.pkl' , 'rb'))
#print("model created")


# dat = {
# 		"quarter": 0.00,
# 		"department": 1.00,
# 		"team": 9.00,
# 		"targeted_productivity": 0.70,
# 		"smv": 28.08,
# 		"wip": 872.00,
# 		"over_time": 6900.00,
# 		"incentive": 44.00,
# 		"idle_time": 0.00,
# 		"idle_men": 0.00,
# 		"no_of_style_change": 0.00,
# 		"no_of_workers": 57.50
# 	}



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform((np.array(list(data.values())).reshape(1,-1)))
    output=model_gb.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    #final_input=scalar.transform(np.array(data).reshape(1,-1))
    final_input=np.array(data).reshape(1,-1)
    print(final_input)
    output=model_gb.predict(final_input)[0]
    return render_template("home.html",prediction_text="The Garment production is :  {}".format(output))

if __name__=="__main__":
    app.run(debug=True)

# {
# 	"data": {
# 		"quarter": 0.00,
# 		"department": 1.00,
# 		"team": 9.00,
# 		"targeted_productivity": 0.70,
# 		"smv": 28.08,
# 		"wip": 872.00,
# 		"over_time": 6900.00,
# 		"incentive": 44.00,
# 		"idle_time": 0.00,
# 		"idle_men": 0.00,
# 		"no_of_style_change": 0.00,
# 		"no_of_workers": 57.50
# 	}
# }

