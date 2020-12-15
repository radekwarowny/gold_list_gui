import datetime
import shutil
import sqlite3

__author__ = "Radek Warowny"
__licence__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Radek Warowny"
__email__ = "radekwarownydev@gmail.com"
__status__ = "Demo"


def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


def db_conn():

    # Open existing or create new databse

    conn = sqlite3.connect('goldlist_db.sqlite')
    cur = conn.cursor()

    try:
        # Create table 'Users' in database
        cur.execute("""CREATE TABLE Users 
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
             username TEXT NOT NULL, 
             password TEXT NOT NULL,
             account_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
             )""")
        # Create table 'word_explanation' in database
        cur.execute("""CREATE TABLE word_explanation
            (page_id INTEGER PRIMARY KEY AUTOINCREMENT, 
             word TEXT NOT NULL,
             explanation TEXT NOT NULL,
             user_id INTEGER NOT NULL,
             page_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
             FOREIGN KEY (user_id) REFERENCES Users(user_id)
             )""")

        # Create table 'Dist_one' in database
        cur.execute("""CREATE TABLE Dist_one
            (dist_id INTEGER PRIMARY KEY AUTOINCREMENT, 
             word TEXT NOT NULL,
             explanation TEXT NOT NULL,
             user_id INTEGER NOT NULL,
             distillation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
             FOREIGN KEY (user_id) REFERENCES Users(user_id)
             )""")
        # Create table 'Dist_two' in database
        cur.execute("""CREATE TABLE Dist_two
                   (dist_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    word TEXT NOT NULL,
                    explanation TEXT NOT NULL,
                    user_id INTEGER NOT NULL,
                    distillation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                    )""")
        # Create table 'Dist_three' in database
        cur.execute("""CREATE TABLE Dist_three
                   (dist_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    word TEXT NOT NULL,
                    explanation TEXT NOT NULL,
                    user_id INTEGER NOT NULL,
                    distillation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                    )""")
        # Insert first user
        dummy_username = ('dummy',)
        dummy_password = ('0000',)

        sqlite_insert_with_param = """INSERT INTO Users (username, password) 
                VALUES (?,?);"""

        data_tuple = (dummy_username, dummy_password)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print_centre("USER ADDED")

    except sqlite3.Error as error:
        pass  # Needs a tweak as it throws error every time it tries to insert into users
    finally:
        if conn:
            conn.close()


def create_user(username, password):

    # Connect to database

    conn = sqlite3.connect('goldlist_db.sqlite')
    cur = conn.cursor()

    # Insert variables into database
    try:
        sqlite_insert_with_param = """INSERT INTO Users (username, password) 
        VALUES (?,?);"""

        data_tuple = (username, password)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print_centre("USER ADDED")

        cur.close()

    except sqlite3.Error as error:
        print_centre("FAILED TO ADD USER")
    finally:
        if conn:
            conn.close()


def check_password(password):

    password = (password,)
    conn = None
    try:
        conn = sqlite3.connect('goldlist_db.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT user_id FROM Users WHERE password =?', password)
        output = cur.fetchone()
        if output is not None:
            flag = True
        else:
            flag = False

        return flag, output
    except sqlite3.Error as e:

        print_centre(f"Error {e.args[0]}")
    finally:
        if conn:
            conn.close()


def check_username(username):

    username = (username,)
    conn = None
    try:
        conn = sqlite3.connect('goldlist_db.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT user_id FROM Users WHERE username =?', username)
        output = cur.fetchone()
        if output is not None:
            flag = True
        else:
            flag = False

        return flag
    except sqlite3.Error as e:

        print_centre(f"Error {e.args[0]}")
    finally:
        if conn:
            conn.close()


def word_count(user_id):
    conn = sqlite3.connect('goldlist_db.sqlite')
    cur = conn.cursor()

    words = cur.execute('SELECT count(*) FROM word_explanation WHERE user_id =?', user_id)
    output = words.fetchmany()[0][0]

    cur.close()
    conn.close()
    print("FUNCT IS WORKING")
    print(output)
    return output


def insert_word(word, explanation, user_id):
    conn = sqlite3.connect('goldlist_db.sqlite')
    cur = conn.cursor()

    try:
        sqlite_insert_with_param = """insert into word_explanation (word, explanation, user_id) VALUES (?,?,?);"""

        data_tuple = (word, explanation, user_id)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print_centre("Failed to insert Python variables into word_explanation table.")
        print(error)
    finally:
        if conn:
            conn.close()


def oldest_word(user_id):
    conn = sqlite3.connect('goldlist_db.sqlite')
    cur = conn.cursor()
    cur.execute("""select word, explanation, page_date from word_explanation where user_id =? and page_date < datetime('now', '-14 day')""", user_id)
    word = cur.fetchone()
    cur.close()
    conn.close()
    if word is None:
        output = "No words older than 14 days"
    else:
        output = word[0]
    return output


def insert_distil(word, explanation, user_id):
    conn = sqlite3.connect('goldlist_db.sqlite')
    cur = conn.cursor()

    try:

        #cur.execute("SELECT word, explanation FROM word_explanation WHERE user_id =? Order BY (page_date)", (user_id,))
        #data = cur.fetchone()
        #cur.execute("DELETE FORM word_explanation WHERE word = ? AND user_id ?", (data[1], data[3]))
        cur.execute("""delete from word_explanation where word = ?""", (word,))
        cur.execute("""insert into Distillations (word, explanation, user_id) VALUES (?,?,?)""", (word, explanation, user_id,))

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print_centre("Failed to insert Python variables into Distillations table.")
        print(error)
    finally:
        if conn:
            conn.close()











