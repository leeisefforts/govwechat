from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class BaoMing(db.Model):
    __tablename__ = 'baoming'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False, server_default=FetchedValue())
    sid = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f1 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f2 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f3 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f4 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f0 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    openid = db.Column(String(128), nullable=False, server_default=FetchedValue())