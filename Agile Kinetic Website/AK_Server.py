import os
from flask import Flask, redirect, request, render_template, jsonify
import sqlite3


#=====================================================================
# Need to insert data base name below
DATABASE = 'FAQDatabase.db'
DATABASE2 = 'Blog.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#=====================================================================


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

#-----------WORK IN PROGRESS----------------------------------------------------
    #FAQ Page Post To
    if request.method == 'POST':
        print("Database Accessed")
        faqQuestion = request.form.get("faqQuestion", default="Error")
        faqAnswer = request.form.get("faqAnswer", default="Error")
        print("inserting " + faqAnswer)
        try:
            print('Attempting to connect to database')
            conn = sqlite3.connect(DATABASE)
            print('Connected to database')
            cur = conn.cursor()
            print('Conn Cursor Running')
#Work In Progress ====================================================================================
            cur.execute("""CREATE TABLE IF NOT EXISTS "FAQ" (
	            "ID"	INTEGER,
	            "Question"	TEXT,
	            "Answer"	TEXT,
	            PRIMARY KEY("ID" AUTOINCREMENT)
            )""")


            cur.execute("INSERT INTO FAQ ('Question', 'Answer')\
		    				VALUES (?,?)",(faqQuestion, faqAnswer) )

#=======================================================================================================
            print('Success database accessed')
            conn.commit()
            msg =  faqQuestion + " has been added"
        except:
            conn.rollback()
            msg = "error in insert, please try again"
        finally:
            conn.close()
            return msg
#-------------------------------------------------------------------------------
    #Blog page post upload
    if request.method == 'POST':
        print("Database Accessed")
        addTitle = request.form.get("addTitle", default="Error")
        addAuthor = request.form.get("addAuthor", default="Error")
        addText = request.form.get("addText", default="Error")
        print("Uploading blog post: " + addTitle)
        try:
            print('Inserting')
            conn = sqlite3.connect(DATABASE2)
            print('Connected to database')
            cur = conn.cursor()
            print('Conn Cursor Running')
            cur.execute("""CREATE TABLE IF NOT EXISTS "Blog" (
	            "ID"	INTEGER,
	            "Title"	TEXT,
	            "Author"	TEXT,
	            "Message"	TEXT,
	            PRIMARY KEY("ID" AUTOINCREMENT)
            )""")

            cur.execute("INSERT INTO Blog ('Title', 'Author', 'Message')\
		    				VALUES (?,?,?)",(addTitle, addAuthor, AddText) )
            print('Still Inserting')
            conn.commit()
            msg =  addTitle + " has been uploaded as a post"
        except:
            conn.rollback()
            msg = "Upload error, please try again"
        finally:
            conn.close()
            return msg

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
