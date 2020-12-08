DROP TABLE IF EXISTS Blog;

CREATE TABLE "Blog" (
	"ID"	INTEGER,
	"Title"	TEXT,
	"Author"	TEXT,
	"Message"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO Blog ("Title", "Author", "Message") VALUES ("Welcome to Mobility Hub!", "Peter B.", "We are really excited to be launching Mobility Hub to help bridge the gap between doctors and recovering patients");
