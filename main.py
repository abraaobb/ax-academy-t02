from playwright.sync_api import sync_playwright
import os

class Automacoes:
    
    def automacao7(self):
        os.makedirs("images", exist_ok=True)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)

            sites = [
                ("https://oglobo.globo.com/epoca/", "oglobo.png"),
                ("https://www.espn.com.br/", "espn.png"),
                ("https://www.acritica.com/", "acritica.png"),
                ("https://www.cbc.ca/news", "cbc.png"),
                ("https://www.linuxjournal.com/", "linux-journal.png")
            ]

            pages = []

            for url, image_name in sites:
                page = context.new_page()
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(4000)
                pages.append((page, image_name))

            for page, image_name in pages:
                page.screenshot(path=f"images/{image_name}", full_page=True)
                print(f"Captura da tela salvo em: images/{image_name}")

            browser.close()

if __name__ == '__main__':
    rpa7 = Automacoes
    rpa7.automacao7(rpa7)







