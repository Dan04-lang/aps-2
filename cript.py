import hashlib
import string

alfabeto = (
    string.ascii_lowercase +  # letras minúsculas
    string.ascii_uppercase +  # letras maiúsculas
    string.digits +           # números 0-9
    string.punctuation +      # caracteres especiais !@#$% etc.
    " "                       # espaço em branco
)

LIMITE_CARACTERES = 128

def validar_chave(chave):
    """Garante que a chave não esteja vazia."""
    if not chave:
        raise ValueError("❌ A chave não pode ser vazia.")

def validar_mensagem(mensagem):
    """Garante que a mensagem não ultrapasse o limite."""
    if len(mensagem) > LIMITE_CARACTERES:
        raise ValueError(f"❌ A mensagem não pode ultrapassar {LIMITE_CARACTERES} caracteres.")

def gerar_deslocamentos(chave):
    """
    Gera deslocamentos a partir da chave, aplicando hash MD5.
    Isso aumenta a segurança, evitando dependência direta da chave.
    """
    tamanho = len(alfabeto)
    chave_hash = hashlib.md5(chave.encode("utf-8")).digest()
    deslocs = [b % tamanho for b in chave_hash]
    return deslocs

def criptografar(mensagem, chave):
    """Criptografa a mensagem usando a chave."""
    validar_chave(chave)
    validar_mensagem(mensagem)
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
            resultado.append(c)  # mantém caracteres fora do alfabeto
    return "".join(resultado)

def descriptografar(mensagem, chave):
    """Descriptografa a mensagem usando a chave."""
    validar_chave(chave)
    validar_mensagem(mensagem)
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

# --- Menu interativo ---
if __name__ == "__main__":
    print("=== CIFRA SIMPLES (APS) ===")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Testar (criptografar + descriptografar)")
    print("0 - Sair")

    while True:
        try:
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "0":
                print("Encerrando o programa.")
                break

            mensagem = input("Mensagem: ")
            chave = input("Chave: ")

            if opcao == "1":
                cifrada = criptografar(mensagem, chave)
                print(" CIFRADA:", cifrada)

            elif opcao == "2":
                decifrada = descriptografar(mensagem, chave)
                print(" DECIFRADA:", decifrada)

            elif opcao == "3":
                cifrada = criptografar(mensagem, chave)
                decifrada = descriptografar(cifrada, chave)
                print(" CIFRADA:", cifrada)
                print(" DECIFRADA:", decifrada)
                if mensagem == decifrada:
                    print(" Mensagem recuperada corretamente!")
                else:
                    print(" A mensagem descriptografada não corresponde ao original.")

            else:
                print(" Opção inválida. Escolha 1, 2, 3 ou 0.")

        except Exception as e:
            print("Erro:", e)
