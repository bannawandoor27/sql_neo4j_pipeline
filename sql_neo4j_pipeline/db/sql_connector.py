
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

class PostgresConnector:
    def __init__(self):
        self.host = os.getenv("PSQL_HOST")
        self.database = os.getenv("PSQL_DATABASE")
        self.user = os.getenv("PSQL_USER")
        self.password = os.getenv("PSQL_PASSWORD")
        self.port = os.getenv("PSQL_PORT")

        self.database_url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def execute_query(self, query, params=None):
        session = self.get_session()
        try:
            result = session.execute(query, params)
            session.commit()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def fetch_query(self, query, params=None):
        session = self.get_session()
        try:
            result = session.execute(query, params).fetchall()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            session.close()


