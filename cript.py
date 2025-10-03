# cifra_simples.py
# Cifra simples inspirada em Vigenère com suporte a letras latinas e cirílicas

alfabeto = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
)

def validar_chave(chave):
    """Garante que a chave não esteja vazia."""
    if not chave:
        raise ValueError("A chave não pode ser vazia.")

def gerar_deslocamentos(chave):
    """Gera deslocamentos a partir da chave."""
    tamanho = len(alfabeto)
    deslocs = []
    for c in chave:
        if c in alfabeto:
            pos = alfabeto.index(c)
            deslocs.append(pos)
        else:
            # caracteres fora do alfabeto são convertidos pelo ord()
            deslocs.append(ord(c) % tamanho)
    return deslocs

def criptografar(mensagem, chave):
    """Criptografa a mensagem usando a chave."""
    validar_chave(chave)
    deslocs = gerar_deslocamentos(chave)
    tamanho_alf = len(alfabeto)
    chave_len = len(deslocs)
    
    resultado = []
    for i, c in enumerate(mensagem):
        if c in alfabeto:
            pos = alfabeto.index(c)
            desloc = deslocs[i % chave_len]
            nova_pos = (pos + desloc) % tamanho_alf
            resultado.append(alfabeto[nova_pos])
        else:
            resultado.append(c)  # mantém espaços, números, pontuação
    return "".join(resultado)

def descriptografar(mensagem, chave):
    """Descriptografa a mensagem usando a chave."""
    validar_chave(chave)
    deslocs = gerar_deslocamentos(chave)
    tamanho_alf = len(alfabeto)
    chave_len = len(deslocs)
    
    resultado = []
    for i, c in enumerate(mensagem):
        if c in alfabeto:
            pos = alfabeto.index(c)
            desloc = deslocs[i % chave_len]
            nova_pos = (pos - desloc) % tamanho_alf
            resultado.append(alfabeto[nova_pos])
        else:
            resultado.append(c)
    return "".join(resultado)

# --- Teste rápido ---
if __name__ == "__main__":
    mensagem = input("Mensagem: ")
    chave = input("Chave: ")

    cifrada = criptografar(mensagem, chave)
    print("CIFRADA:", cifrada)

    decifrada = descriptografar(cifrada, chave)
    print("DECIFRADA:", decifrada)
