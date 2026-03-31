import os
import sys
from playwright.sync_api import sync_playwright

def run_safari():
    # 1. This part tells the EXE where to find the bundled browser engine
    if getattr(sys, 'frozen', False):
        # We are running inside the PyInstaller EXE
        bundle_dir = sys._MEIPASS
        browser_path = os.path.join(bundle_dir, "playwright", "driver", "package", ".local-browsers")
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = browser_path

    with sync_playwright() as p:
        # 2. Launch WebKit (The Safari Engine)
        # We use 'headless=False' so the window actually pops up
        browser = p.webkit.launch(headless=False)
        
        # 3. Create a clean window context
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()
        
        try:
            # 4. Remove all timeouts for navigation
            page.set_default_navigation_timeout(0)
            
            # 5. Navigate to your site
            page.goto("https://www.sibany.com")
            
            # 6. Keep the app alive until the user closes the window
            page.wait_for_event("close", timeout=0)
            
        except Exception:
            # Handle manual closure gracefully
            pass
        finally:
            browser.close()

if __name__ == "__main__":
    run_safari()
