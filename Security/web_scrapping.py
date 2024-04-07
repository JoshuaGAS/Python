import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re

def get_valid_url():
    while True:
        url = input("Enter the URL of the website you want to scrape: ").strip()
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return url
        else:
            print("Invalid URL. Please enter a valid URL.")

def detect_js_and_py_files(url):
    try:
        # Send a GET request to the webpage
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <script> tags
        script_tags = soup.find_all('script')

        # Find all <link> tags with href ending in '.js'
        js_links = soup.find_all('link', href=lambda href: href and href.endswith('.js'))

        # Find all <a> tags with href ending in '.py'
        py_links = soup.find_all('a', href=lambda href: href and href.endswith('.py'))

        # Print JavaScript scripts and links to JavaScript files
        if script_tags or js_links:
            print("JavaScript scripts and links to JavaScript files detected on the page:")
            for script_tag in script_tags:
                print(script_tag)
            for link in js_links:
                js_url = urljoin(url, link['href'])
                print(js_url)
        else:
            print("No JavaScript scripts or links to JavaScript files found on the page.")

        # Print links to Python files
        if py_links:
            print("\nLinks to Python files found on the page:")
            for link in py_links:
                py_url = urljoin(url, link['href'])
                print(py_url)
        else:
            print("\nNo links to Python files found on the page.")

        # Check for threats
        page_content = response.text
        if re.search(r'phish|malware|spyware|virus', page_content, re.IGNORECASE):
            print("\nWarning: Suspicious keywords found in page content.")

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    url = get_valid_url()
    detect_js_and_py_files(url)
