import tkinter as tk
from tkinter import ttk, messagebox
from models.banco_dados import BancoDados
from datetime import datetime

class InterfaceCitricos:
    def __init__(self):
        self.db = BancoDados()
        
        self.janela = tk.Tk()
        self.janela.title("Sistema de Gerenciamento de Fazenda de Cítricos")
        self.janela.configure(bg='white')
        
        # Configurar tela cheia
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")
        
        # Estilo dos widgets
        style = ttk.Style()
        style.configure('TButton', background='green', foreground='black', padding=10)
        style.configure('TLabel', background='white', foreground='black', font=('Arial', 12))
        style.configure('TEntry', background='white', foreground='black', font=('Arial', 12))
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        
        self.criar_widgets()
    
    def criar_widgets(self):
        # Container principal
        container = ttk.Frame(self.janela, padding="20")
        container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)
        
        # Título
        titulo = ttk.Label(container, text="Sistema de Gerenciamento de Fazenda de Cítricos", 
                          style='Header.TLabel')
        titulo.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Frame esquerdo - Cadastros
        frame_esquerdo = ttk.LabelFrame(container, text="Cadastros", padding="10")
        frame_esquerdo.grid(row=1, column=0, padx=10, sticky=(tk.N, tk.S))
        
        # Adicionar Fruta
        ttk.Label(frame_esquerdo, text="Nova Fruta").grid(row=0, column=0, pady=5)
        self.nome_fruta = ttk.Entry(frame_esquerdo, width=30)
        self.nome_fruta.grid(row=1, column=0, pady=5)
        ttk.Button(frame_esquerdo, text="Adicionar Fruta", 
                  command=self.adicionar_fruta).grid(row=2, column=0, pady=10)
        
        # Adicionar Árvores
        ttk.Label(frame_esquerdo, text="Número de Fileiras").grid(row=3, column=0, pady=5)
        self.fileiras = ttk.Entry(frame_esquerdo, width=30)
        self.fileiras.grid(row=4, column=0, pady=5)
        
        ttk.Label(frame_esquerdo, text="Árvores por Fileira").grid(row=5, column=0, pady=5)
        self.arvores_por_fileira = ttk.Entry(frame_esquerdo, width=30)
        self.arvores_por_fileira.grid(row=6, column=0, pady=5)
        
        ttk.Button(frame_esquerdo, text="Adicionar Árvores", 
                  command=self.adicionar_arvores).grid(row=7, column=0, pady=10)
        
        # Frame central - Registros
        frame_central = ttk.LabelFrame(container, text="Registros", padding="10")
        frame_central.grid(row=1, column=1, padx=10, sticky=(tk.N, tk.S))
        
        # Definir Área
        ttk.Label(frame_central, text="Área (hectares)").grid(row=0, column=0, pady=5)
        self.hectares = ttk.Entry(frame_central, width=30)
        self.hectares.grid(row=1, column=0, pady=5)
        ttk.Button(frame_central, text="Definir Área", 
                  command=self.definir_area).grid(row=2, column=0, pady=10)
        
        # Registrar Colheita
        ttk.Label(frame_central, text="Quantidade Colhida (kg)").grid(row=3, column=0, pady=5)
        self.quantidade = ttk.Entry(frame_central, width=30)
        self.quantidade.grid(row=4, column=0, pady=5)
        ttk.Button(frame_central, text="Registrar Colheita", 
                  command=self.registrar_colheita).grid(row=5, column=0, pady=10)
        
        # Frame direito - Ações
        frame_direito = ttk.LabelFrame(container, text="Ações", padding="10")
        frame_direito.grid(row=1, column=2, padx=10, sticky=(tk.N, tk.S))
        
        # Seleção de frutas
        ttk.Label(frame_direito, text="Selecione a Fruta").grid(row=0, column=0, pady=5)
        self.frutas_combo = ttk.Combobox(frame_direito, state="readonly", width=30)
        self.frutas_combo.grid(row=1, column=0, pady=5)
        
        # Botões de ação
        ttk.Button(frame_direito, text="Registrar Irrigação", 
                  command=self.registrar_irrigacao).grid(row=2, column=0, pady=10)
        ttk.Button(frame_direito, text="Registrar Fertilização", 
                  command=self.registrar_fertilizacao).grid(row=3, column=0, pady=10)
        ttk.Button(frame_direito, text="Visualizar Informações", 
                  command=self.visualizar_informacoes).grid(row=4, column=0, pady=10)
        
        # Configurar pesos das colunas
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)
        
        self.atualizar_lista_frutas()
    
    def atualizar_lista_frutas(self):
        frutas = self.db.listar_frutas()
        self.frutas_combo['values'] = frutas
        if frutas:
            self.frutas_combo.set(frutas[0])
    
    def adicionar_fruta(self):
        nome = self.nome_fruta.get()
        if nome:
            self.db.salvar_fruta(nome)
            messagebox.showinfo("Sucesso", f"Fruta {nome} adicionada com sucesso!")
            self.nome_fruta.delete(0, tk.END)
            self.atualizar_lista_frutas()
        else:
            messagebox.showerror("Erro", "Por favor, digite o nome da fruta")
    
    def adicionar_arvores(self):
        tipo_fruta = self.frutas_combo.get()
        try:
            fileiras = int(self.fileiras.get())
            arvores = int(self.arvores_por_fileira.get())
            self.db.salvar_arvores(tipo_fruta, fileiras, arvores)
            messagebox.showinfo("Sucesso", "Árvores adicionadas com sucesso!")
            self.fileiras.delete(0, tk.END)
            self.arvores_por_fileira.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite números válidos")
    
    def definir_area(self):
        tipo_fruta = self.frutas_combo.get()
        try:
            hectares = float(self.hectares.get())
            self.db.salvar_area(tipo_fruta, hectares)
            messagebox.showinfo("Sucesso", "Área definida com sucesso!")
            self.hectares.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido")
    
    def registrar_colheita(self):
        tipo_fruta = self.frutas_combo.get()
        try:
            quantidade = float(self.quantidade.get())
            self.db.adicionar_colheita(tipo_fruta, quantidade)
            messagebox.showinfo("Sucesso", "Colheita registrada com sucesso!")
            self.quantidade.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido")
    
    def registrar_irrigacao(self):
        tipo_fruta = self.frutas_combo.get()
        self.db.atualizar_irrigacao(tipo_fruta)
        messagebox.showinfo("Sucesso", "Irrigação registrada com sucesso!")
    
    def registrar_fertilizacao(self):
        tipo_fruta = self.frutas_combo.get()
        self.db.atualizar_fertilizacao(tipo_fruta)
        messagebox.showinfo("Sucesso", "Fertilização registrada com sucesso!")
    
    def visualizar_informacoes(self):
        tipo_fruta = self.frutas_combo.get()
        info = self.db.obter_info_fruta(tipo_fruta)
        
        mensagem = f"=== Informações para {tipo_fruta} ===\n\n"
        if 'quantidade' in info:
            mensagem += f"Quantidade atual: {info['quantidade']}kg\n"
        if 'total_arvores' in info:
            mensagem += f"Total de árvores: {info['total_arvores']}\n"
        if 'area' in info:
            mensagem += f"Área de plantação: {info['area']} hectares\n"
        if 'media_colheita' in info:
            mensagem += f"Média de colheita: {info['media_colheita']:.2f}kg\n"
        if 'ultima_colheita' in info and info['ultima_colheita']:
            mensagem += f"Última colheita: {info['ultima_colheita']}\n"
        if 'ultima_irrigacao' in info and info['ultima_irrigacao']:
            mensagem += f"Última irrigação: {info['ultima_irrigacao']}\n"
        if 'ultima_fertilizacao' in info and info['ultima_fertilizacao']:
            mensagem += f"Última fertilização: {info['ultima_fertilizacao']}\n"
        
        messagebox.showinfo("Informações", mensagem)
    
    def iniciar(self):
        self.janela.mainloop()