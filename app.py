import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template


app = Flask(__name__)
model = pickle.load(open(r'F:\final_proj\sc.pkl', 'rb'))
scale = pickle.load(open(r'F:\final_proj\model.pkl','rb'))

app = Flask(__name__)

@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
@app.route('/predict1',methods=["POST","GET"]) # rendering the html template
def predict() :
    return render_template("input.html")

@app.route('/predict',methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
    print("new")
    a=[]
    #name = request.form['name']
    #print(name)
    #a.append(name)
    # gender = request.form.get('gender')
    # a.append(gender)
    # age = request.form.get('age')
    # a.append(age)
    # sm_status = request.form.get('sm')
    # a.append(sm_status)
    # bp_status = request.form.get('bp')
    # a.append(bp_status)
    # hs_status = request.form.get('hs')
    # a.append(hs_status)
    # dia_status = request.form.get('dia')
    # a.append(dia_status)
    # dia_lev = request.form.get('dia_lev')
    # a.append(dia_lev)
    # chol = request.form.get('cho')
    # a.append(chol)
    # sys_bp = request.form.get('sysbp')
    # a.append(sys_bp)
    # dia_bp = request.form.get('diabp')
    # a.append(dia_bp)
    # bmi = request.form.get('bmi')
    # a.append(bmi)
    # hrt = request.form.get('hrt')
    # input_feature=[int(x) for x in request.form.values() ]
    input_feature = [int(request.form["gender"]),
                     int(request.form['age']),
                     int(request.form['sm']),
                     int(request.form['bp']),
                     int(request.form['hs']),
                     int(request.form['dia']),
                     int(request.form['dia_lev']),
                     int(request.form['cho']),
                     int(request.form['sysbp']),
                     int(request.form['diabp']),
                     int(request.form['bmi']),
                     int(request.form['hrt'])]

    
    # a.append(hrt)
    print(input_feature)
    
    
    # input_feature=[np.array(a)]
    # print(input_feature)
    #prediction = 0
    return render_template("output.html",prediction ="Loan wiil Not be Approved")

if __name__ == '__main__':
    app.run(debug=True)
