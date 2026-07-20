import os
from lucida_symbols import VarSymbol, BuiltInFunctionSymbol, ScopedSymbolTable, BuiltInTypeSymbol

def read_file(args):
    if not os.path.exists(args[0]):
        raise Exception(f"Erro FS: Arquivo '{args[0]}' não encontrado.")
    with open(args[0], 'r', encoding='utf-8') as f:
        return f.read()

def write_file(args):
    with open(args[0], 'w', encoding='utf-8') as f:
        f.write(str(args[1]))
    return True

def exists(args):
    return os.path.exists(args[0])

def delete(args):
    if os.path.exists(args[0]):
        os.remove(args[0])
        return True
    return False

NATIVE_FS_MODULE = {
    "read": read_file,
    "write": write_file,
    "exists": exists,
    "delete": delete
}