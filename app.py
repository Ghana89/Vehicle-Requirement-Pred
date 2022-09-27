from flask import Flask , render_template , request
from artifacts.utils import prediction1
app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')
@app.route("/prediction",methods = ['POST'])
def prediction():
    data = request.form
    obj = prediction1(data)
    result = obj.output()
    return render_template('index.html', pred = result)

if __name__ == '__main__':
    app.run(debug=True)

    
