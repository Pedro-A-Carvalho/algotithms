def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    first = 0
    last = len(word) - 1
    while first < last:
        if word[first] != word[last]:
            return False
        first += 1
        last -= 1
    return True
