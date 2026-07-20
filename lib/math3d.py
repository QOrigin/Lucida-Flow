import math
from lucida_symbols import VarSymbol, BuiltInFunctionSymbol, ScopedSymbolTable, BuiltInTypeSymbol

def dist2d(args):
    """Calcula a distância entre dois pontos (x1, y1) e (x2, y2). Ex: [x1, y1, x2, y2]"""
    return math.hypot(args[2] - args[0], args[3] - args[1])

def dot_product(args):
    """Produto Escalar entre dois vetores 3D. Ex: [[x1,y1,z1], [x2,y2,z2]]"""
    v1, v2 = args[0], args[1]
    return sum(a * b for a, b in zip(v1, v2))

def cross_product(args):
    """Produto Vetorial entre dois vetores 3D."""
    v1, v2 = args[0], args[1]
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def normalize(args):
    """Normaliza um vetor 3D (tamanho igual a 1)."""
    v = args[0]
    magnitude = math.sqrt(sum(x**2 for x in v))
    if magnitude == 0: return [0, 0, 0]
    return [x / magnitude for x in v]

NATIVE_MATH3D_MODULE = {
    "dist2d": dist2d,
    "dot": dot_product,
    "cross": cross_product,
    "normalize": normalize
}

def register_semantics():
    # 1. Definindo os tipos básicos que vamos usar
    list_type = BuiltInTypeSymbol('list')
    float_type = BuiltInTypeSymbol('float')
    
    # 2. Criando o escopo do módulo 'math3d'
    scope = ScopedSymbolTable(scope_name='math3d', scope_level=2)
    
    # 3. Registrando as funções matemáticas e suas assinaturas
    # dist2d recebe uma lista [x1, y1, x2, y2] e retorna float
    scope.define(BuiltInFunctionSymbol('dist2d', params=[VarSymbol('coords', list_type)], return_type=float_type))
    
    # dot e cross recebem dois vetores (listas)
    scope.define(BuiltInFunctionSymbol('dot', params=[VarSymbol('v1', list_type), VarSymbol('v2', list_type)], return_type=float_type))
    scope.define(BuiltInFunctionSymbol('cross', params=[VarSymbol('v1', list_type), VarSymbol('v2', list_type)], return_type=list_type))
    
    # normalize recebe um vetor e retorna outro vetor
    scope.define(BuiltInFunctionSymbol('normalize', params=[VarSymbol('v', list_type)], return_type=list_type))
    
    return scope