from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {

       'id':1,
       'title':'front-end enginer',
       'location':"pakistan,karachi",
       'salary':100000,
    },

    {
       'id':2,
       'title':'web dev',
       'location':"pakistan,lahore",
       'salary':150000,
    
    },


    { 
      'id':3,
       'title':'backend dev',
       'location':"remote",
       'salary':102000,
    },

  ]
@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
 
