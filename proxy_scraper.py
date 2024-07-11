import requests
import re

def fetch_proxies_from_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching proxies from {url}: {e}")
        return ""

def extract_proxies_from_html(html):
    proxy_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}:\d+')
    return proxy_pattern.findall(html)

def sort_proxies(proxies):
    return sorted(proxies)

def save_proxies(proxies, filename="sorted_proxies.txt"):
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")

def main():
    urls = [
        "https://www.sslproxies.org/",
        "https://free-proxy-list.net/",
        "https://www.us-proxy.org/",
        "https://free-proxy-list.net/uk-proxy.html",
        "http://free-proxy.cz/en/proxylist/country/US/https/ping/all",
        "https://www.proxynova.com/proxy-server-list/",
        "http://spys.one/en/https-ssl-proxy/"
    ]

    all_proxies = []

    for url in urls:
        html = fetch_proxies_from_html(url)
        proxies = extract_proxies_from_html(html)
        all_proxies.extend(proxies)

    sorted_proxies = sort_proxies(all_proxies)
    save_proxies(sorted_proxies)
    return sorted_proxies

if __name__ == "__main__":
    main()
