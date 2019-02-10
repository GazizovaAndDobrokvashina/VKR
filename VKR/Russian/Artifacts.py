import sqlite3

class Artifacts:
    def __init__(self, conn):
        self.conn = conn
        self.actors_db = conn.cursor()
        self.actors_db.execute("""CREATE TABLE if not exists Artifacts(id integer primary key autoincrement, base_name text, nams text)""")
        self.conn.commit()

    def add_artifact(self, base_name, names):
        nams = str(names)
        # print(nams)
        self.actors_db = self.conn.cursor()
        self.actors_db.execute('SELECT * FROM Artifacts WHERE base_name = ?', (base_name,))
        res = self.actors_db.fetchall()
        if len(res) == 0:
            self.actors_db.execute('INSERT INTO Artifacts(base_name, nams) VALUES (?,?)', (base_name, nams))
            self.conn.commit()

    def get_artifacts(self):
        actors = list()
        for row in self.actors_db.execute('SELECT * FROM Artifacts'):
            actors.append(row)
        return actors
