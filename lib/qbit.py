import random
from lucida_symbols import VarSymbol, BuiltInFunctionSymbol, ScopedSymbolTable, BuiltInTypeSymbol

def h_gate(args):
    """Porta Hadamard: Coloca um bit clássico (0 ou 1) em estado de superposição quântica."""
    state = args[0]
    if state in [0, 1]:
        return "superposition"
    return state # Se já estiver em superposição, mantém (em uma simulação simplificada)

def x_gate(args):
    """Porta Pauli-X: O equivalente quântico da porta NOT clássica."""
    state = args[0]
    if state == "superposition": 
        return "superposition"
    return 1 if state == 0 else 0

def measure(args):
    """Medição: Colapsa um Qubit em superposição para um estado clássico (0 ou 1)."""
    state = args[0]
    if state == "superposition":
        return random.choice([0, 1])
    return state

NATIVE_QBIT_MODULE = {
    "h_gate": h_gate,
    "x_gate": x_gate,
    "measure": measure
}

def register_semantics():
    # 1. Tipos (O qbit lida com inteiros e strings de estado, então usamos 'any' para flexibilidade)
    any_type = BuiltInTypeSymbol('any')
    int_type = BuiltInTypeSymbol('int')
    
    # 2. Criando o escopo do módulo 'qbit'
    scope = ScopedSymbolTable(scope_name='qbit', scope_level=2)
    
    # 3. Registrando as portas quânticas
    scope.define(BuiltInFunctionSymbol('h_gate', params=[VarSymbol('estado', any_type)], return_type=any_type))
    scope.define(BuiltInFunctionSymbol('x_gate', params=[VarSymbol('estado', any_type)], return_type=any_type))
    
    # measure sempre colapsa para 0 ou 1 (int)
    scope.define(BuiltInFunctionSymbol('measure', params=[VarSymbol('estado', any_type)], return_type=int_type))
    
    return scope