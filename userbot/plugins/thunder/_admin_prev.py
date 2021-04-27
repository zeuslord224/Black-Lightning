#    Copyright (C) 2021 KeinShin


from userbot import bot

from sqlalchemy.orm import sessionmaker


from sqlalchemy import Column, Integer, String
from userbot.plugins.sql_helper import BASE, SESSION

class AdminRank:
    async def __init__(self, name):
        self.name = name
  
    async def getAdin(self, name):
     pass

    async def rnk(self, chet, rank):
        self.rank = rank
        if chet is None:
            await bot.send_message("me", f"Rank has been set to {self.rank} of admin {self.name}")
        else:

            await bot.send_message(chet, f"Rank has been set to {self.rank}")

Session = sessionmaker()
session = Session()


class Admin(BASE):
    __tablename__ = 'admin'
    rank = Column('admin_rank', Integer, primary_key=True)
    name = Column('admin_name', String(50))
    def __repr__(self):
        return "<Admin(name='%s', rank='%s')>" % (
                                self.name, self.rank)
    @staticmethod
    def he_is_admin(name):
        he_is_ad =  session.query(Admin).filter_by(name=f'{name}').first() 
        return he_is_ad 
    def prom(self, name, rank, get ):
        ad = Admin()
        self.nam  = name
        self.rank = rank 
        self.get = get
        admin = Admin(name=f"{name}", rank=f"{rank}") 

         
        if self.get is True:
         self.tru = admin is ad.he_is_admin()   
         return self.tru
        else:
          session.add(admin)
          session.commit()
Admin.__table__.create(checkfirst=True)



