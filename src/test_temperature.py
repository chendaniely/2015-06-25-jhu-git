import temperature

def test_f_to_k():
    assert temperature.f_to_k(32) == 273.15
    assert temperature.f_to_k(212) == 373.15
