def minimal_palindrome_greedy(s):
    n = len(s)
    contador = 0
    i = 0
    j = n - 1

# Percorre todo a string com dois índices para percorrer a esquerda para direita e da direita para esquerda
    while i < j:
        # Se as letras forem iguais somente atualiza os índices
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            # Heurística gulosa: escolhe o lado que "custa menos"
            if (i + 1 < j) and (s[i+1] == s[j]):
                # Move o ponteiro esquerdo (simula inserção à direita, pois esta opção é mais atrativa a curto prazo)
                contador += 1
                i += 1
            elif (i < j - 1) and (s[i] == s[j-1]):
                # Move o ponteiro direito (simula inserção à esquerda, pois esta opção é mais atrativa a curto prazo)
                contador += 1
                j -= 1
            else:
                # Caso ambíguo: escolhe arbitrariamente um lado, nesse caso escolhemos inserçãO a esquerda
                contador += 1
                j -= 1
                # ou i += 1 (ambas as escolhas são válidas, mas não ótimas)
    return contador


if __name__ == "__main__":
    s = "luis"
    print(f"Número de inserções: {minimal_palindrome_greedy(s)}")
