import tkinter as tk
from tkinter import messagebox, filedialog

# ==========================================================
# ESTADO GLOBAL DO MÓDULO GUI
# ==========================================================
ROOT = None
WIDGETS = {}
CHECKBOX_VARS = {}
INTERPRETER_REF = None

def _run_lucida_function(function_name):
    if not INTERPRETER_REF: return
    process_obj = INTERPRETER_REF.global_scope.get(function_name)
    if process_obj:
        try:
            from lucida_interpreter import Process
            if isinstance(process_obj, Process):
                INTERPRETER_REF.call_process(process_obj, [])
        except Exception as e:
            messagebox.showerror("Erro de Runtime", str(e))

def _run_lucida_function_com_args(function_name, args):
    if not INTERPRETER_REF: return
    process_obj = INTERPRETER_REF.global_scope.get(function_name)
    if process_obj:
        try:
            from lucida_interpreter import Process
            if isinstance(process_obj, Process):
                INTERPRETER_REF.call_process(process_obj, args)
        except Exception as e:
            messagebox.showerror("Erro de Runtime", str(e))

# ==========================================================
# FUNÇÕES NATIVAS EXPORTADAS
# ==========================================================

# --- JANELA E LOOP ---
def criar_janela(args):
    global ROOT
    if ROOT is not None: return
    ROOT = tk.Tk()
    ROOT.title(args[0])
    ROOT.geometry(args[1])
    return True

def iniciar_loop(args):
    global ROOT, WIDGETS, CHECKBOX_VARS
    if ROOT:
        ROOT.mainloop()
        ROOT = None
        WIDGETS.clear()
        CHECKBOX_VARS.clear()
    return True

# --- WIDGETS BÁSICOS ---
def criar_rotulo(args):
    id_w, texto = args[0], args[1]
    rotulo = tk.Label(ROOT, text=texto, font=("Consolas", 14))
    rotulo.pack(pady=10)
    WIDGETS[id_w] = rotulo
    return True

def criar_botao(args):
    id_w, texto, nome_funcao_lf = args[0], args[1], args[2]
    botao = tk.Button(ROOT, text=texto, font=("Consolas", 12), bg="#1F2937", fg="white",
                      command=lambda: _run_lucida_function(nome_funcao_lf))
    botao.pack(pady=5)
    WIDGETS[id_w] = botao
    return True

def alterar_texto(args):
    id_widget, novo_texto = args[0], args[1]
    if id_widget in WIDGETS:
        texto_formatado = str(novo_texto).replace('\\n', '\n')
        WIDGETS[id_widget].config(text=texto_formatado)
    return True

def agendar_atualizacao(args):
    ms, nome_funcao_lf = int(args[0]), str(args[1])
    if ROOT: ROOT.after(ms, lambda: _run_lucida_function(nome_funcao_lf))
    return True

# --- ENTRADAS E TEXTO ---
def criar_entrada(args):
    id_w = args[0]
    entrada = tk.Entry(ROOT, font=("Consolas", 14), width=20)
    entrada.pack(pady=5)
    WIDGETS[id_w] = entrada
    return True

def obter_texto(args):
    id_w = args[0]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Entry):
        return WIDGETS[id_w].get()
    return ""

def criar_caixa_texto(args):
    id_w = args[0]
    caixa = tk.Text(ROOT, font=("Consolas", 12), height=10, width=40)
    caixa.pack(pady=10, padx=10)
    WIDGETS[id_w] = caixa
    return True

def obter_texto_completo(args):
    id_w = args[0]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Text):
        return WIDGETS[id_w].get("1.0", "end-1c")
    return ""

def definir_texto_completo(args):
    id_w, novo_texto = args[0], args[1]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Text):
        WIDGETS[id_w].delete("1.0", tk.END)
        WIDGETS[id_w].insert("1.0", novo_texto)
    return True

# --- CONTROLES ESPECIAIS ---
def criar_checkbox(args):
    id_w, texto = args[0], args[1]
    var = tk.IntVar()
    checkbox = tk.Checkbutton(ROOT, text=texto, variable=var, font=("Consolas", 12))
    checkbox.pack(pady=2)
    WIDGETS[id_w] = checkbox
    CHECKBOX_VARS[id_w] = var
    return True

def obter_valor_checkbox(args):
    id_w = args[0]
    return CHECKBOX_VARS[id_w].get() if id_w in CHECKBOX_VARS else 0

def criar_slider(args):
    id_w, de, para = args[0], int(args[1]), int(args[2])
    slider = tk.Scale(ROOT, from_=de, to=para, orient="horizontal", length=200)
    slider.pack(pady=5)
    WIDGETS[id_w] = slider
    return True

def obter_valor_slider(args):
    id_w = args[0]
    return int(WIDGETS[id_w].get()) if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Scale) else 0

def criar_rotulo_resultado(args):
    id_w, texto = args[0], args[1]
    rotulo = tk.Label(ROOT, text=texto, font=("Consolas", 16, "bold"), bg="lightgray", fg="black", padx=10, pady=10)
    rotulo.pack(pady=10)
    WIDGETS[id_w] = rotulo
    return True

# --- COMPONENTES DINÂMICOS (LISTAS) ---
def criar_lista(args):
    id_w = args[0]
    frame = tk.Frame(ROOT)
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    lista = tk.Listbox(frame, font=("Consolas", 12), yscrollcommand=scrollbar.set, bg="#0D0E15", fg="#00FFFF", selectbackground="#FF007F")
    scrollbar.config(command=lista.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    WIDGETS[id_w] = lista
    return True

def adicionar_item_lista(args):
    id_w, item = args[0], args[1]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Listbox):
        WIDGETS[id_w].insert(tk.END, item)
    return True

def obter_selecao_lista(args):
    id_w = args[0]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Listbox):
        selecao = WIDGETS[id_w].curselection()
        if selecao: return WIDGETS[id_w].get(selecao[0])
    return ""

def limpar_lista(args):
    id_w = args[0]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Listbox):
        WIDGETS[id_w].delete(0, tk.END)
    return True

# --- CANVAS / DESENHO ---
def criar_tela(args):
    id_w, largura, altura, cor_fundo = args[0], int(args[1]), int(args[2]), args[3]
    tela = tk.Canvas(ROOT, width=largura, height=altura, bg=cor_fundo)
    tela.pack(pady=10, padx=10)
    WIDGETS[id_w] = tela
    return True

def definir_cor_fundo(args):
    id_w, nova_cor = args[0], args[1]
    if id_w in WIDGETS and isinstance(WIDGETS[id_w], tk.Canvas):
        WIDGETS[id_w].config(bg=str(nova_cor))
    return True

def vincular_evento_rato(args):
    id_widget, nome_evento, nome_funcao_lf = args[0], args[1], args[2]
    if id_widget in WIDGETS:
        callback = lambda e: _run_lucida_function_com_args(nome_funcao_lf, [e.x, e.y])
        eventos = {"botao_pressionado": "<Button-1>", "botao_solto": "<ButtonRelease-1>", "movimento": "<B1-Motion>"}
        if nome_evento in eventos: WIDGETS[id_widget].bind(eventos[nome_evento], callback)
    return True

def desenhar_linha(args):
    id_tela, x1, y1, x2, y2, cor = args[0], int(args[1]), int(args[2]), int(args[3]), int(args[4]), args[5]
    if id_tela in WIDGETS and isinstance(WIDGETS[id_tela], tk.Canvas):
        WIDGETS[id_tela].create_line(x1, y1, x2, y2, fill=cor, width=3)
    return True

# --- DIÁLOGOS ---
def salvar_dialogo_ficheiro(args):
    c = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    return c if c else ""

def abrir_dialogo_ficheiro(args):
    c = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return c if c else ""

# ==========================================================
# DICIONÁRIO DE EXPORTAÇÃO E SEMÂNTICA
# ==========================================================
NATIVE_GUI_MODULE = {
    "criar_janela": criar_janela, "iniciar_loop": iniciar_loop, "criar_rotulo": criar_rotulo,
    "criar_botao": criar_botao, "alterar_texto": alterar_texto, "agendar_atualizacao": agendar_atualizacao,
    "criar_entrada": criar_entrada, "obter_texto": obter_texto, "criar_caixa_texto": criar_caixa_texto,
    "obter_texto_completo": obter_texto_completo, "definir_texto_completo": definir_texto_completo,
    "criar_checkbox": criar_checkbox, "obter_valor_checkbox": obter_valor_checkbox,
    "criar_slider": criar_slider, "obter_valor_slider": obter_valor_slider,
    "criar_rotulo_resultado": criar_rotulo_resultado, "criar_lista": criar_lista,
    "adicionar_item_lista": adicionar_item_lista, "obter_selecao_lista": obter_selecao_lista,
    "limpar_lista": limpar_lista, "criar_tela": criar_tela, "vincular_evento_rato": vincular_evento_rato,
    "desenhar_linha": desenhar_linha, "salvar_dialogo_ficheiro": salvar_dialogo_ficheiro,
    "definir_cor_fundo": definir_cor_fundo,
    "abrir_dialogo_ficheiro": abrir_dialogo_ficheiro
}

def register_semantics():
    from lucida_symbols import BuiltInTypeSymbol, ScopedSymbolTable, BuiltInFunctionSymbol, VarSymbol
    s_t, i_t, n_t = BuiltInTypeSymbol('string'), BuiltInTypeSymbol('int'), BuiltInTypeSymbol('null')
    scope = ScopedSymbolTable(scope_name='gui', scope_level=2)
    
    # Registrando assinaturas para o Compilador
    scope.define(BuiltInFunctionSymbol('criar_janela', [VarSymbol('t', s_t), VarSymbol('r', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('iniciar_loop', [], n_t))
    scope.define(BuiltInFunctionSymbol('criar_rotulo', [VarSymbol('i', s_t), VarSymbol('x', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('criar_botao', [VarSymbol('i', s_t), VarSymbol('x', s_t), VarSymbol('c', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('alterar_texto', [VarSymbol('i', s_t), VarSymbol('n', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('agendar_atualizacao', [VarSymbol('m', i_t), VarSymbol('c', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('criar_entrada', [VarSymbol('i', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('obter_texto', [VarSymbol('i', s_t)], s_t))
    scope.define(BuiltInFunctionSymbol('criar_caixa_texto', [VarSymbol('i', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('obter_texto_completo', [VarSymbol('i', s_t)], s_t))
    scope.define(BuiltInFunctionSymbol('definir_texto_completo', [VarSymbol('i', s_t), VarSymbol('n', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('criar_checkbox', [VarSymbol('i', s_t), VarSymbol('x', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('obter_valor_checkbox', [VarSymbol('i', s_t)], i_t))
    scope.define(BuiltInFunctionSymbol('criar_slider', [VarSymbol('i', s_t), VarSymbol('d', i_t), VarSymbol('p', i_t)], n_t))
    scope.define(BuiltInFunctionSymbol('obter_valor_slider', [VarSymbol('i', s_t)], i_t))
    scope.define(BuiltInFunctionSymbol('criar_rotulo_resultado', [VarSymbol('i', s_t), VarSymbol('x', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('criar_lista', [VarSymbol('i', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('adicionar_item_lista', [VarSymbol('i', s_t), VarSymbol('it', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('obter_selecao_lista', [VarSymbol('i', s_t)], s_t))
    scope.define(BuiltInFunctionSymbol('limpar_lista', [VarSymbol('i', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('criar_tela', [VarSymbol('i', s_t), VarSymbol('w', i_t), VarSymbol('h', i_t), VarSymbol('c', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('definir_cor_fundo', [VarSymbol('i', s_t), VarSymbol('c', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('vincular_evento_rato', [VarSymbol('i', s_t), VarSymbol('e', s_t), VarSymbol('c', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('desenhar_linha', [VarSymbol('i', s_t), VarSymbol('x1', i_t), VarSymbol('y1', i_t), VarSymbol('x2', i_t), VarSymbol('y2', i_t), VarSymbol('c', s_t)], n_t))
    scope.define(BuiltInFunctionSymbol('salvar_dialogo_ficheiro', [], s_t))
    scope.define(BuiltInFunctionSymbol('abrir_dialogo_ficheiro', [], s_t))
    
    return scope