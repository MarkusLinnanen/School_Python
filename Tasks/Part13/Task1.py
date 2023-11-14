from flask import Flask, request

app = Flask(__name__)
@app.route("/prime/<num>")
def prime(num):
    l = []
    n = int(num)
    for i in range(n):
        if (n % (i + 1)) == 0: l.append(i)

    return {"number":n, "isPrime" : len(l) <= 2}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
