from nomina import Nomina

nomina1 = Nomina(salario_base=1400, complementos={"turnicidad":40, "antigüedad":30}, retencion=3, numero_pagas=14, antiguedad=True, horas_extra_normales=60, horas_extra_fuerza_mayor=30)
nomina2 = Nomina(salario_base=3825, complementos={"antigüedad":95}, retencion=18, numero_pagas=14, antiguedad=True, horas_extra_normales=20, horas_extra_fuerza_mayor=20)


print(nomina2)