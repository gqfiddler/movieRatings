import pandas as pd
import mysql.connector as ms

createTestTable = (
    "CREATE TABLE IF NOT EXISTS test_table3 ("
     "   rating_id INT NOT NULL AUTO_INCREMENT,"
     "   user_id INT DEFAULT NULL,"
     "   movie_id INT DEFAULT NULL,"
     "   rating FLOAT DEFAULT NULL,"
     "   timestamp INT DEFAULT NULL,"
     "   PRIMARY KEY (rating_id)"
    ");"
)

login_info = {
    "user": "root",
    "database": "movieLens",
    "password": "s2sofour444"
}
# cnx = ms.connect(user="root", database="movieLens", password="s2sofour444")
cnx = ms.connect(**login_info)
cursor = cnx.cursor(buffered=True)
cursor.execute(createTestTable)
print(cursor.execute("DESCRIBE test_table3;"))
