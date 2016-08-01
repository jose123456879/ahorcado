def guiones(palabra):
	guiones=[]
	for letra in palabra:
		guiones.append("_")
	return (guiones)	
def letras(palabra,guiones):
	real=false
	for i in range(len(palabra)):
		if list(palabra[p])==letra:
			real=true

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
	___|____


	]



