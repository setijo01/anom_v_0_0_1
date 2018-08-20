from src.common.database import Database
import datetime
import uuid


class Message(object):

    def __init__(self, name, email, content, date_received=datetime.datetime.utcnow(), _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        self.email = email
        self.content = content
        self.date_received = date_received

    def json(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
            'content': self.content,
            'date_received': self.date_received
        }

    @classmethod
    def get_by_id(cls, _id):
        user_data = Database.find_one(collection='messages', query={'_id': _id})
        if user_data:
            return cls(**user_data)

    @classmethod
    def get_by_email(cls, email):
        user_data = Database.find_one(collection='messages', query={'email': email})
        if user_data:
            return cls(**user_data)

    def save_to_database(self):
        while self.get_by_id(self._id):
            self._id = uuid.uuid4().hex
        Database.insert(collection='messages', data=self.json())
        print("Message is successfully stored into database.")

