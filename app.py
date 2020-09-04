from flask import Flask
from flask import render_template
import xml.etree.ElementTree as ET

from models.programme import Programme
from models.channel import Channel

from datetime import datetime

tree = ET.parse('tv.xml')
root = tree.getroot()


# printNode(root)
# exit()

progs = []

for child in root:
    if child.tag != "programme":
        continue
    p = Programme(Channel(
        child.attrib["channel"], child.attrib["channel"]), child.attrib["start"], child.attrib["stop"])
    for c in child:
        p.data[c.tag] = c.text.replace(" - ", " – ").replace("  ", " ")
    progs.append(p)
    # print(p.data)

channelProg = {}
for prog in progs:
    channelProg.setdefault(prog.channel.id, []).append(prog)

for channel in channelProg:
    print(channel)

app = Flask(__name__)

# sudo apt install xmltv -y
# cd to folder where this file exists
# tv_grab_eu_xmltvse --config-file .xmltv/tv_grab_eu_xmltvse.conf --output tv.xml


@app.route('/')
def index():
    return render_template('hello.html', channelProg=channelProg)


@app.route('/hello')
def hello():
    return 'Hello, World'
