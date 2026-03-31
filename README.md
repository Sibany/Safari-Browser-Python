# Safari Browser Emulator for Sibany Developers

This application is a specialized **WebKit-based browser environment** built using Python and Playwright. It was created specifically for **Sibany developers** to handle iOS-specific display testing and error inspection on Windows machines.

## 🚀 Overview
Unlike standard desktop browsers, this tool uses the actual WebKit engine (the core of iOS Safari). It allows developers to:
* **Check iOS Version Displays:** Test how sites render on the Safari engine.
* **Inspect Errors:** Identify JavaScript and CSS bugs unique to Apple devices.
* **Continuous Testing:** No timeouts; the window stays open until you manually close it.

---

## 🛠️ Setup & Installation

To run this tool on your local machine, ensure you have **Python 3.11+** installed, then follow these steps:

### 1. Install Required Packages
Open your terminal or PowerShell and run:
```powershell
pip install playwright
2. Download the WebKit Engine
This command downloads the Safari (WebKit) binaries used by the script:

PowerShell
python -m playwright install webkit
💻 Usage
Running the Script
Execute the script from your project folder:

PowerShell
python safari_test.py
🔍 Using the Inspect Tool (For Debugging)
To catch errors and inspect elements (similar to Chrome DevTools), run the script with the Debug Flag enabled:

PowerShell
# On Windows PowerShell:
$env:PWDEBUG=1; python safari_test.py
This will open a second window (Playwright Inspector) allowing you to trace errors and audit the DOM.

📂 Script Details
The script (safari_test.py) is optimized with the following logic:

No Timeouts: page.set_default_navigation_timeout(0) ensures the page never times out while you are debugging.

Portable Logic: Includes sys._MEIPASS handling to support future conversion into a standalone .exe.

Clean UI: Launches a high-resolution window (1280x800) without unnecessary browser toolbars for a clean testing space.

📦 Building an EXE (Optional)
If you need to share this as a standalone executable for other Sibany team members:

PowerShell
python -m PyInstaller --noconsole --onefile --name "Safari_Browser" --collect-all playwright safari_test.py
Note: This is an internal tool developed for the Sibany engineering team.
