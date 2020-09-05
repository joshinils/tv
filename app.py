from flask import Flask
from flask import render_template
import xml.etree.ElementTree as ET
import jinja2
from models.programme import Programme
from models.channelName import ChannelName
from models.tvGuide import TvGuide
import codecs

from datetime import datetime

import subprocess

# sudo apt install xmltv -y
# cd to folder where this file exists
#subprocess.call("sudo tv_grab_eu_xmltvse --config-file .xmltv/tv_grab_eu_xmltvse.conf --output tv.xml", shell=True)


tree = ET.parse('tv.xml')
root = tree.getroot()


# printNode(root)
# exit()

guide = TvGuide()

channelName_Id = {}

for child in root:
    if child.tag != "channel":
        continue
    channelName_Id[child.attrib["id"]] = child.getchildren()[0].text


for child in root:
    if child.tag != "programme":
        continue
    p = Programme(ChannelName(
        channelName_Id[child.attrib["channel"]], child.attrib["channel"]), child.attrib["start"], child.attrib["stop"])
    for c in child:
        p.data[c.tag] = c.text.replace(" - ", " – ").replace("  ", " ")
    guide.addProgram(p)
    # print(p.data)

app = Flask(__name__)


templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "hello.html"
template = templateEnv.get_template(TEMPLATE_FILE)


def url_for(where, filename):
    return filename


guideHtmlString = template.render(guide=guide, url_for=url_for)

f = codecs.open("guide.html", "w", "utf-8-sig")
f.write(guideHtmlString)
f.close()


@app.route('/')
def index():
    return render_template('hello.html', guide=guide)


@app.route('/hello')
def hello():
    return 'Hello, World'
