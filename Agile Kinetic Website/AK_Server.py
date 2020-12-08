import os
from flask import Flask, redirect, request, render_template, jsonify
import sqlite3


#Please Note Many of the later app routes which are commented out
#and have placeholder written next to them
#are (as you may have guessed) placeholders

#To make them functional simply uncomment them and correct the
#render template name
#The placeholders are unlikely to have been properly tested if you
#do uncomment them
#There is also a piece of code below for inserting information into
#the database, this is very much untested, but I thought it might be
#useful later on :)

#-Love from Archie
#p.s any questions just let me know

#=====================================================================
# Need to insert data base name below
#DATABASE = ''
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#=====================================================================
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

#Route to Home Page
@app.route("/Home", methods=['POST','GET'])
def returnHome():
    if request.method == 'GET':
        print("Home Page") #Just for testing
        return render_template('homeBlock.html')

#Route to About Us page
@app.route("/AboutUs", methods=['POST','GET'])
def returnAboutUs():
    if request.method == 'GET':
        return render_template('AboutUs.html')

@app.route("/Support", methods=['POST','GET'])
def returnSupport():
    if request.method == 'GET':
        print("support page") #Just for testing
        return render_template('support.html')

#Route to Admin page
@app.route("/Admin", methods=['POST','GET'])
def returnFourth():
    if request.method == 'GET':
        print("Admin Page Accessed")
        return render_template('adminBlock.html')

#-----------WORK IN PROGRESS----------------------------------------
    #FAQ Page Post To
#    if request.method == 'POST':
#        faqQuestion = request.form.get("faqQuestion", default="Error")
#	    faqAnswer = request.form.get("faqAnswer", default="Error")
#		print("inserting module" + faqAnswer)
#	    try:
#		    print('Inserting')
#			conn = sqlite3.connect(DATABASE)
#			cur = conn.cursor()      #NEED TO CHANGE PLACEHOLDER TO NAME OF DATABASE TABLE
#			cur.execute("INSERT INTO PLACEHOLDER ('faqQuestion','faqAnswer')\
#			        VALUES (?,?)",(faqQuestion,faqAnswer) )
#
#			print("Still Inserting")
#			conn.commit()
#			msg =  faqQuestion + "has been added"
#		except:
#			conn.rollback()
#			msg = "error in insert, please try again"
#		finally:
#			conn.close()
#			return msg


#Route to Patients page - PLACE HOLDER
@app.route("/PatientsInformation", methods=['GET'])
def returnFifth():
    if request.method == 'GET':
        return render_template('Patients.html')

#Route to Log-in page - PLACE HOLDER
#@app.route("/Admin", methods=['POST','GET'])
#def returnSixth():
#    if request.method == 'GET':
#        return render_template('Login.html')


#Route to Contact page - PLACE HOLDER
@app.route("/Contact", methods=['POST','GET'])
def returnSeventh():
    if request.method == 'GET':
        return render_template('Contact.html')

#Route to Blog/Update page
@app.route("/Blog", methods=['POST','GET'])
def returnEitgh():
    if request.method == 'GET':
        return render_template('blog.html')

#Jinja template for NavBar
@app.route("/templates/NavBar", methods=['GET'])
def navbarTemplate():
    if request.method == 'GET':
        return render_template('NavBar.html')

#Jinja template for footer
@app.route("/templates/Footer", methods=['GET'])
def footerTemplate():
    if request.method == 'GET':
        return render_template('Footer.html')




if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)
