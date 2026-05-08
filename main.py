from playwright.sync_api import sync_playwright
import os, json

class Automacoes:
    
    def automacao7(self):
        os.makedirs("images", exist_ok=True)

        with open("utils/sites.json", "r", encoding="utf-8") as file:
            sites = json.load(file)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)

            pages = []

            for site in sites:
                page = context.new_page()
                page.goto(site["url"], wait_until="domcontentloaded", timeout=50000)
                page.wait_for_timeout(3000)
                pages.append((page, site["image"]))

            for page, image_name in pages:
                page.screenshot(path=f"images/{image_name}", full_page=True)

                print(f"Prints sites salvo em: images/{image_name}")

            browser.close()

if __name__ == '__main__':
    rpa7 = Automacoes
    rpa7.automacao7(rpa7)







