import dotenv
import psycopg2
import psycopg2.extras
import os
dotenv.load_dotenv()


class Database:
    def __init__(self):
        self.connection_string = self.get_connection_string()
        self.connection = None
        self.cursor = None

    def get_connection_string(self):
        user_name = os.environ.get('PSQL_USER_NAME')
        password = os.environ.get('PSQL_PASSWORD')
        host = os.environ.get('PSQL_HOST')
        database_name = os.environ.get('PSQL_DB_NAME')

        env_variables_defined = all([user_name, password, host, database_name])

        if env_variables_defined:
            return f'postgresql://{user_name}:{password}@{host}/{database_name}'
        else:
            raise KeyError('Some necessary environment variable(s) are not defined')

    def __enter__(self):
        self.connection = psycopg2.connect(self.connection_string)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

