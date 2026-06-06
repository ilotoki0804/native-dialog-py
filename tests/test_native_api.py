from native_dialog import confirm


def test_confirm():
    assert confirm("title", "body", "info")
