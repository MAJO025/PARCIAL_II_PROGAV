from Parcial_II import Country
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import HTTPError, ConnectionError, Timeout

BASE = "https://restcountries.com/v3.1"

class CountryAPI:
    def by_name(self, name: str):
        url = f"{BASE}/name/{name}"
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            return Country(r.json()[0])
        except Timeout:
            print(f"Tardó demasiado: {name}")
        except ConnectionError:
            print("Sin conexión")
        except HTTPError as e:
            print(f" {name} no encontrado ({e.response.status_code})")
        return None

    def by_names_concurrente(self, nombres: list) -> list:
        resultados = []

        inicio = time.time()

        with ThreadPoolExecutor(max_workers=5) as pool:
            futuros = {pool.submit(self.by_name, n): n for n in nombres}
            for f in as_completed(futuros):
                pais = f.result()
                if pais:
                    resultados.append(pais)

        fin = time.time()
        print(f"Tiempo con concurrencia: {fin - inicio:.2f}s\n")

        return resultados