class Arvore:
    def __init__(self, tipo_fruta: str, numero_fileiras: int, arvores_por_fileira: int):
        self._tipo_fruta = tipo_fruta
        self._numero_fileiras = numero_fileiras
        self._arvores_por_fileira = arvores_por_fileira
        self._ultima_irrigacao = None
        self._ultima_fertilizacao = None
    
    @property
    def total_arvores(self) -> int:
        return self._numero_fileiras * self._arvores_por_fileira
    
    @property
    def ultima_irrigacao(self):
        return self._ultima_irrigacao
    
    @ultima_irrigacao.setter
    def ultima_irrigacao(self, data):
        self._ultima_irrigacao = data
    
    @property
    def ultima_fertilizacao(self):
        return self._ultima_fertilizacao
    
    @ultima_fertilizacao.setter
    def ultima_fertilizacao(self, data):
        self._ultima_fertilizacao = data
    
    def __str__(self) -> str:
        return f"{self._tipo_fruta} - Total de árvores: {self.total_arvores} ({self._numero_fileiras} fileiras x {self._arvores_por_fileira} árvores)"