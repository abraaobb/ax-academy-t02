from playwright.sync_api import Playwright, sync_playwright, expect
import os, json
import time
import os
from dotenv import load_dotenv
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
    def ax_academy_10():
        # TAREFAS:
        #   - abrir navegador
        #   - abrir gmail, calendario, github e microsoft teams
        #   - fazer login em cada uma delas
        #   - deixar aberto por mais 40 segundos
        # VARIÁVEIS:
        #   - page1 = gmail
        #   - page2 = calendario
        #   - page3 = github
        #   - page4 = microsoft teams
        load_dotenv()
        email = os.getenv("email")
        senha = os.getenv("senha")
        senha2 = os.getenv("senha2")
        def run(playwright: Playwright) -> None:
            
            browser = playwright.chromium.launch(
                headless=False,
                channel="chrome", 
                args=["--disable-blink-features=AutomationControlled"], 
                ignore_default_args=["--enable-automation"]
            )
            context = browser.new_context()

            page1 = context.new_page()
            page1.goto("https://workspace.google.com/intl/pt-BR/gmail/")
            with page1.expect_popup() as page1_info:
                page1.get_by_role("link", name="Fazer login no Gmail").filter(visible=True).click()
            page1.close()
            page1 = page1_info.value
            page1.get_by_role("textbox", name="E-mail ou telefone").fill(email)
            page1.get_by_role("button", name="Avançar").filter(visible=True).click()
            page1.get_by_role("textbox", name="Digite sua senha").fill(senha)
            page1.get_by_role("button", name="Avançar").filter(visible=True).click()
            
            page2 = context.new_page()
            page2.goto("https://workspace.google.com/intl/pt-BR/products/calendar/")
            page2.get_by_text("Fazer login").filter(visible=True).first.click()
            page2.close()
            
            page3 = context.new_page()
            page3.goto("https://github.com/?locale=pt-br")
            page3.locator("a[href='/login']").filter(visible=True).click()
            page3.locator("input[id='login_field']").fill(email)
            page3.locator("input[id='password']").fill(senha2)
            page3.locator("input[value='Sign in']").filter(visible=True).click()

            page4 = context.new_page()
            page4.goto("https://teams.live.com/free/")
            page4.locator("button[data-onclick='signIn']").filter(visible=True).click()
            page4.locator("input[id='usernameEntry']").fill(email)
            page4.get_by_text("Avançar").filter(visible=True).click()
            page4.get_by_text("Use sua senha").filter(visible=True).click()
            page4.locator("input[id='passwordEntry']").fill(senha2)
            page4.get_by_text("Avançar").filter(visible=True).click()
            
            time.sleep(60)
            
        with sync_playwright() as playwright:
            run(playwright)
 

if __name__ == '__main__':
    rpa7 = Automacoes
    rpa7.automacao7(rpa7)
    rpa7.ax_academy_10()







