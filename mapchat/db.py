import time
import uuid

from peewee import *

DB = SqliteDatabase('mapchat.db')


#######################
#
#   Entity section
#
#######################


class Location(Model):
    lat = FloatField()
    long = FloatField()
    name = CharField()

    class Meta:
        database = DB


class User(Model):
    user_id = CharField(unique=True)
    username = CharField()

    class Meta:
        database = DB


class Chat(Model):
    chat_id = CharField()
    owner = ForeignKeyField(User, backref="chat")
    created_at = DateTimeField()
    location = ForeignKeyField(Location, backref="chat")
    deleted = BooleanField(default=False)

    class Meta:
        database = DB


class Message(Model):
    message = CharField()
    chat = ForeignKeyField(Chat, backref="messages")

    class Meta:
        database = DB


ALL_TABLES = [Location, User, Chat, Message]


#######################
#
#   Helper section
#
#######################

class CreateException(Exception):
    pass


def create_location(name, lat, long):
    try:
        parsed_lat, parsed_long = float(lat), float(long)
        return Location.create(name=name, lat=parsed_lat, long=parsed_long)
    except Exception:
        raise CreateException(f"Could not create the Location object for these values: {name},{lat},{long}")


def create_user(username):
    return User.create(username=username, user_id=generate_user_id()).save()


def create_chat(db, owner_id, location):
    owner = db.execute(User.select().where(User.user_id == owner_id))
    if owner:
        return Chat.create(owner=owner, location=location, created_at=time.time())
    raise CreateException(f"Could not create the chat for these values: {owner_id},{location}")


def create_message(db, message, chat_id):
    chat = db.execute(Chat.select().where(Chat.chat_id == chat_id))
    if chat:
        return Chat.create(message=message, chat=chat)
    raise CreateException("You're dumb af")


def generate_user_id():
    return str(uuid.uuid4())


def drop_tables(db):
    db.drop_tables(ALL_TABLES)


def create_tables(db):
    db.create_tables(ALL_TABLES)


if __name__ == '__main__':
    drop_tables(DB)
    create_tables(DB)

    with DB.atomic() as db:

        User.insert_many([("nice name", "nice id")], fields=(User.username, User.user_id)).execute()

        for stupid_shit in DB.execute(User.select()):
            print(stupid_shit)
