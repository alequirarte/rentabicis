import csv


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



def graba_diccionario_id(diccionario:dict,llave_dict:str,archivo:str):
    with open(archivo,'w', encoding="utf8") as fh: #fh = file handle
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

