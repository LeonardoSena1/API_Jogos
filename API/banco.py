# coding: utf-8
import dataset

cnx = "sqlite:///apijogos.db"
dbJogo = "jogos"

class Banco:
	def listJogos(self):
		with dataset.connect(cnx) as db:
			jogos = db[dbJogo].all()
			if db[dbJogo].count() > 0 :
				listaJogos = [dict(id=data['id'],nome=data['nome'], plataforma=data['plataforma'], preco=data['preco']) for data in jogos]
				return listaJogos
			else:
				return False

	def saveJogo(self, data):
		with dataset.connect(cnx) as db:
			return db[dbJogo].insert(dict(nome=data['nome'], plataforma=data['plataforma'], preco=data['preco']))

	def getJogo (self, id):
		with dataset.connect(cnx) as db:
			jogo = db[dbJogo].find_one(id=id)
			
			if jogo:
				return jogo
			else:
				return False

	def updateJogo(self, id, data):
		with dataset.connect(cnx) as db:
			return db[dbJogo].update(dict(id=id, nome=data['nome'], plataforma=data['plataforma'], preco=data['preco']), ['id'])	
			
	def deleteJogo(self, id):
		with dataset.connect(cnx) as db:
			return db[dbJogo].delete( id=id )
