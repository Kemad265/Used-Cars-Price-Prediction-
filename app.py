from flask import Flask, render_template, request
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
app = Flask(__name__)
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
le5 = LabelEncoder()
le6 = LabelEncoder()
le7 = LabelEncoder()
le8 = LabelEncoder()
le9 = LabelEncoder()
le10 = LabelEncoder()
le11 = LabelEncoder()
le1 = joblib.load('encoding1.joblib')
le2 = joblib.load('encoding2.joblib')
le3 = joblib.load('encoding3.joblib')
le4 = joblib.load('encoding4.joblib')
le5 = joblib.load('encoding5.joblib')
le6 = joblib.load('encoding6.joblib')
le7 = joblib.load('encoding7.joblib')
le8 = joblib.load('encoding8.joblib')
le9 = joblib.load('encoding9.joblib')
le10 = joblib.load('encoding10.joblib')
le11 = joblib.load('encoding11.joblib')
model = joblib.load('model.h5')
scaler = joblib.load('scale.h5')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict():
    user_input =list()
    user_input.append(request.args.get('Year'))
    user_input.append(request.args.get('manufacturer'))
    user_input.append(request.args.get('model'))
    user_input.append(request.args.get('condition'))
    user_input.append(request.args.get('cylinders'))
    user_input.append(request.args.get('fuel'))
    user_input.append(request.args.get('odometer'))
    user_input.append(request.args.get('Title_status'))
    user_input.append(request.args.get('transmission'))
    user_input.append(request.args.get('drive'))
    user_input.append(request.args.get('size'))
    user_input.append(request.args.get('type'))
    user_input.append(request.args.get('paint'))
    user_input[1]=le1.transform([user_input[1]])[0]
    user_input[2]=le2.transform([user_input[2]])[0]
    user_input[3]=le3.transform([user_input[3]])[0]
    user_input[4]=le4.transform([user_input[4]])[0]
    user_input[5]=le5.transform([user_input[5]])[0]
    user_input[7]=le6.transform([user_input[7]])[0]
    user_input[8]=le7.transform([user_input[8]])[0]
    user_input[9]=le8.transform([user_input[9]])[0]
    user_input[10]=le9.transform([user_input[10]])[0]
    user_input[11]=le10.transform([user_input[11]])[0]
    user_input[12]=le11.transform([user_input[12]])[0]
    user_input = [int(n) for n in user_input]
    profit = model.predict(scaler.transform([user_input]))[0]
    return render_template('index.html', profit=profit)
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')