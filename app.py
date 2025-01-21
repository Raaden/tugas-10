from flask import Flask, render_template, request
import math

app = Flask(__name__)

def binomial_probability(n, k, p):
    """
    Calculate binomial probability using the formula:
    P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
    Where C(n, k) = n! / (k! * (n-k)!)
    """
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        return num * factorial(num - 1)

    combination = factorial(n) / (factorial(k) * factorial(n - k))
    probability = combination * (p ** k) * ((1 - p) ** (n - k))
    return probability

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n = int(request.form['n'])  # Total number of trials
        k = int(request.form['k'])  # Number of successes
        p = float(request.form['p'])  # Probability of success in a single trial

        if not (0 <= p <= 1):
            return render_template('error.html', message="Probability 'p' must be between 0 and 1.")

        result = binomial_probability(n, k, p)
        return render_template('result.html', n=n, k=k, p=p, result=result)

    except ValueError:
        return render_template('error.html', message="Invalid input. Please enter numeric values for all fields.")

if __name__ == '__main__':
    app.run(debug=True)
