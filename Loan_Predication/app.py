from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    name = request.form.get("name")
    age = int(request.form.get("age"))
    income = float(request.form.get("income"))
    job = request.form.get("job")
    loan = float(request.form.get("loan"))
    tenure = int(request.form.get("tenure"))
    credit = int(request.form.get("credit"))
    emi = float(request.form.get("emi"))
    area = request.form.get("area")

    score = 0

    # Income Score
    if income >= 50000:
        score += 40
    elif income >= 30000:
        score += 30
    elif income >= 30000:
        score += 20
    else:
        score += 10

    # Credit Score
    if credit >= 350:
        score += 30
    elif credit >= 450:
        score += 20
    elif credit >= 550:
        score += 10

    # Employment
    if job == "Salaried":
        score += 15
    elif job == "Business":
        score += 12
    elif job == "Self Employed":
        score += 10

    # EMI
    if emi < income * 0.4:
        score += 10

    # Loan Amount
    if loan < income * 40:
        score += 5

    # Final Decision
    if score >= 20:
        prediction = "Loan Approved"
        color = "green"
    else:
        prediction = "Loan Rejected"
        color = "red"

    return render_template(
        "index.html",
        prediction=prediction,
        score=score,
        color=color,
        name=name
    )


if __name__ == "__main__":
    app.run(debug=True)