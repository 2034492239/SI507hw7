#flaskapp3.py
import requests
import secrets_nyt
from flask import Flask, render_template

#part1
NYTAPI_KEY = secrets_nyt.api_key
base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
params = {
    "api-key":NYTAPI_KEY,
    }
response = requests.get(base_url, params)
result = response.json()
article_list = []
for i in range(5):
    article_list.append(result['results'][i]['title'])
url_list = []
for i in range(5):
    url_list.append(result['results'][i]['url'])
# print(result['results'][1])
# print(len(url_list))


#part2
app = Flask(__name__)
#homepage
@app.route('/')
def index():
    return '<h1>Welcome!</h1>'
#name page
@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm) 
#headline page
@app.route('/headlines/<nm>')
def headlines(nm):
    return render_template('headlines.html', name=nm, stories = article_list, urls = url_list)

if __name__ == '__main__':
    app.run(debug=True)