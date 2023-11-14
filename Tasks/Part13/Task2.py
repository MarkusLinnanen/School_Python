from flask import Flask, request
import mysql.connector

cnx = mysql.connector.connect(user='userguy', password='pw0rd',
                              host='localhost',
                              database='flight_game')
cursor = cnx.cursor()

app = Flask(__name__)
@app.route("/port/<ICAO>")
def port(ICAO):
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = %s", (ICAO,))
    res = cursor.fetchone()
    if res:
        return {"ICAO": res[0], "Name": res[1], "Municipality":res[2]}
    else:
        return {"result": "no existing airport"}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
cursor.close()
cnx.close()