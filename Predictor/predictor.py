import re
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
def cuentaLetras(archivo):
	a = 0
	diccionario = {}	
	patron2 = re.compile("\w")
	total = (len(patron2.findall(archivo)))		
	for i in "abcdefghijklmnñopqrstuvwxyz":
		patron = re.compile(i)			
		a += len(patron.findall(archivo))		
		diccionario[i]=(len(patron.findall(archivo))/total)
		#diccionario[]=3
	print (diccionario)
	#return (diccionario)
	
	
def readWords(file1):
	text = open(file1,encoding = 'utf8')
	readW = text.read()
	readW.lower()	
	information = []
	readW = reemplaza(readW)	
	cuentaLetras(readW)	
	frecuencias = dict
	readW= readW.split()
	frecuencia = dict()
	for i in range(len (readW)):
        	
        ## if ((len(information)) < len(readW)):
             information.append(readW[i])
	return (information)

(readWords("texto"))
