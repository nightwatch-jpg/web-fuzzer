import requests

paths = ["admin", "login", "backup.zip", "config", "robots.txt"]

def fuzz_site(url):
    print(f"Начинаю поиск: {url}...")
    url = url.rstrip("/")
    for path in paths:
        full_url = f"{url}/{path}"
        print(f"Проверяю: {full_url}...")
        
        try:
            response = requests.get(full_url, timeout=3)
            
            # ВОТ ЗДЕСЬ ДОЛЖНА БЫТЬ ПРОВЕРКА (с отступом внутри for)
            if response.status_code == 200:
                print(f"🟢 НАЙДЕНО: {full_url}")  # Выводим full_url, а не url
            elif response.status_code == 403:
                print(f"🟡 ЗАЩИЩЕНО: {full_url}")
                
        except:
            pass

fuzz_site("https://github.com")