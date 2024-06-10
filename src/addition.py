# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(4, 5) == 9
    assert add(3, 4) == 7
# github actions test
