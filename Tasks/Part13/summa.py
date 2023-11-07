from flask import Flask, request

app = Flask(__name__)
@app.route("/summa/<num>")
def summa():
    args = request.args
    num = float(args.get("num"))
    l = []
    for i in range(num):
        if not (num % i): l.append(i)
        i += 1

    return len(l) == 2

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
