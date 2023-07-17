from sqlalchemy import create_engine, text
import os
my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={
                        "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs



def load_job_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :job_id")
        result = conn.execute(query.bindparams(job_id=id))
        row = result.fetchone()
        if row is not None:
            job_dict = dict(row._asdict())
            return job_dict
        else:
            return None



