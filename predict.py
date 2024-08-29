from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

'''
@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=['GET'])
def pinger():
    return "<p>Hello i am under water!</p>"

@app.route("/json", methods=['GET'])
def json_check():
    return {"message": "Hi i am json!"}
'''
model_pickle = open("./artefacts/classifier.pkl", "rb")
clf = pickle.load(model_pickle)

@app.route("/predict", methods=['POST'])
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 1
    else:
        Married = 0
    
    if loan_req['Credit_History'] == 'Unclear Debts':
        Credit_History = 0
    else:
        Credit_History = 1
    
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    #Credit_History = loan_req['Credit_History']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}

