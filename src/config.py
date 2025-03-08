#CONSTANTS

SUBJECTS = ['PROCESO DE DESARROLLO DE SOFTWARE', 'SEMINARIO DE INTEGRACIÓN PROFESIONAL', 'TELEINFORMÁTICA Y REDES', 'INGENIERÍA DE DATOS II', 'PROBABILIDAD Y ESTADÍSTICA', 'APLICACIONES INTERACTIVAS']

#['PROGRAMACION III', 'PARADIGMA ORIENTADO A OBJETOS', 'FUNDAMENTOS DE TELECOMUNIC.', 'INGENIERÍA DE DATOS I', 'CÁLCULO II', 

turnos = {
    "1": '//*[@id="ContentPlaceHolder1_cboTurno"]/option[2]',
    "2": '//*[@id="ContentPlaceHolder1_cboTurno"]/option[3]',
    "3": '//*[@id="ContentPlaceHolder1_cboTurno"]/option[4]'
}

day_index = {
    6: 'LUNES',
    7: 'MARTES',
    8: 'MIERCOLES',
    9: 'JUEVES',
    10: 'VIERNES',
    11: 'SABADO'
}

column_names = ["Código", "Ubicación", "Turno", "DIA", "Hora_Inicio", "Hora_Fin", "Fecha_Inicio", "Fecha_Fin", "VACANTES"]
