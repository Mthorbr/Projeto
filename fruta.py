from datetime import datetime
from typing import Dict

class Fruta:
    def __init__(self, nome: str, quantidade: float = 0):
        self._nome = nome
        self._quantidade = quantidade
        self._ultima_colheita = None
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def quantidade(self) -> float:
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor: float):
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa")
        self._quantidade = valor
    
    @property
    def ultima_colheita(self) -> datetime:
        return self._ultima_colheita
    
    @ultima_colheita.setter
    def ultima_colheita(self, data: datetime):
        self._ultima_colheita = data
    
    def __str__(self) -> str:
        return f"{self.nome}: {self.quantidade}kg"