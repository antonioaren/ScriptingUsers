import glob
import json
results = open('resultado.json', 'w+')
data={}
data['usuarios']=[]
for filename in glob.iglob('users/**/*.txt', recursive=True):
    # diccionario = {'Nombre':'SinNombre', 'DNI':'SinDNI', 'Correo':'SinCorreo'}
    fileToRead = open(filename).read()
    if 'datos personales' in fileToRead.lower():
            #Posición donde aparece el campo nombre
            nombre_index = fileToRead.lower().find('nombre : ')
            #Posición del pimer salto de linea que aparece despeus de nombre
            nombre = fileToRead.lower().find('\n', nombre_index)
            dni_index = fileToRead.lower().find('dni : ')
            dni = fileToRead.lower().find('\n', dni_index)
            correo_index = fileToRead.lower().find('correo: ')
            correo = fileToRead.lower().find('\n', correo_index)
            data['usuarios'].append({
                'nombre' : fileToRead[nombre_index+9:nombre],
                'dni' : fileToRead[dni_index+6:dni],
                'correo' : fileToRead[correo_index+8:correo]
            })

results.write(json.dumps(data))
