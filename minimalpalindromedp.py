def minRecur(s, l, h, memo):
    # Função recursiva com memoização para calcular o mínimo de inserções necessárias.

    # Caso base: quando os índices se cruzam ou passam um do outro
    if l >= h:
        return 0

    # Se já calculamos esse subproblema antes, retornamos o resultado armazenado
    if memo[l][h] != -1:
        return memo[l][h]

    # Se os caracteres nos extremos forem iguais, não precisamos inserir nada
    # e verificamos a substring interna
    if s[l] == s[h]:
        memo[l][h] = minRecur(s, l + 1, h - 1, memo)
        return memo[l][h]

    # Se os caracteres forem diferentes, consideramos ambas as opções:
    # 1. Inserir um caractere igual ao final no início
    # 2. Inserir um caractere igual ao início no final
    # E pegamos o mínimo dessas opções + 1 (pela inserção)
    memo[l][h] = min(minRecur(s, l + 1, h, memo),
                     minRecur(s, l, h - 1, memo)) + 1
    return memo[l][h]


def encontrarMinInsert(s):
    # Função principal que inicia o cálculo das inserções mínimas.

    n = len(s)
    # Inicializa a tabela de memoização com -1 (indicando não calculado)
    memo = [[-1] * n for _ in range(n)]
    return minRecur(s, 0, n - 1, memo)


if __name__ == "__main__":
    s = "abcdddd"
    print(f"Número mínimo de inserções: {encontrarMinInsert(s)}")
