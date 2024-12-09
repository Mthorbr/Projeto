import sqlite3
from datetime import datetime

class BancoDados:
    def __init__(self):
        self.conn = sqlite3.connect('fazenda_citricos.db')
        self.criar_tabelas()
    
    def criar_tabelas(self):
        cursor = self.conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS frutas (
            nome TEXT PRIMARY KEY,
            quantidade REAL,
            ultima_colheita TEXT
        )''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS arvores (
            tipo_fruta TEXT PRIMARY KEY,
            numero_fileiras INTEGER,
            arvores_por_fileira INTEGER,
            ultima_irrigacao TEXT,
            ultima_fertilizacao TEXT
        )''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS areas (
            tipo_fruta TEXT PRIMARY KEY,
            hectares REAL
        )''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS colheitas (
            tipo_fruta TEXT,
            quantidade REAL,
            data TEXT
        )''')
        
        self.conn.commit()
    
    def salvar_fruta(self, nome, quantidade=0, ultima_colheita=None):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO frutas VALUES (?, ?, ?)',
                      (nome, quantidade, ultima_colheita))
        self.conn.commit()
    
    def salvar_arvores(self, tipo_fruta, fileiras, arvores_por_fileira, ultima_irrigacao=None, ultima_fertilizacao=None):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO arvores VALUES (?, ?, ?, ?, ?)',
                      (tipo_fruta, fileiras, arvores_por_fileira, ultima_irrigacao, ultima_fertilizacao))
        self.conn.commit()
    
    def salvar_area(self, tipo_fruta, hectares):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO areas VALUES (?, ?)',
                      (tipo_fruta, hectares))
        self.conn.commit()
    
    def adicionar_colheita(self, tipo_fruta, quantidade):
        cursor = self.conn.cursor()
        data = datetime.now().isoformat()
        cursor.execute('INSERT INTO colheitas VALUES (?, ?, ?)',
                      (tipo_fruta, quantidade, data))
        self.conn.commit()
    
    def obter_info_fruta(self, tipo_fruta):
        cursor = self.conn.cursor()
        info = {}
        
        # Informações da fruta
        cursor.execute('SELECT * FROM frutas WHERE nome = ?', (tipo_fruta,))
        fruta = cursor.fetchone()
        if fruta:
            info['quantidade'] = fruta[1]
            info['ultima_colheita'] = fruta[2]
        
        # Informações das árvores
        cursor.execute('SELECT * FROM arvores WHERE tipo_fruta = ?', (tipo_fruta,))
        arvore = cursor.fetchone()
        if arvore:
            info['total_arvores'] = arvore[1] * arvore[2]
            info['ultima_irrigacao'] = arvore[3]
            info['ultima_fertilizacao'] = arvore[4]
        
        # Informações da área
        cursor.execute('SELECT hectares FROM areas WHERE tipo_fruta = ?', (tipo_fruta,))
        area = cursor.fetchone()
        if area:
            info['area'] = area[0]
        
        # Média de colheitas
        cursor.execute('SELECT AVG(quantidade) FROM colheitas WHERE tipo_fruta = ?', (tipo_fruta,))
        media = cursor.fetchone()[0]
        info['media_colheita'] = media if media else 0.0
        
        return info
    
    def atualizar_irrigacao(self, tipo_fruta):
        cursor = self.conn.cursor()
        data = datetime.now().isoformat()
        cursor.execute('UPDATE arvores SET ultima_irrigacao = ? WHERE tipo_fruta = ?',
                      (data, tipo_fruta))
        self.conn.commit()
    
    def atualizar_fertilizacao(self, tipo_fruta):
        cursor = self.conn.cursor()
        data = datetime.now().isoformat()
        cursor.execute('UPDATE arvores SET ultima_fertilizacao = ? WHERE tipo_fruta = ?',
                      (data, tipo_fruta))
        self.conn.commit()
    
    def listar_frutas(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT nome FROM frutas')
        return [row[0] for row in cursor.fetchall()]