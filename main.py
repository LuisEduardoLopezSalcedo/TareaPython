import csv
import sqlite3

def lecturaArchivo(archivo):

    db = sqlite3.connect("Persona.db")
    curSelect = db.cursor()
    curUpdate = db.cursor()
    curInsert = db.cursor()
    
    with open("datos.csv") as documento:
        for fila in documento:
            filaOrganizada = fila.split(";")
            cedula = filaOrganizada[0]
            nombre = filaOrganizada[1]
            edad = filaOrganizada[2]
            profesion = filaOrganizada[3]
            
            consulta = curSelect.execute(f"Select * from datosPersona where cedula = '{cedula}'").fetchall()    
            
            if len(consulta) >= 1: 
                print("ACTUALIZANDO")
                curUpdate.execute(f"UPDATE datosPersona set nombre = '{nombre}', edad = '{edad}', profesion = '{profesion}' where cedula = '{cedula}'") 
                db.commit()
                
            if len(consulta) == 0: 
                print("INSERTANDO")
                curInsert.execute(f"INSERT into datosPersona(cedula,nombre,edad,profesion) VALUES ('{cedula}','{nombre}','{edad}','{profesion}')")
                db.commit()
                
            
           
if __name__ == '__main__':
    
    lecturaArchivo("datos.csv")

    

    
    