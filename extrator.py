# Definir o texto que vamos analisar.
texto = "O projeto da Alura para Strings é muito bom, e a Alura é uma excelente plataforma de ensino. Python é a melhor linguagem de programação."

# Criar uma lista com as palavras-chave que queremos encontrar.
palavras_chave = ["Alura", "Python", "programação", "projeto", "ensino"]

# Separar o texto em palavras.
# A função .split() divide o texto onde encontra espaços.
palavras_do_texto = texto.split()

# Criar uma lista vazia para guardar as palavras-chave encontradas.
encontradas = []

# Loop para verificar cada palavra-chave da nossa lista.
for palavra_chave in palavras_chave:
    # A verificação '.lower()' é importante para o código ignorar letras maiúsculas ou minúsculas.
    # Por exemplo, "Alura" será tratada da mesma forma que "alura".
    if palavra_chave.lower() in [palavra.lower() for palavra in palavras_do_texto]:
        encontradas.append(palavra_chave)

# Imprimir o resultado.
print("As palavras-chave encontradas no texto são:", encontradas)  
