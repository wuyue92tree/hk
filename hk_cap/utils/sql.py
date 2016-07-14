#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Http(Base):
	__tablename__ = 'http'
	id = Column(Integer, primary_key=True)
	sip = Column(String(20))
	dip = Column(String(20))
	sport = Column(String(20))
	dport = Column(String(20))
	method = Column(String(20))
	platform = Column(String(20))
	browser = Column(String(20))
	host = Column(String(100))
	uri = Column(String(1000))
	url = Column(String(200))
	url_type = Column(String(20))
	time = Column(DateTime, default=datetime.datetime.utcnow)


class CaptureSql(object):
	def __init__(self, database):
		self.database = database
		self.engine = create_engine('sqlite:///../data/%s.db' % self.database)
		DBSession = sessionmaker(bind=self.engine)
		self.session = DBSession()

	def create_table(self):
		return Base.metadata.create_all(self.engine)

	def delete_table(self):
		return Base.metadata.drop_all(self.engine)
