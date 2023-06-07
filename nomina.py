class Nomina:

    CC = 4.70 # Contingencias Comunes
    FP = 0.10 # Formación Profesional
    DP = 1.55 # Desempleo
    HEN = 4.70
    HEFM = 2

    retencion = 0
    numero_pagas = 14
    antiguedad = False

    salario_base = 0
    complementos = {}
    horas_extra_normales = 0.0
    horas_extra_fuerza_mayor = 0.0

    def __init__(self, salario_base:float, complementos:dict, retencion:float, numero_pagas:int, antiguedad:bool, horas_extra_normales:float = 0.0, horas_extra_fuerza_mayor:float = 0.0):
        self.salario_base = salario_base
        self.complementos = complementos
        self.retencion = retencion
        self.numero_pagas = numero_pagas
        self.antiguedad = antiguedad
        self.horas_extra_normales = horas_extra_normales
        self.horas_extra_fuerza_mayor = horas_extra_fuerza_mayor

    def existe_complemento_antiguedad(self):
        return self.complementos.get("antigüedad") is not None
        
    def prorratear_paga_extra(self):
        paga_extra_prorrateada = 0
        calc = 0
        calc += self.salario_base
        if self.existe_complemento_antiguedad() and self.antiguedad == True:
            calc += self.complementos['antigüedad']
        
        paga_extra_prorrateada = calc/6
        return paga_extra_prorrateada
    
    def calcular_devengo(self):
        devengo = self.salario_base
        valores_de_complementos = list(self.complementos.values())
        devengo += sum(valores_de_complementos)
        devengo += (self.horas_extra_normales + self.horas_extra_fuerza_mayor)
        
        if self.numero_pagas == 12:
            devengo += self.prorratear_paga_extra()
        
        return devengo
        
    def calcular_base_de_cotizacion_contingencias_comunes(self):
        base_de_cotizacion_cc = 0
        if self.numero_pagas == 14:
            base_de_cotizacion_cc = self.calcular_devengo() + self.prorratear_paga_extra()
        elif self.numero_pagas == 12:
            base_de_cotizacion_cc = self.calcular_devengo()

        base_de_cotizacion_cc -= (self.horas_extra_normales - self.horas_extra_fuerza_mayor)

        return base_de_cotizacion_cc
    
    def calcular_base_de_cotizacion_contingencias_profesionales(self):

        base_de_cotizacion_cp = self.calcular_base_de_cotizacion_contingencias_comunes() + self.horas_extra_normales + self.horas_extra_fuerza_mayor
        return base_de_cotizacion_cp
    
    def calcular_base_hacienda(self):
        base_hacienda = self.calcular_devengo()
        return base_hacienda
    
    def calcular_deducciones_cc(self):
        resultado_cc = self.calcular_base_de_cotizacion_contingencias_comunes() * self.CC / 100
        return resultado_cc

    def calcular_deducciones_fp(self):
        resultado_fp = self.calcular_base_de_cotizacion_contingencias_profesionales() * self.FP / 100
        return resultado_fp

    def calcular_deducciones_dp(self):
        resultado_dp = self.calcular_base_de_cotizacion_contingencias_profesionales() * self.DP / 100
        return resultado_dp
    
    def calcular_deducciones_horas_extra_normales(self):
        resultado_hen = self.horas_extra_normales * self.HEN / 100
        return resultado_hen

    def calcular_deducciones_horas_extra_fuerza_mayor(self):
        resultado_hefm = self.horas_extra_fuerza_mayor * self.HEFM / 100
        return resultado_hefm

    def calcular_retenciones_irpf(self):
        resultado_retenciones = self.calcular_devengo() * self.retencion / 100
        return resultado_retenciones

    def calcular_total_deducciones(self):
        total_deducciones = 0
        total_deducciones += self.calcular_deducciones_cc() 
        total_deducciones += self.calcular_deducciones_fp() 
        total_deducciones += self.calcular_deducciones_dp() 
        total_deducciones += self.calcular_deducciones_horas_extra_normales() 
        total_deducciones += self.calcular_deducciones_horas_extra_fuerza_mayor()

        return total_deducciones
    
    def calcular_liquido_a_percibir(self):
        liquido_a_percibir = self.calcular_devengo() - (self.calcular_total_deducciones() + self.calcular_retenciones_irpf())
        return liquido_a_percibir

    