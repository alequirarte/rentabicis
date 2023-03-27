import csv
from passlib.hash import sha256_crypt
from Levenshtein import distance



def lee_archivo_csv(archivo:str)->list:
    '''Lee un archivo CSV y regresa una lista de registros
    '''
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.reader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return lista


def lee_diccionario_csv(archivo:str)->list:
    '''Lee un archivo CSV y regresa un diccionario de diccionarios
    '''
    diccionario = {}
    try:
        with open(archivo,'r',encoding='UTF-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                llave = renglon['usuario']
                diccionario[llave]=renglon
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return diccionario



def lee_diccionario_csv_id(archivo:str)->list:
    '''Lee un archivo CSV y regresa un diccionario de diccionarios
    '''
    diccionario = {}
    try:
        with open(archivo,'r',encoding='UTF-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                llave = renglon['id']
                diccionario[llave]=renglon
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return diccionario



def crea_diccionario(diccionario_peliculas:dict,llave_ext:str)->dict:
    diccionario = {}
    for id,pelicula in diccionario_peliculas.items():
        llave = pelicula[llave_ext]
        if llave not in diccionario:
            diccionario[llave] = [pelicula]
        else:
            diccionario[llave].append(pelicula)
    return diccionario



def graba_diccionario(diccionario:dict,llave_dict:str,archivo:str):
    with open(archivo,'w') as fh: #fh = file handle
        lista_campos = obten_campos(diccionario, llave_dict)
        dw = csv.DictWriter(fh,lista_campos)
        dw.writeheader()
        renglones = []
        for llave, valor_d in diccionario.items():
            d = { 'usuario':llave}
            for key, value  in valor_d.items():
                d[key] = value
            renglones.append(d)
        dw.writerows(renglones)



def graba_diccionario_id(diccionario:dict,llave_dict:str,archivo:str):
    with open(archivo,'w') as fh: #fh = file handle
        lista_campos = obten_campos(diccionario, llave_dict)
        dw = csv.DictWriter(fh,lista_campos)
        dw.writeheader()
        renglones = []
        for llave, valor_d in diccionario.items():
            d = { 'id':llave}
            for key, value  in valor_d.items():
                d[key] = value
            renglones.append(d)
        dw.writerows(renglones)



def obten_campos(diccionario:dict,llave_d:str)->list:
    lista = [llave_d]
    llaves = list(diccionario.keys())
    k = llaves[0]
    nuevo_diccionario = diccionario[k]
    lista_campos = list(nuevo_diccionario.keys())
    lista.extend(lista_campos)
    return lista


#if __name__ == "__main__":
   