from flask import Flask
app = Flask(__name__)
from flask import render_template, url_for, send_file
import pkg_resources

logo = None
integration_data = None
packagename = None

@app.route('/')
def index():
  global logo, integration_data, packagename
  return render_template('index.html', name=packagename, logo=logo, data=integration_data)

@app.route('/dashboard/')
def dashboard():
  global logo, integration_data, packagename
  return render_template('integration_dashboard.html', name=packagename, logo=logo, data=integration_data)


def main(name, integration):
  global logo, integration_data, packagename
  
  integration_data = integration
  packagename = name

  with open(packagename + '/assets/' + integration_data['logo_file_name'], 'r') as f:
    data = f.read()
    logo = data.encode("base64")  


  app.debug = True
  app.run()

