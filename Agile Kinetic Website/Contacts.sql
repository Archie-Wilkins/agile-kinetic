DROP TABLE IF EXISTS Contacts;

CREATE TABLE "Contacts"(
	"ID"	INTEGER,
	"firstName"	TEXT,
	"lastName"	TEXT,
  "Email"	TEXT,
  "Clinician"	Boolean,
  "queryType"	TEXT,
  "Message"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO Contacts ("firstName", "lastName","Email","Clinician","queryType","Message" ) VALUES ("Ryan", "Swales","123@gmail.com",True,"asking a question","wooo im welsh");
