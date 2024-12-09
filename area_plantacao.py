class AreaPlantacao:
    def __init__(self, hectares: float):
        self._hectares = hectares
    
    @property
    def hectares(self) -> float:
        return self._hectares
    
    @hectares.setter
    def hectares(self, valor: float):
        if valor <= 0:
            raise ValueError("A área deve ser maior que 0")
        self._hectares = valor
    
    def __str__(self) -> str:
        return f"Área de plantação: {self.hectares} hectares"