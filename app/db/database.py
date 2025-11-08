import os
import psycopg2
from flask import jsonify
from dotenv import load_dotenv

load_dotenv("config/.env")


class Query:
    def __init__(self, query, params=None):
        self._query = query
        self._params = params
        self.connect()

    def connect(self):
        try:

            db_name = os.getenv("DB_NAME")
            db_user = os.getenv("DB_USER")
            db_pass = os.getenv("DB_PASS")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT") or "5432"

            self._conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_pass,
                host=db_host,
                port=db_port,
            )

            self._cursor = self._conn.cursor()

            print("Database connected successfully")

        except Exception as e:
            return jsonify({"error": "Database connection failed"}), 500

    def query(self):
        try:

            print("Executing query:", self._query)
            print("With parameters:", self._params)

            self._cursor.execute(self._query, self._params)

            try:

                return self._cursor.fetchall()

            except psycopg2.ProgrammingError:

                return jsonify({"error": "No data to fetch"}), 400

        except Exception:

            return jsonify({"error": "Query execution failed"}), 500

        finally:
            self.close()

    def close(self):

        self._cursor.close()
        self._conn.close()

        print("Closing database connection")
