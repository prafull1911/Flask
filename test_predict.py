import pytest
from predict import app


@pytest.fixture
def client():
    return app.test_client()

def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE" : "Hi I am Pinging...!!!"}

def test_predict(client):
    test_data = {
    "Gender": "Male",
    "Married": "Married",
    "ApplicantIncome": 50000,
    "Credit_History": "Cleared Debts",
    "LoanAmount": 500
                    }
    resp = client.post('/predict',json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": 'Approved'}