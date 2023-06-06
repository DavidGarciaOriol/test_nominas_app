import nomina

nomina1 = nomina.Nomina(salario_base=3000, complementos={"turnicidad":90, "antigüedad":30, "peligrosidad":100}, retencion=6, numero_pagas=14, antiguedad=True)

print(f'''
SALARIO BASE: {nomina1.salario_base} €
COMPLEMENTOS: {list(nomina1.complementos.items())}
DEVENGO: {nomina1.calcular_devengo()} €
\n========================================================\n
ANTIGÜEDAD EN PRORRATEO PAGA EXTRA? -> {nomina1.antiguedad}
PRORRATEO PAGA EXTRA: {nomina1.prorratear_paga_extra()} €
\n========================================================\n
BASE DE COTIZACIÓN - CC: {nomina1.calcular_base_de_cotizacion_contingencias_comunes()} €
BASE DE COTIZACIÓN - CP: {nomina1.calcular_base_de_cotizacion_contingencias_profesionales()} €
BASE HACIENDA: {nomina1.calcular_base_hacienda()} €
\n========================================================\n
DEDUCCIÓN CC: {nomina1.calcular_deducciones_cc()} €
DEDUCCIÓN FP: {nomina1.calcular_deducciones_fp()} €
DEDUCCIÓN DP: {nomina1.calcular_deducciones_dp()} €
\n========================================================\n
LÍQUIDO A PERCIBIR: {nomina1.calcular_liquido_a_percibir()} €''') 