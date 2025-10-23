from model.auth_model import AuthModel

def test_auth_validate_admin():
    # usar banco em memória
    auth = AuthModel(":memory:")
    ok, user = auth.validate("admin", "admin")
    assert ok is True
    assert user["username"] == "admin"

def test_auth_invalid_empty():
    auth = AuthModel(":memory:")
    ok, user = auth.validate("", "")
    assert ok is False
    assert user == {}
