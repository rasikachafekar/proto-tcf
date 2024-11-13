import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__, template_folder="pages")
dburl = os.getenv("DB_URL")
host_ip = os.getenv("PG_HOST")
uname = os.getenv("POSTGRES_USER").rstrip()
pwd = os.getenv("POSTGRES_PASSWORD").rstrip()
print(f"{uname=}, {pwd=}")
connection = psycopg2.connect(f"dbname=test user={uname} password={pwd} host={host_ip} port=5432")

@app.get("/")
def home():
    select = []
    with connection:
        with connection.cursor() as cur:
            cur.execute("select * from tree_species;")
            while True:
                rec = cur.fetchone()
                if not rec:
                    break
                select.append(rec)
                
    return render_template('index.html', dburl=dburl, select=select)

@app.post("/administrators/add/tree-type")
def insert():
    ip = request.get_json()
    name, scientific, desc = ip["tree_name"], ip["scientific_name"], ip["description"]
    with connection:
        with connection.cursor() as cur:
            cur.execute("select max(id) from tree_species;")
            row = cur.fetchone()
            max_id = int(row[0]) + 1
            cur.execute("insert into tree_species (id,tree_name,scientific_name,description) VALUES ({},'{}','{}','{}')".format(max_id, name, scientific, desc))
    return str(max_id)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)