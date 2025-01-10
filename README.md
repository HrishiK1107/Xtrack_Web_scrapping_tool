# Xtract - Powerful Web Scraping Tool 🕵️‍♂️

**Xtract** is a powerful and easy-to-use web scraping tool designed to extract all links from a given webpage. It provides flexibility by allowing users to choose between two modes for fetching web data: using simple `requests` or leveraging **Selenium** for rendering JavaScript-heavy websites.

## Features
- **Extract Links**: Extracts all links (URLs) from a webpage.
- **JavaScript Rendering**: Handles JavaScript rendering with Selenium for dynamic pages.
- **User-Friendly CLI**: Engaging and simple command-line interface guiding users through the scraping process.
- **Supports Multiple Modes**: Choose between `requests` or `Selenium` depending on the webpage's complexity.
- **Colorful Output**: Outputs results in a colorful and readable format using ASCII art.

## Requirements

To run **Xtract**, you need to have the following Python packages installed:

- `requests`: For fetching static webpages.
- `beautifulsoup4`: For parsing HTML content.
- `selenium`: For scraping JavaScript-heavy pages.
- `webdriver-manager`: For managing browser drivers.
- `pyfiglet`: For generating ASCII art banners.
- `termcolor`: For adding color to the terminal output.

## Installation

Follow these steps to set up **Xtract** on your machine:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/xtract.git
cd xtract
```

### 2. Install Dependencies
Use the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Tool
Once the setup is complete, run the tool with the following command:

```bash
python xtract.py
```

### 2. Enter the URL to Scrape
When prompted, enter the URL of the website you want to scrape.


### 3. Choose JavaScript Rendering
Next, you'll be asked if the website requires JavaScript rendering. Answer y for Yes and n for No.

``
Does the website require JavaScript rendering? (y/n): n
``

### 4. View the Extracted Links
The tool will output the list of all links on the page, showing the link titles and URLs.

![image](https://github.com/user-attachments/assets/55bf6604-a16b-4a4c-b028-2078afd7227f)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
XTract tool is intended for educational and ethical hacking purposes only. This tool should only be used on passwords or systems that you own or have explicit permission to test. Unauthorized use against any system is illegal and may lead to severe consequences, including legal action.

By using this tool, you acknowledge that you are solely responsible for any consequences arising from its use. The author and contributors of this project are not liable for any damages, losses, or legal issues resulting from the misuse of this tool.
