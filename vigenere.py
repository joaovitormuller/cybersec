
import re
from collections import Counter


def limpar_texto(texto):
    return re.sub('[^A-Za-z]', '', texto).upper()


def gerar_keystream(texto, chave):
    chave = limpar_texto(chave)
    return (chave * (len(texto) // len(chave) + 1))[:len(texto)]


def cifrar_vigenere(mensagem, chave):
    mensagem = limpar_texto(mensagem)
    keystream = gerar_keystream(mensagem, chave)
    cifrado = ""

    for m, k in zip(mensagem, keystream):
        m_val = ord(m) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = (m_val + k_val) % 26
        cifrado += chr(c_val + ord('A'))

    return cifrado


def decifrar_vigenere(cifrado, chave):
    cifrado = limpar_texto(cifrado)
    keystream = gerar_keystream(cifrado, chave)
    mensagem = ""

    for c, k in zip(cifrado, keystream):
        c_val = ord(c) - ord('A')
        k_val = ord(k) - ord('A')
        m_val = (c_val - k_val + 26) % 26
        mensagem += chr(m_val + ord('A'))

    return mensagem


frequencia_portugues = {
    'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57,
    'F': 1.02, 'G': 1.30, 'H': 1.28, 'I': 6.18, 'J': 0.40,
    'K': 0.02, 'L': 2.78, 'M': 4.74, 'N': 5.05, 'O': 10.73,
    'P': 2.52, 'Q': 1.20, 'R': 6.53, 'S': 7.81, 'T': 4.34,
    'U': 4.63, 'V': 1.67, 'W': 0.01, 'X': 0.21, 'Y': 0.01,
    'Z': 0.47
}


def indice_coincidencia(texto):
    N = len(texto)
    contagem = Counter(texto)
    ic = sum(f * (f - 1) for f in contagem.values()) / (N * (N - 1)) if N > 1 else 0
    return ic


def estimar_tamanho_chave(cifrado, max_tamanho=20):
    ic_teorico = 0.065
    melhores = []

    for tamanho in range(1, max_tamanho + 1):
        grupos = ['' for _ in range(tamanho)]
        for i, letra in enumerate(cifrado):
            grupos[i % tamanho] += letra

        ic_medio = sum(indice_coincidencia(grupo) for grupo in grupos) / tamanho
        melhores.append((tamanho, ic_medio))

    melhores.sort(key=lambda x: abs(x[1] - ic_teorico))
    return melhores[0][0]


def ataque_vigenere(cifrado, idioma='PT'):
    cifrado = limpar_texto(cifrado)

    if idioma == 'PT':
        freq_ref = frequencia_portugues
    else:
        raise ValueError("Idioma não suportado. Use 'PT'.")

    tamanho_chave = estimar_tamanho_chave(cifrado)
    print(f"Estimativa de tamanho da chave: {tamanho_chave}")

    grupos = ['' for _ in range(tamanho_chave)]
    for i, letra in enumerate(cifrado):
        grupos[i % tamanho_chave] += letra

    chave = ''
    for grupo in grupos:
        melhor_score = float('-inf')
        melhor_deslocamento = 0

        for deslocamento in range(26):
            texto_tentativo = ''.join(
                chr((ord(c) - ord('A') - deslocamento + 26) % 26 + ord('A')) for c in grupo
            )
            contagem = Counter(texto_tentativo)
            total = sum(contagem.values())

            score = sum(
                (contagem.get(chr(ord('A') + i), 0) / total) * freq_ref[chr(ord('A') + i)]
                for i in range(26)
            )

            if score > melhor_score:
                melhor_score = score
                melhor_deslocamento = deslocamento

        chave += chr((melhor_deslocamento % 26) + ord('A'))

    mensagem = decifrar_vigenere(cifrado, chave)
    return chave, mensagem


if __name__ == "__main__":
    texto_original = "SEGURANCA COMPUTACIONAL"
    chave = "CRYPTO"

    cifrado = cifrar_vigenere(texto_original, chave)
    print(f"Texto Cifrado: {cifrado}")

    decifrado = decifrar_vigenere(cifrado, chave)
    print(f"Texto Decifrado: {decifrado}")

    print("\n--- ATAQUE ---")
    chave_recuperada, mensagem_recuperada = ataque_vigenere(cifrado)
    print(f"Chave Descoberta: {chave_recuperada}")
    print(f"Mensagem Decifrada: {mensagem_recuperada}")
