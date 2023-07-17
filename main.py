from flask import Flask, jsonify, render_template
from database import load_jobs_from_db, load_job_from_db
import json
app = Flask(__name__)


@app.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs)
@app.route("/job/<id>")
def show_jobs(id):
    job = load_job_from_db(id)
    if job is None:
        return jsonify({})
    else:
        return render_template("job_pages.html",jobs=job)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)