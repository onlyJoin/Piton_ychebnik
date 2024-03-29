from flask import Flask, jsonify
import json
import sqlite3

app = Flask(__name__)


@app.route("/types/")
def index():
    with open('js.json') as js_file:
        js = json.load(js_file)

        con = sqlite3.connect("films_db.sqlite")

        cur = con.cursor()

        result = cur.execute(f"""SELECT * FROM films
                    WHERE year = {js['year']} AND {js['duration']} % 2 == 0""").fetchall()
        con.close()

    a = []
    for i in result:
        a.append({
            'title': i[0]
        })

    return jsonify(a)


if __name__ == '__main__':
    app.run()
