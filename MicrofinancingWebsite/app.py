from flask import Flask, render_template, request

app = Flask(__name__)

# Interest rates based on loan type
INTEREST_RATES = {
    "Home Loan": 0.08,
    "Car Loan": 0.10,
    "Personal Loan": 0.13,
    "Bussiness Loan": 0.11
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    age = int(request.form["age"])
    profession = request.form["profession"]
    loan_type = request.form["reason"]
    amount = float(request.form["amount"])
    duration = int(request.form["duration"])

    # Get interest rate based on loan type
    interest_rate = INTEREST_RATES.get(loan_type, 0.22)  # Default to 22% if not found

    # Compound interest formula: A = P(1 + r)^t
    total_amount = amount * (1 + interest_rate) ** duration

    return render_template("result.html", first_name=first_name, last_name=last_name, age=age, profession=profession, amount=amount, duration=duration, total_amount=total_amount, loan_type=loan_type, interest_rate=interest_rate)

if __name__ == "__main__":
    app.run(debug=True)
