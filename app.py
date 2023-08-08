# web server
# step 1
from flask import Flask,render_template,request
import joblib
import numpy as np
import pandas as pd


app=Flask(__name__)
ml_reg=open('regression.pkl','rb')
ml_model=joblib.load(ml_reg)





@app.route('/')
def home():
    return render_template('home.html')




@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        try:
            # newyork=float(request.form['newyork'])
            # california=float(request.form['california'])
            # florida=float(request.form['florida'])
            newyork=0
            california=0
            florida=0
            state=request.form['state']
            if state=='New York':
                newyork=1
            if state=='California':
                california=1
            if state=='Florida':
                florida=1
            rdspend=float(request.form['spending1'])
            adminspend=float(request.form['spending2'])
            marketing=float(request.form['spending3'])

            pred_args=[newyork,california,florida,rdspend,adminspend,marketing]
            pred_args_arr=np.array(pred_args)
            pred_args_arr=pred_args_arr.reshape(1,-1)

            # ml_reg=open('regression.pkl','rb')
            # ml_model=joblib.load(mul_reg)

            model_prediction=ml_model.predict(pred_args_arr)
            model_prediction=round(float(model_prediction),2)


        except valueError:
            return 'check value again'

    return render_template('predict.html' , prediction=model_prediction)







if __name__=='__main__':
    app.run()    






'''
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

mul_reg = open("regression.pkl", "rb")
ml_model = joblib.load(mul_reg)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    print("I was here 1")
    if request.method == 'POST':
        print(request.form.get('NewYork'))
        try:
            NewYork = float(request.form['NewYork'])
            California = float(request.form['California'])
            Florida = float(request.form['Florida'])
            RnD_Spend = float(request.form['RnD_Spend'])
            Admin_Spend = float(request.form['Admin_Spend'])
            Market_Spend = float(request.form['Market_Spend'])
            pred_args = [NewYork, California, Florida, RnD_Spend, Admin_Spend, Market_Spend]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            # mul_reg = open("multiple_regression_model.pkl", "rb")
            # ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', prediction = model_prediction)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

'''


