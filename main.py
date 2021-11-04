from datetime import date

import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

#se podrìa omitir la línea siguiente (emp_no,apellido,oficio,dir,fecha_alt,salario, comision,dept_no)  dado que están todas las columnas
# también se puede quitar alguna columns  "(emp_no, oficio,dir,fecha_alt,salario, comision,dept_no) "
#  VALUES (:P1, :P3, :P4, to_date(:P5,'dd-mm-yyyy'), :P6, :P7, :P8)
# datosEmpleados = (1111,  'Programado', 7566, '4-6-1976', 100000, 100, 20), quitado el apellido
    ConsultaAlta = ("INSERT INTO emp "
                    "(emp_no,apellido,oficio,dir,fecha_alt,salario, comision,dept_no) "
#                    "VALUES (:P1, :P2, :P3, :P4, to_date(:P5,'dd-mm-yyyy'), :P6, :P7, :P8)")
                    "VALUES (:P1, :P2, :P3, :P4, :P5, :P6, :P7, :P8)")

    datosEmpleados = (1112, 'Benito', 'Programado', 7566, date(1976, 6, 4), 100000, 100, 20)
#    datosEmpleados = (1111, 'Benito', 'Programado', 7566, '4-6-1976', 100000, 100, 20)

    cursor.execute(ConsultaAlta, datosEmpleados)

    connection.commit()




except connection.Error as error:
    print("Error: ", error)

connection.close()