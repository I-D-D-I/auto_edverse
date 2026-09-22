from playwright.sync_api import Page  # Тип Page для аннотации

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def open(self, url: str):
        """Открыть страницу по URL."""
        self.page.goto(url)
        return self
    
    def take_screenshot(self, name: str):
        """Сохранить скриншот в папку screenshots."""
        self.page.screenshot(path=f"screenshots/{name}.png")
        return self
    
    