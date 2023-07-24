from flask import Flask, jsonify, render_template, request
from database import load_jobs_from_db, load_job_from_db 
# add_application_to_db
app = Flask(__name__)


@app.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template('index.html', 
                         jobs=jobs)
@app.route("/job/<id>")
def show_jobs(id):
    job = load_job_from_db(id)
    if job is None:
        return jsonify({})
    else:
        return render_template("job_pages.html",jobs=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_jobs(id):
  data = request.form
  job = load_job_from_db(id)
  # add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         jobs=job)
@app.route("/about")
def about():
  return render_template("about.html")
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)