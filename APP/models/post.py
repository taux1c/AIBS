
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, Text, Boolean
from json import loads, dumps
from pathlib import Path


Base = declarative_base()


class Post(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    post_id = Column(Text, nullable=False, unique=True)
    message = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    subject = Column(Text, nullable=False)
    media = Column(Text, nullable=True)
    downloaded = Column(Boolean, nullable=False, default=False)

    def __init__(self, post_id, message, author, category, subject, media):
        self.post_id = post_id
        self.message = message
        self.author = author
        self.category = category
        self.subject = subject
        self.media = media
        self.downloaded = False

    def save(self, profile):
        self.save_location = str(profile.save_location)
        self.media = dumps(self.media)
        Base.metadata.create_all(create_engine(profile.db_string))
        engine = create_engine(profile.db_string)
        Session = sessionmaker(bind=engine)
        with Session() as session:
            results = session.query(Post).filter(Post.post_id == self.post_id).first()
            if results is None:
                print(f"Saving post: {self.post_id}")
                session.add(self)
                session.commit()
            else:
                print(f"Post: {self.post_id} already exists in database.")

    def __repr__(self):
        identity = (f"Post: {self.post_id}\n"
                    f"Message: {self.message}\n"
                    f"Author: {self.author}\n"
                    f"Category: {self.category}\n"
                    f"Subject: {self.subject}\n"
                    f"Media: {self.media}\n"
                    f"Downloaded: {self.downloaded}")
        return identity


    def load(self):
        self.media = loads(self.media)


    def dump(self):
        self.media = dumps(self.media)