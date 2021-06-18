import psycopg2
from fastapi import HTTPException

class Database:
    """PostgreSQL Database class."""

    def __init__(self, settings):
        self.host = settings.POSTGRES_SERVER
        self.username = settings.POSTGRES_USER
        self.password = settings.POSTGRES_PASSWORD
        self.port = settings.POSTGRES_PORT
        self.dbname = settings.POSTGRES_DB
        self.conn = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname,
                )
            except psycopg2.DatabaseError as e:
                print("Error connecting to DB", e)
                raise e
            finally:
                print("Connection to DB opened successfully.")

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records
    
    def insert_row(self,query,user):
        """ Run a SQL query to insert a row."""
        try:
            with self.conn.cursor() as cur:
                cur.execute(query,user)
                self.conn.commit()
                cur.close()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Information created a conflict")
        return "User added"
