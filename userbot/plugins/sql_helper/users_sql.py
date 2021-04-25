# (c) @its_xditya
from sqlalchemy import Column, String
from . import BASE, SESSION


class userbase(BASE):
    __tablename__ = "UserBase"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


userbase.__table__.create(checkfirst=True)


def add_to_userbase(message_id: int, chat_id: int, um_id: int):
    """ add the message to the table """
    __user = userbase(message_id, str(chat_id), um_id)
    SESSION.add(__user)
    SESSION.commit()


def full_userbase():
    users = SESSION.query(userbase).all()
    SESSION.close()
    return users


def present_in_userbase(chat_id):
    try:
        return SESSION.query(userbase).filter(
            userbase.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

        
def his_userid(message_id: int):
    """ get the user_id from the message_id """
    try:
        s__ = SESSION.query(userbase).get(str(message_id))
        return int(s__.chat_id), s__.um_id
    finally:
        SESSION.close()