from datetime import datetime
from typing import Dict, List
from .fruta import Fruta
from .arvore import Arvore
from .area_plantacao import AreaPlantacao
from .estatisticas_colheita import EstatisticasColheita

class GerenciadorFazenda:
    def __init__(self):
        self._frutas: Dict[str, Fruta] = {}
        self._arvores: Dict[str, Arvore] = {}
        self._areas: Dict[str, AreaPlantacao] = {}
        self._estatisticas_colheita = EstatisticasColheita()
    
    def adicionar_fruta(self, nome: str, quantidade: float = 0):
        self._frutas[nome] = Fruta(nome, quantidade)
    
    def adicionar_arvores(self, tipo_fruta: str, fileiras: int, arvores_por_fileira: int):
        self._arvores[tipo_fruta] = Arvore(tipo_fruta, fileiras, arvores_por_fileira)
    
    def definir_area(self, tipo_fruta: str, hectares: float):
        self._areas[tipo_fruta] = AreaPlantacao(hectares)
    
    def registrar_colheita(self, tipo_fruta: str, quantidade: float):
        if tipo_fruta not in self._frutas:
            raise ValueError(f"Tipo de fruta desconhecido: {tipo_fruta}")
        
        self._frutas[tipo_fruta].quantidade = quantidade
        self._frutas[tipo_fruta].ultima_colheita = datetime.now()
        self._estatisticas_colheita.adicionar_colheita(tipo_fruta, quantidade)
    
    def registrar_irrigacao(self, tipo_fruta: str):
        if tipo_fruta in self._arvores:
            self._arvores[tipo_fruta].ultima_irrigacao = datetime.now()
    
    def registrar_fertilizacao(self, tipo_fruta: str):
        if tipo_fruta in self._arvores:
            self._arvores[tipo_fruta].ultima_fertilizacao = datetime.now()
    
    def obter_info_fruta(self, tipo_fruta: str) -> dict:
        info = {}
        if tipo_fruta in self._frutas:
            fruta = self._frutas[tipo_fruta]
            info['quantidade'] = fruta.quantidade
            info['ultima_colheita'] = fruta.ultima_colheita
        
        if tipo_fruta in self._arvores:
            arvore = self._arvores[tipo_fruta]
            info['total_arvores'] = arvore.total_arvores
            info['ultima_irrigacao'] = arvore.ultima_irrigacao
            info['ultima_fertilizacao'] = arvore.ultima_fertilizacao
        
        if tipo_fruta in self._areas:
            info['area'] = self._areas[tipo_fruta].hectares
        
        info['media_colheita'] = self._estatisticas_colheita.obter_media(tipo_fruta)
        
        return info