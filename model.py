import pyodbc as bc
class Database:
    def connection(self):
        DATABASE = 'MYDATABASE'
        DRIVER = 'SQL SERVER'
        SERVER = 'DESKTOP-J8TVMCP\SQLEXPRESS'
        conn_String = "DRIVER={" + DRIVER + "}; SERVER=" + SERVER + "; DATABASE=" + DATABASE
        self.con = bc.connect(conn_String)
        print("Database Connected")

    def getData(self, id):
        cursor = self.con.cursor()
        getdata = "select * from STUDENT where id = " + id
        cursor.execute(getdata)
        data = cursor.fetchall()
        return data

    def updateData(self, id, name, degree, session):
        updateQuery = "update STUDENT SET id = " + id + ", name = '" + name + "', degree = '" + degree + "', session = '" + session + "' where ID = " + id
        cursor = self.con.cursor()
        cursor.execute(updateQuery)
        cursor.commit()
        print(updateQuery)

    def insertData(self, s_id, s_name, s_degree, s_session):
        insert = "insert into STUDENT (s_id,s_name,s_degree) values ( " + str(s_id) + ", '" + str(
            s_name) + "', '" + str(s_degree) + "', '" + str(s_session) + "')"
        print(insert)
        cursor = self.con.cursor()
        cursor.execute(insert)
        cursor.commit()
