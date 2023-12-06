import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    @classmethod
    def create_table(self):
                sql = """
            CREATE TABLE dogs
                (id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT)
        """

                CURSOR.execute(sql)
                CONN.commit()
    def drop_table(cls):
        sql = """
            DROP TABLE dogs
        """

        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit()
    @classmethod
    def create(cls, name, breed):
        dog = cls(name, breed)
        dog.save()
        return dog
    @classmethod
    def new_from_db(cls, row):
        dog = cls(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

        return dog
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM dogs
        """

        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM dogs
            WHERE name = ?
            LIMIT 1
        """


       
    
