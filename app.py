from flask import Flask, render_template,jsonify

app=Flask(__name__)

JOBS=[
  {
  "id":1,
 'title':'Data analyst',
  "location":'Texas, USA',
  "salary":'$100,000'
},
{
       "id":2,
      'title':'Data scientist',
       "location":'Texas, USA',
       "salary":'$100,000'
     },
  
    {
      "id":1,
     'title':'Frontend engineer',
      "location":'California, USA',
      "salary":'$150,000'
    }
  
     ]

@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
