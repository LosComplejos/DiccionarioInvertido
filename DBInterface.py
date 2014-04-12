# -*- encoding: utf-8 -*-
import sqlite3


class createDB:
	def __init__(self,tabla):
		self.tabla=tabla
		self.conn=sqlite3.connect("acm.db")
		self.cursor=self.conn.cursor()

#	def createTitle(self):
#		try:
#			self.cursor.execute('CREATE TABLE '+self.tabla+' ('+
#						      'id TEXT PRIMARY KEY, '+
#						      'unique_id NUMERIC, '+
#						      'parent_id NUMERIC, '+
#						      self.tabla.lower()+' TEXT)')
#			self.conn.commit()

#		except Exception as error:
#			print error



	def itera(self):
		d={}
		try:
			self.cursor.execute("select id,"+self.tabla.lower()+" from "+self.tabla)#+" limit 10")#+" where parent_id!=0")
			data=self.cursor.fetchall()
			for row in data:
				d[row[0]]=row[1]
			return d
			
		except Exception as error:
			print error

#	def saveDB(self,ID,abstr):
#		temp=ID.split(".")
#		if len(temp)==1:
#			unique_id=temp[0]
#			parent_id="0"
#		else:
#			unique_id=temp[1]
#			parent_id=temp[0]
#		
#		abstr=abstr.replace('"',"")
#		
#		#print "unique:"+unique_id+" , parent:"+parent_id
#		query='INSERT INTO '+self.tabla+' VALUES ("'+ID+'",'+unique_id+','+parent_id+',"'+abstr+'"'+')'
#		try:
#			self.cursor.execute(query)
#			self.conn.commit()

#		except Exception as error:
#			print error
#			print "\t"+query
