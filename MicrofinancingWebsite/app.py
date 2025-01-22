from flask import Flask, render_template, request

app = Flask(__name__)

# Set the interest rate for compound interest
INTEREST_RATE = 0.22  # 22% annually

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    amount = float(request.form["amount"])
    duration = int(request.form["duration"])

    # Compound interest formula: A = P(1 + r)^t
    total_amount = amount * (1 + INTEREST_RATE) ** duration

    return render_template("result.html", first_name=first_name, last_name=last_name, amount=amount, duration=duration, total_amount=total_amount)

if __name__ == "__main__":
    app.run(debug=True)
