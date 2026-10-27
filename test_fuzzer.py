from fuzzer import fuzz_site

def test_fuzz_site_bad_url():
    try:
        fuzz_site("https://this-site-does-not-exist-12345.com")
        assert True
    except Exception as e:
        assert False, f"Функция fuzz_site упала с ошибкой: {e}"

def test_fuzz_site_good_url():
    try:
        fuzz_site("https://example.com")
        assert True
    except Exception as e:
        assert False, f"Функция fuzz_site упала с ошибкой: {e}"