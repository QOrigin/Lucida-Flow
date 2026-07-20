from datetime import datetime
from lucida_symbols import BuiltInTypeSymbol, ScopedSymbolTable, BuiltInFunctionSymbol

# ==========================================================
# FUNÇÕES NATIVAS EXPORTADAS
# ==========================================================
def obter_hora_atual(args):
    """Retorna a hora atual formatada como HH:MM:SS"""
    return datetime.now().strftime("%H:%M:%S")

# O Dicionário de Exportação
NATIVE_TIME_MODULE = {
    "now": obter_hora_atual
}

# ==========================================================
# REGISTRO SEMÂNTICO (Para o Compilador)
# ==========================================================
def register_semantics():
    string_type = BuiltInTypeSymbol('string')
    
    scope = ScopedSymbolTable(scope_name='time', scope_level=2)
    # Define a função now() que não recebe parâmetros e retorna uma string
    scope.define(BuiltInFunctionSymbol('now', params=[], return_type=string_type))
    
    return scope