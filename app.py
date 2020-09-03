from flask import Flask
app = Flask(__name__)

# sudo apt install xmltv -y
# cd to folder where this file exists
# tv_grab_eu_xmltvse --config-file .xmltv/tv_grab_eu_xmltvse.conf --output tv.xml


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'
