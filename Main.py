from flask import Flask,render_template,request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

#Renders index.html as front end from templates folder
@app.route('/')
def home():
    return render_template('index.html')

#Triggers QR code generator if form is submitted (method post)
@app.route('/', methods=['POST'])
def genQR():
    memory = BytesIO()
    #Gets link variable from index.html via flask
    URL = request.form.get('link')
    image = qrcode.make(URL)
    image.save(memory) #saves image in code rather than locally downloading the image
    memory.seek(0) #Ensures Byte sequence is read from the start index value 0
    base64Img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii') #converts bytes to base 64

    return render_template('index.html', URL = base64Img)

#Runs app
if __name__ == '__main__':
    app.run(debug = True)