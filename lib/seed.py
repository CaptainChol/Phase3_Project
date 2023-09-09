from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Converter, Encripted


engine = create_engine('sqlite:///key.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



session.commit()

session.close()