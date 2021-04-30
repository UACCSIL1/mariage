from flask import Flask,request,render_template
import numpy as np
app=Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    import joblib
    model=joblib.load('ModelTDCSIL1.ml')
    int_features=[float(i) for i in request.form.values()]
    final_features=[np.array(int_features)] 
    indexDateNaissance=[1,2,3,4,5,6]
    dateNaissance=np.delete(final_features,indexDateNaissance)
    import math
    dateNaissance=dateNaissance[0]
    dateNaissance=math.ceil(dateNaissance)
    indexAnnee=0
    features_model=np.delete(final_features,indexAnnee)
    features_model=np.array([features_model]).reshape(1,6)
    prediction=model.predict(features_model)
    Agepredit=round(prediction[0],1)
    x=math.ceil(Agepredit)
    output= x+dateNaissance
    return render_template('index.html',prediction_text='Vous devriez vous marier en {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    