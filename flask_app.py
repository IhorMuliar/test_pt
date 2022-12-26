from flask import Flask
app = Flask(__name__)
 
@app.route('/')
@app.route('/home')
def functionAS(n=3):
    commonDifference = 3
    firstTerm = 4
    sumOfTerms = 0
    for i in range(1, n + 1):
        ithTerm = firstTerm + (i - 1) * commonDifference
        sumOfTerms = sumOfTerms + ithTerm
    return sumOfTerms
 
if __name__ == '__main__':
    app.run(debug=True)