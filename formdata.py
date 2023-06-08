from flask import Flask, render_template, request
import flaskApi
# Importing urllib request module in the program  
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    name=request.form['name']
    print(name)
    amazonUrl = 'http://192.168.90.9:8080/?q='+name
    # Using urlopen() function with url in it  
    webUrl = requests.post(amazonUrl)  

    jd = flaskApi.table_html
    print(jd)
    return render_template('showData.html', n=name,jd=jd)

if __name__ == '__main__':
    app.run(debug=True)
