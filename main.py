from nomina import Nomina

nomina1 = Nomina(
                salario_base=5000, 
                complementos={
                                "antigüedad":40,
                                "peligrosidad":100,
                                "nocturnidad":60
                                },
                retencion=5, 
                numero_pagas=14, 
                antiguedad=True, 
                horas_extra_normales=50, 
                horas_extra_fuerza_mayor=50, 
                dias_cotizados=30
                )

print(nomina1)