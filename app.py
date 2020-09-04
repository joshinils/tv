from flask import Flask
from flask import render_template
import xml.etree.ElementTree as ET


tree = ET.parse('tv.xml')
root = tree.getroot()


def printNode(root, indent=0):
    for child in root:
        print(' ' * indent + "child.tag   :", child.tag)
        print(' ' * indent + "child.attrib:", child.attrib)
        print(' ' * indent + "child.text  :", child.text)
        print(' ' * indent + "child.tail  :", child.tail)
        printNode(child, indent + 4)


# printNode(root)
# exit()


app = Flask(__name__)

# sudo apt install xmltv -y
# cd to folder where this file exists
# tv_grab_eu_xmltvse --config-file .xmltv/tv_grab_eu_xmltvse.conf --output tv.xml


@app.route('/')
def index():
    return render_template('hello.html', a_variable="foo", root=root)


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    # parseObjects(root)
    app.run()
