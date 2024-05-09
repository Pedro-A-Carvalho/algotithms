def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == "":
        return False
    if len(word) - 1 == high_index:
        return word == is_palindrome_recursive(word, high_index, low_index)
    return word[::-1]
