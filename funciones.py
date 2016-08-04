def guiones(palabra):
	guiones=[]
	for letra in palabra:
		guiones.append("_")
	return (guiones)	
def letras(palabra,guiones):
	real= False
	for i in range(len(palabra)):
		if palabra[i] == letra:
		f="A"
		f+= (guiones[i]+"")
		print(f)
			
def ahorcado():
	list=[
	"""______ 
       |     |
       |    
       |   
       |  
       |     
	___|____
	""",
		"""
		______ 
       |     |
       |    ( )
       |   
       |   
       |   
	___|____
	""", 
	"""______ 
       |     |
       |    ( )
       |     |
       |     |
       |      
	___|____

		""",
	"""	______ 
       |     |
       |    ( )
       |   __|
       |     |
       |     
	___|____
		""",
		"""
		_____ 
       |     |
       |    ( )
       |   __|__
       |     |
       |     
	___|____
		""",
		"""
		_____ 
       |     |
       |    ( )
       |   __|__
       |     |
       |    / 
	___|
""",
	""" _____
       |     |
       |    ( )
       |   __|__
       |     |
       |    / \ 
	___|____
"""

	]



