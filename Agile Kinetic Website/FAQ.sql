DROP TABLE IF EXISTS FAQ;

CREATE TABLE "FAQ" (
	"ID"	INTEGER,
	"Question"	TEXT,
	"Answer"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO FAQ ("Question", "Answer") VALUES ("How do I sign up for Mobility Hub?", "Get in touch with us via the contact page and we'll create login details for you");
