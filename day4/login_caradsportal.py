# python -m pip install playwright
# python -m playwright install

from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()  # ładuje .env z bieżącego katalogu lub katalogów nadrzędnych


LOGIN_URL = "https://caradsportal.pl/login"
OFFERS_URL = "https://caradsportal.pl/offers"


USERNAME = os.getenv("CARADS_USER")
PASSWORD = os.getenv("CARADS_PASS")


if not USERNAME or not PASSWORD:
    raise ValueError("Ustaw zmienne środowiskowe CARADS_USER i CARADS_PASS")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(LOGIN_URL)

    # Na podstawie Twojego HTML:
    page.locator("#user_name").fill(USERNAME)
    page.locator("#user_pass").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    page.wait_for_load_state("networkidle")

    # zapis sesji do ponownego użycia
    context.storage_state(path="carads_state.json")

    print("Zalogowano i zapisano sesję.")

    print("Zalogowano. Przeglądarka zostaje otwarta.")

    input("Naciśnij Enter, aby przejsc do offers..")
    page.goto(OFFERS_URL)

    input("Naciśnij Enter, aby zamknąć przeglądarkę...")
    browser.close()
