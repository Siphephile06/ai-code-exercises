from abc import ABC, abstractmethod

# Base class
class DatabaseConnectionBase(ABC):
    def __init__(self, db_type, host, port, username, password, database,
                 use_ssl=False, connection_timeout=30, retry_attempts=3,
                 pool_size=5, charset='utf8'):
        self.db_type = db_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.use_ssl = use_ssl
        self.connection_timeout = connection_timeout
        self.retry_attempts = retry_attempts
        self.pool_size = pool_size
        self.charset = charset
        self.connection = None

        @abstractmethod
        def connect(self):
            pass

# Subclass for each DB type.
                     
class MySQLConnection(DatabaseConnectionBase):
    def connect(self):
        # MySQL connection code. 
        connection_string = (
            f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
            f"?charset={self.charset}&connectionTimeout={self.connection_timeout}"
        )

        if self.use_ssl:
            connection_string += "&useSSL=true"

        print(f"MySQL Connection: {connection_string}")
        print("Connection Successful")
        return self.connection
        # In a real app, we would: self.connection = mysql.connector.connect(...)

class PostgresConnection(DatabaseConnectionBase):
    def connect(self):
        # Postgres connection code.
        connection_string = ( 
            f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

        if self.use_ssl:
            connection_string += "?sslmode=require"

        print(f"PostgreSQL Connection: {connection_string}")
        print("Connection Successful")
        return self.connection
        # In a real app, we would: self.connection = psycopg2.connect(...)

class MongoDBConnection(DatabaseConnectionBase):
    def connect(self):
        # MongoDB connection code.
        connection_string = (
            f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
            f"?retryAttempts={self.retry_attempts}&poolSize={self.pool_size}"
        )

        if self.use_ssl:
            connection_string += "&ssl=true"

        print(f"MongoDB Connection: {connection_string}")
        print("Connection Successful")
        return self.connection
        # In a real app, we would: self.connection = pymongo.MongoClient(...)

class RedisConnection(DatabaseConnectionBase):
    def connect(self):
        # Redis connection code
        print(f"Redis Connection: {self.host}:{self.port}/{self.database}")
        print("Connection Successful")
        return self.connection
        # In a real app, we would: self.connection = redis.Redis(...)

# Factory
class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_tpye, **kwargs):
        if db_type == "mysql":
            return MySQLConnection(**kwargs)
        elif db_type == "postgres":
            return PostgresConnection(**kwargs)
        elif db_type == "mongodb":
            return MongoDBConnection(**kwargs)
        elif db_type == "redis":
            return RedisConnection(**kwargs)
        else:
            raise ValueError(f"Unsupported database type{db_type}")


# Example usage
# Creating different database connections with various configurations
mysql_db = DatabaseConnection(
    db_type='mysql',
    host='localhost',
    port=3306,
    username='db_user',
    password='password123',
    database='app_db',
    use_ssl=True
)
mysql_db.connect()

mongo_db = DatabaseConnection(
    db_type='mongodb',
    host='mongodb.example.com',
    port=27017,
    username='mongo_user',
    password='mongo123',
    database='analytics',
    pool_size=10,
    retry_attempts=5
)
mongo_db.connect()
