import pymysql
# from passlib.hash import sha256_crypt
class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        password = ''
        database = 'Voyago'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

    def add_person(self, firstname, lastname,email):
        sql = """insert into marketing (firstname, lastname,email) values (%s, %s, %s)"""
        input_values = (firstname, lastname,email)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_person_id = "select id from marketing order by id desc limit 1"
        self.cursor.execute(sql_new_person_id)
        new_person = self.cursor.fetchone()
        return new_person[0]

    def login(self, email, password):

        succesful_login = []
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        self.cursor.execute(sql)
        input_values = (email,password)
        self.cursor.execute(sql, input_values)
        login = self.cursor.fetchall(email,password)
        if login == email and password:
                return succesful_login


    def add_user(self, firstname, lastname,email,password):
        sql = """insert into user (firstname, lastname,email,password) values (%s, %s, %s,%s)"""
        input_values = (firstname, lastname,email,password)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_register_id = "select id from user order by id desc limit 1"
        self.cursor.execute(sql_register_id)
        user = self.cursor.fetchone()
        return user[0]

