''' archivos de ancho fijo

    id_persona : int
    tipo: char(e/s) entra/salida
    datetime: (dd/mmm/yyyy) yyyy/mmm/dd hh:mm:ss

    esta logica se usaba cuando el espacio era limitado

'''

def fixed_width_parser(datos):
    lst = [
    "{0:05d}".format(datos[0]),
    datos[1],
    "".join(datos[2].split("/")),
    "".join(datos[3].split(":")),
    ]
    str_list = "".join(lst)
    return str_list



datos = [10, "e", "10/MAY/2019", "07:15:30"]

str_datos = fixed_width_parser(datos)

with open("entr_sal.txt", "w") as out_s:
    out_s.write(str_datos)

with open("entr_sal.txt", "r") as int_s:
    data_int = int_s.read()

#print(data_int)

# transformar la data a formato legible

#00010e10MAY2019071530

def fixed_width_reader(data_int):
    lst_out = [
    int(data_int[0:5]),
    data_int[5],
    "/".join([data_int[6:8],data_int[8:11],data_int[11:15]]),
    ":".join([data_int[15:17],data_int[17:19],data_int[19:21]]),
    
    ]
    print(lst_out)


fixed_width_reader(data_int)

