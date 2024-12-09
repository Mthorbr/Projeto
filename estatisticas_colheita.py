from typing import Dict
from datetime import datetime

class EstatisticasColheita:
    def __init__(self):
        self._colheitas: Dict[str, list] = {}
    
    def adicionar_colheita(self, tipo_fruta: str, quantidade: float):
        if tipo_fruta not in self._colheitas:
            self._colheitas[tipo_fruta] = []
        self._colheitas[tipo_fruta].append(quantidade)
    
    def obter_media(self, tipo_fruta: str) -> float:
        if tipo_fruta not in self._colheitas or not self._colheitas[tipo_fruta]:
            return 0.0
        return sum(self._colheitas[tipo_fruta]) / len(self._colheitas[tipo_fruta])
    
    def __str__(self) -> str:
        resultado = "Médias de Colheita:\n"
        for tipo_fruta, colheitas in self._colheitas.items():
            media = self.obter_media(tipo_fruta)
            resultado += f"{tipo_fruta}: {media:.2f}kg\n"
        return resultado