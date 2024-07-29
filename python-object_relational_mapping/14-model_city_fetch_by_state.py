#!/usr/bin/python3
"""
Fetch and display all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>")
        return

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{database_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    main()
