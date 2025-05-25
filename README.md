
# 🔐 Vigenère Crypto

Implementação completa da Cifra de Vigenère, com suporte para:
- 🔸 Cifrar mensagens
- 🔸 Decifrar mensagens
- 🔍 Realizar ataque de análise de frequência para quebra da cifra

## 🚀 Funcionalidades

- 📜 Cifra e decifra mensagens usando chave alfabética
- 🕵️ Descobre a chave e decifra mensagens cifradas utilizando análise de frequência

## 🛠️ Tecnologias

- Python 3 (100% puro, sem dependências externas)

## 📂 Estrutura

```
src/vigenere.py           # Código principal da cifra
tests/test_vigenere.py    # Testes simples de funcionamento
```

## 🏃‍♂️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/vigenere-crypto.git
cd vigenere-crypto
```

2. Execute o código:

```bash
python src/vigenere.py
```

3. Teste a cifra manualmente ou rode os testes:

```bash
python tests/test_vigenere.py
```

## ✅ Exemplos

```python
from src.vigenere import cifrar_vigenere, decifrar_vigenere, ataque_vigenere

mensagem = "SEGURANCA COMPUTACIONAL"
chave = "CRYPTO"

cifrado = cifrar_vigenere(mensagem, chave)
print("Cifrado:", cifrado)

decifrado = decifrar_vigenere(cifrado, chave)
print("Decifrado:", decifrado)

chave_recuperada, texto_recuperado = ataque_vigenere(cifrado)
print("Chave encontrada:", chave_recuperada)
print("Texto decifrado pelo ataque:", texto_recuperado)
```

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
