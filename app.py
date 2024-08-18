from flask import Flask, render_template, request, flash
import os
from dotenv import load_dotenv
import smtplib

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/resume')
def resume():
   return render_template('resume.html')

@app.route('/projects')
def projects():
   return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'POST':
      name = request.form['name']
      email = request.form['email']
      number = request.form['number']
      message = request.form['message']
      
      flash('Thank you for getting in touch! I will get back to you soon.')
      
      with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
         connection.set_debuglevel(1)
         connection.starttls()
         connection.login(EMAIL, PASSWORD)
         
         subject = "New Message From Portfolio"
         body = f"Name: {name}\nEmail: {email}\nPhone: {number}\nMessage: {message}"
         email_message = f"Subject: {subject}\n\n{body}"
         
         connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_message)
         
         return render_template("contact.html", msg_sent=True)

   return render_template("contact.html", msg_sent=False)



if __name__ == "__main__":
   app.run(debug=True)