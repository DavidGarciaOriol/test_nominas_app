from nomina import Nomina

nomina1 = Nomina(salario_base=1400, complementos={"turnicidad":40, "antigüedad":30}, retencion=3, numero_pagas=14, antiguedad=True, horas_extra_normales=60, horas_extra_fuerza_mayor=30)
nomina2 = Nomina()


print(nomina1)