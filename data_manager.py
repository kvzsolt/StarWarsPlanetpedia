class DataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, db):
        if not hasattr(self, 'db'):
            self.db = db

    def add_user(self, username, password):
        query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)"""
        with self.db as cursor:
            cursor.execute(query, [username, password])

    def get_password_for_login(self, username):
        query = """
        SELECT password from users
        WHERE users.username = %s;
        """
        with self.db as cursor:
            cursor.execute(query, [username])
            return cursor.fetchone()

    def get_users_for_login(self, username):
        query = """
        SELECT username from users
        WHERE users.username = %s;
        """
        with self.db as cursor:
            cursor.execute(query, [username])
            return cursor.fetchone()
