import pyfiglet
from termcolor import colored
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Display the banner when the tool starts
def display_banner():
    # Create an ASCII banner for the name "Xtract"
    ascii_banner = pyfiglet.figlet_format("Xtract")
    # Add color to the banner
    colored_banner = colored(ascii_banner, 'red')
    print(colored_banner)

# Function to fetch and parse the page
def fetch_and_parse(url, use_selenium=False):
    if use_selenium:
        # Setup Selenium WebDriver with Chrome
        options = Options()
        options.headless = True  # Run in headless mode
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
    else:
        # Use requests and BeautifulSoup for simple pages
        response = requests.get(url)
        page_source = response.text

    # Parse the page using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

# Function to extract and print all links from the page
def extract_links(soup):
    links = soup.find_all('a')
    print(f"Found {len(links)} <a> tags.")
    
    for index, link in enumerate(links, start=1):
        href = link.get('href')

        if href and (href.startswith('http://') or href.startswith('https://')):
            title = link.text.strip()
            if title:
                print(f"{index}. {title} - {href}")
            else:
                print(f"{index}. No title found - {href}")

def main():
    # Display the Xtract banner when the tool starts
    display_banner()

    # Get the URL to scrape from the user
    url = input("Enter the URL to scrape: ")

    # Ask if the website requires JavaScript rendering
    js_rendering = input("Does the website require JavaScript rendering? (y/n): ").lower()

    use_selenium = js_rendering == 'y'

    # Fetch the page content using the appropriate method (requests or Selenium)
    print(f"Fetching data from: {url}")
    soup = fetch_and_parse(url, use_selenium)

    # Extract and display all links from the page
    extract_links(soup)

if __name__ == "__main__":
    main()
