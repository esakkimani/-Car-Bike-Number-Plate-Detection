from flask import Flask, render_template
import ImageCapture

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/scan_image/')
def scan():
    plateNumber = ImageCapture.Image()


# @app.route('/confirm', methods=['POST', 'GET'])
# def getValues():
#     if request.method == 'POST':
#         name = request.form.get('username')
#         password = request.form.get('pass')
#         if 8 <= len(name) <= 15:
#             return render_template('index.html', username=name, msg1="valid username", passs=password)
#         else:
#             return render_template('index.html', msg="username is incorrect", password=password)


if __name__ == '__main__':
    app.run(debug=True)
