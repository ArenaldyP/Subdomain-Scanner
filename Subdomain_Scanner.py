import requests
from concurrent.futures import ThreadPoolExecutor

# Domain yang akan dipindai untuk subdomain
domain = input("Masukkan Domain: ")

# Membaca semua subdomain dari file
with open("subdomain.txt") as file:
    # Membaca seluruh konten
    content = file.read()
    # Memisahkan berdasarkan baris baru
    subdomains = content.splitlines()

# Daftar subdomain yang ditemukan
discovered_subdomains = []

# Menetapkan header User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def check_subdomain(subdomain):
    url = f"https://{subdomain}.{domain}"
    try:
        # Menggunakan metode GET untuk memeriksa ketersediaan subdomain
        requests.get(url, headers=headers, timeout=1)
    except requests.ConnectionError:
        # Mengabaikan jika terjadi kesalahan koneksi
        pass
    else:
        print(f"[+] Subdomain Ditemukan: {url}")
        discovered_subdomains.append(url)

# Menggunakan ThreadPoolExecutor untuk multi-threading
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_subdomain, subdomains)

# Menyimpan daftar subdomain yang ditemukan ke dalam file
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
