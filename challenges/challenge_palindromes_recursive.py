def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if not word:
        return False
    cond = word[low_index] == word[high_index]
    if low_index >= high_index:
        return True
    if cond:
        return True and is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )
    return False
