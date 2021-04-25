from sqlalchemy import Column, String

from userbot.plugins.sql_helper import BASE, SESSION
class Admin(BASE):
    __tablename__ = "admins"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


Admin.__table__.create(checkfirst=True)


def is_admin(sender_id):
    try:
        return SESSION.query(Admin).all()
    except:
        return None
    finally:
        SESSION.close()

def admin_(admin):
    try:   
     a =  SESSION.query(Admin).get((str(admin)))
     return a
    except Exception:
     return False
    finally:
     SESSION.close()



def make_admin(sender):
    adder = Admin(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def demote(sender):
    delete = SESSION.query(Admin).get((str(sender)))
    if delete:
        SESSION.delete(delete)
        SESSION.commit()



#    Copyright (C) Midhun KM 2020
 # Lagta hai meri jindgi vich khuch galt horeya ve. TwT
def add_usersid_in_db(sender: int):
    id_user = Admin(str(sender))
    SESSION.add(id_user)
    SESSION.commit()


def users():
    all_users = SESSION.query(Admin).all()
    SESSION.close()
    return all_users

def already_added(sender):
    try:
        return SESSION.query(Admin).filter(Admin.sender == str(sender)).one()
    except:
        return None
    finally:
        SESSION.close()
