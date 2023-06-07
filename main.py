import nomina

nomina1 = nomina.Nomina(salario_base=1400, complementos={"turnicidad":40, "antigüedad":30}, retencion=3, numero_pagas=14, antiguedad=True, horas_extra_normales=60)


def mostrar_nomina(nomina:nomina.Nomina):

    print(f'''
    SALARIO BASE: {nomina.salario_base} €
    COMPLEMENTOS: {list(nomina.complementos.items())}
    HORAS EXTRA NORMALES: {nomina.horas_extra_normales} €
    HORAS EXTRA FUERZA MAYOR: {nomina.horas_extra_fuerza_mayor} €
    DEVENGO: {nomina.calcular_devengo()} €
    \n========================================================\n
    ANTIGÜEDAD EN PRORRATEO PAGA EXTRA? -> {nomina.antiguedad}
    PRORRATEO PAGA EXTRA: {nomina.prorratear_paga_extra()} €
    \n========================================================\n
    BASE DE COTIZACIÓN - CC: {nomina.calcular_base_de_cotizacion_contingencias_comunes()} €
    BASE DE COTIZACIÓN - CP: {nomina.calcular_base_de_cotizacion_contingencias_profesionales()} €
    BASE HACIENDA: {nomina.calcular_base_hacienda()} €
    \n========================================================\n
    DEDUCCIÓN CC: {nomina.CC}% = {nomina.calcular_deducciones_cc()} €
    DEDUCCIÓN FP: {nomina.FP}% = {nomina.calcular_deducciones_fp()} €
    DEDUCCIÓN DP: {nomina.DP}% = {nomina.calcular_deducciones_dp()} €
    DEDUCCIÓN HEN: {nomina.HEN}% = {nomina.calcular_deducciones_horas_extra_normales()} €
    DEDUCCIÓN HEFM: {nomina.HEFM}% = {nomina.calcular_deducciones_horas_extra_fuerza_mayor()} €
    \n========================================================\n
    RETENCIÓN IRPF: {nomina.retencion}% = {nomina.calcular_retenciones_irpf()}
    \n========================================================\n
    LÍQUIDO A PERCIBIR: {nomina.calcular_liquido_a_percibir()} €''')

    return

mostrar_nomina(nomina1)