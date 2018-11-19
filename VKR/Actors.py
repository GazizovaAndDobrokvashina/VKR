import sqlite3

class Actors:
    def __init__(self, conn):
        self.actors_db = conn.cursor()
        self.actors_db.execute("""CREATE TABLE if not exists Actors(id integer primary key autoincrement, base_name text, nams text)""")

        # ex = self.actors_db.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='table_name'""")
        # if ex == 0:

    def add_actor(self, base_name, nams):
        self.actors_db.execute('INSERT INTO Actors(base_name, nams) VALUES (?,?)', (base_name, nams))

    def get_actors(self):
        actors = list()
        for row in self.actors_db.execute('SELECT * FROM Actors'):
            actors.append(row)
        return actors
