def get_default_det(n=2):
    import pickle as pk
    if n in get_defaults():
        with open(f"determinantes/{n}x{n}.pkl", 'rb') as f:
            expr = pk.load(f)
            f.close()

        return expr
    
    return None

def save_pkl(file, name):
    import pickle as pk
    with open(f"{name}.pkl", 'wb') as f:
        pk.dump(file, f)
        f.close()

def get_symbols_det(n=2):
    import pickle as pk
    if n in get_default_symbols():
        with open(f"determinantes/symbols/{n}x{n}.pkl", 'rb') as f:
            expr = pk.load(f)
            f.close()

        return expr
    
    return None

def get_default_symbols():
    from os import listdir

    files = listdir("determinantes/symbols/")
    defaults = list(map(lambda i: int(i.split('x')[0]), files))

    return defaults

def get_defaults():
    from os import listdir

    files = listdir("determinantes/")
    defaults = list(map(lambda i: int(i[0]), files))

    return defaults