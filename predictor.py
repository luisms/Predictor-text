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
    archivo = archivo.replace(')','')
    archivo = archivo.replace('(','')
    #archivo = archivo.replace(patron,'')    
    archivo = patron.sub('',archivo)    
    return archivo.lower()
#quita las entradas vacias del diccionario



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

def unigramLetras(archivo):
    a = 0
    diccionario = {}    
    patron2 = re.compile("\w")
    total = (len(patron2.findall(archivo)))        
    for i in "abcdefghijklmnñopqrstuvwxyz":
        patron = re.compile(i)            
        a += len(patron.findall(archivo))        
        diccionario[i]=(len(patron.findall(archivo))/total)
    return (diccionario)


def bigramLetras(archivo):
    a = 0
    diccionario = {}        
    for i in "abcdefghijklmnñopqrstuvwxyz":
        patronIni = re.compile(i)
        for j in "abcdefghijklmnñopqrstuvwxyz":        
            patron = re.compile(i+j)    #crea patron de busqueda        
            a += len(patron.findall(archivo))#busca todas las letras del texto                        
            diccionario[i+j]=(len(patron.findall(archivo)))/ len(patronIni.findall(archivo))
    #diccionario = limpia(diccionario)    
    return (diccionario)
    

def readWords(file1):
    text = open(file1,encoding = 'utf8')
    readW = text.read()
    readW.lower()    
    readW = reemplaza(readW)    
    return readW    

def decodificaBigramLetras(numeros,diccionarioUni,diccionarioBi,teclado):
    numeros= numeros.split(" ")
    texto = []
    posPalabra = 0
    #Recorre los distintos numeros que se encontraban separados por espacios
    for numero in numeros:    
        #Se genera la primera letra a partir del unigramLetras
        valDigito = (teclado.get(int(numero[0])))            
        letraI=valDigito[0]
        frecuenciaI = diccionarioUni.get(valDigito[0])            
        for y in valDigito:
            if(frecuenciaI < diccionarioUni.get(y)):
                letraI=y
                frecuenciaI = diccionarioUni.get(y)
        #Genera el resto de letras con el bigram
        texto.append(letraI)
        posLetra = 0
        for digito in numero[1:]:
            valDigito = (teclado.get(int(digito)))            
            letra=valDigito[0] 
            frecuencia = diccionarioBi.get(texto[posPalabra][posLetra]+letra)                     
            for valor in valDigito:
                if(frecuencia < diccionarioBi.get(texto[posPalabra][posLetra]+valor)):
                    letra=valor
                    frecuencia = diccionarioBi.get(texto[posPalabra][posLetra]+valor)    
            texto[posPalabra]+=letra
            print(posPalabra,posLetra, texto)
            posLetra += 1
        posPalabra += 1

def unigramPalabras(archivo):
	a = 0
	diccionario = {}
	total =archivo.split()     
	for i in range (len(total)):
		if(total [i] in diccionario):
			diccionario[i] = 0
		else:
			diccionario =  diccionario.get(i)+1
	return (diccionario)


###almacenar en diccionari ####

# almacenar un diccionario en un fichero
def guarda (texto):
	with open("unigram", 'w') as f:
    		for key, value in texto.items():
        		f.write('%s:%s\n' % (key, value))
#lee un diccionario de un fichero y lo carga en memoria
def lee():
	data = dict()
	
	with open("unigram") as raw_data:
				
		for item in raw_data:
			if (':' in item):
				key,value = item.split(':', 1)
				data[key]= value[:-1]
	return data



teclado = {}
teclado[2] = ["a","b","c"]
teclado[3] = ["d","e","f"]
teclado[4] = ["g","h","i"]
teclado[5] = ["j","k","l"]
teclado[6] = ["m","n","ñ","o"]
teclado[7] = ["p","q","r","s"]
teclado[8] = ["t","u","v"]
teclado[9] = ["w","x","y","z"]


archivo = readWords("texto")
diccionarioUni=unigramLetras(archivo)
diccionarioBi=bigramLetras(archivo)

numeros = "42782 58346 5847"
(decodificaBigramLetras(numeros,diccionarioUni,diccionarioBi,teclado))
a = unigramLetras(archivo)
guarda(a)
a =  (lee())
print (a.keys())
print (a.values())
