from flask import redirect, render_template, request
from Project import app
from Project.email import send_email

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/sendMail", methods=['POST'])
def sendMail():
    recipient = request.form['email']
    input = request.form['content']

    print('Got the input!')

    if recipient and input:
        print("Attempting to send email...")
        subject = "User Input Received"
        body = f"The user entered: {input}"
        if send_email(recipient, subject, body):
            return redirect('success.html')
        else:
            return render_template('home.html', error='Error!!')
    return render_template('home.html')

@app.route("/success")
def display():
    return "Successful!"

if __name__ == '__main__':
    app.run(debug=True)