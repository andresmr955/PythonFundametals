import unittest
import requests

BANCO_API_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series"
TOKEN = "e3980208bf01ec653aba9aee3c2d6f70f6ae8b066d2545e379b9e0ef92e9de25"
SERIE_USD_MXN = "SF43718"  # Tipo de cambio FIX USD/MXN

def is_api_available():
    headers = {"BMX-Token": TOKEN}  # Usamos el token en el header
    try:
        url = f"{BANCO_API_URL}/{SERIE_USD_MXN}/datos/oportuno"
        response = requests.get(url, headers=headers, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

class TestBanxicoAPI(unittest.TestCase):
    
    # Usamos el decorador skipUnless para verificar la disponibilidad de la API
    @unittest.skipUnless(is_api_available(), "La API de Banxico no está disponible")
    def test_api_is_running(self):
        headers = {"BMX-Token": TOKEN}  # Usamos el token en el header
        url = f"{BANCO_API_URL}/{SERIE_USD_MXN}/datos/oportuno"
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.headers["Content-Type"], [
            "application/json", "application/xml", "text/html"
        ])

if __name__ == "__main__":
    unittest.main()
