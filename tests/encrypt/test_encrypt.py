import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("hello", 2) == "oll_eh"
    assert encrypt_message("world", 3) == "row_dl"
    assert encrypt_message("python", 4) == "no_htyp"
    assert encrypt_message("hello", 6) == "olleh"
    with pytest.raises(TypeError):
        encrypt_message("hello", "2")
    with pytest.raises(TypeError):
        encrypt_message(123, 2)
