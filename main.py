from nomina import Nomina

nomina1 = Nomina(salario_base=3000, complementos={"antigüedad":80}, retencion=4, numero_pagas=14, antiguedad=True, horas_extra_normales=150, horas_extra_fuerza_mayor=0)
nomina2 = Nomina(salario_base=3200, complementos={"antigüedad":90, "Peligrosidad":20, "Turnicidad":40}, retencion=3, numero_pagas=12, antiguedad=True, horas_extra_normales=100, horas_extra_fuerza_mayor=50)


print(nomina1, "\n\n==================================\n==================================\n\n", nomina2)