import re
#elimina del texto caracteres extraños
def reemplaza(archivo):
	patron = re.compile('\d+')
	archivo = archivo.replace(',','')
	archivo = archivo.replace('*','')
	archivo = archivo.replace('?','')
	archivo = archivo.replace('¿','')
	archivo = archivo.replace('!','')
	archivo = archivo.replace('¡','')
	archivo = archivo.replace('á','a')
	archivo = archivo.replace('é','e')
	archivo = archivo.replace('í','i')
	archivo = archivo.replace('ó','o')
	archivo = archivo.replace('ú','u')
	archivo = archivo.replace('.','')
	archivo = archivo.replace('-',' ')
	archivo = archivo.replace('_',' ')	
	archivo = archivo.replace(':',' ')
	archivo = archivo.replace(';',' ')
	archivo = archivo.replace(']','')
	archivo = archivo.replace('[','')
	#archivo = archivo.replace(patron,'')	
	archivo = patron.sub('',archivo)	
	return archivo.lower()
#quita las entradas vacias del diccionario
def limpia( diccionario):
	diccionarioAux = {}
	for i in diccionario:
		if(diccionario.get(i) != 0.0):
			diccionarioAux[i]=diccionario.get(i)	
	return diccionarioAux


#codifica la cadena de numeros para elegir la letra más frecuente
def descomprime(l):
	l = str(l)
	if not l:
		return l
	else:
		prev=l[0]
		cont=1
		res=[]
		for x in l[1:]:
			if x == prev:
				cont+=1
			else:
				res.append([cont,prev] if cont>1 else prev)
				cont = 1
				prev = x
		res.append([cont,prev] if cont>1 else prev)
		return res

def unigram(archivo):
	a = 0
	diccionario = {}	
	patron2 = re.compile("\w")
	total = (len(patron2.findall(archivo)))		
	for i in "abcdefghijklmnñopqrstuvwxyz":
		patron = re.compile(i)			
		a += len(patron.findall(archivo))		
		diccionario[i]=(len(patron.findall(archivo))/total)
	return (diccionario)


def bigram(archivo):
	a = 0
	diccionario = {}	
	patron2 = re.compile("\w")
	total = (len(patron2.findall(archivo)))		
	for i in "abcdefghijklmnñopqrstuvwxyz":
		patronIni = re.compile(i)
		for j in "abcdefghijklmnñopqrstuvwxyz":		
			patron = re.compile(i+j)	#crea patron de busqueda		
			a += len(patron.findall(archivo))#busca todas las letras del texto						
			diccionario[i+j]=(len(patron.findall(archivo)))/ len(patronIni.findall(archivo))
	diccionario = limpia(diccionario)	
	return (diccionario)
	
#metodo principal ##organizarlo


def readWords(file1):
	text = open(file1,encoding = 'utf8')
	readW = text.read()
	readW.lower()	
	readW = reemplaza(readW)	
	return readW	
	
	



def decodifica(numeros,diccionarioUni,diccionarioBi,teclado):
	numeros= numeros.split(" ")	
	for x in numeros:	
		a = (teclado.get(int(x[0])))			
		letraI=a[0]
		frecuenciaI = diccionarioUni.get(a[0])			
		for y in a:
			if(frecuenciaI < diccionarioUni.get(y)):
				letraI=y
				frecuenciaI = diccionarioUni.get(y)
		#print(letra, frecuencia)
		for j in x[1:]:
			a = (teclado.get(int(j)))			
			letra=a[0]
			
			frecuencia = diccionarioBi.get(letraI+letra)			
					
			for z in a:
				if(frecuencia < diccionarioBi.get(letraI+z)):
					letra=z
					frecuencia = diccionarioBi.get(letraI+z)	
			
			print(letraI,letra,frecuencia)

		#for x in (1, numeros):
	#	x
	#return res



teclado = {}
teclado[2] = ["a","b","c"]
teclado[3] = ["d","e","f"]
teclado[4] = ["g","h","i"]
teclado[5] = ["j","k","l"]
teclado[6] = ["m","n","ñ","o"]
teclado[7] = ["p","q","r","s"]
teclado[8] = ["t","u","v"]
teclado[9] = ["w","x","y","z"]


archivo =readWords("texto")
diccionarioUni=unigram(archivo)
diccionarioBi=bigram(archivo)
numeros = "235 87"
(decodifica(numeros,diccionarioUni,diccionarioBi,teclado))
