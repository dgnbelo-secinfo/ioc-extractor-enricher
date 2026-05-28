import re

with open("sample_iocs.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\n=== IOC EXTRACTOR & ENRICHER ===\n")

# IPs
ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)

# URLs
urls = re.findall(r'https?://[^\s]+', content)

# Domains
domains = re.findall(r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', content)

# MD5
md5_hashes = re.findall(r'\b[a-fA-F0-9]{32}\b', content)

# SHA256
sha256_hashes = re.findall(r'\b[a-fA-F0-9]{64}\b', content)

# Resultados
if ips:
    print("[+] IPs encontrados:")
    for ip in ips:
        print(f" - {ip}")

if urls:
    print("\n[+] URLs encontradas:")
    for url in urls:
        print(f" - {url}")

if domains:
    print("\n[+] Domínios encontrados:")
    for domain in domains:
        print(f" - {domain}")

if md5_hashes:
    print("\n[+] MD5 encontrados:")
    for md5 in md5_hashes:
        print(f" - {md5}")

if sha256_hashes:
    print("\n[+] SHA256 encontrados:")
    for sha in sha256_hashes:
        print(f" - {sha}")

print("\n=== Análise concluída ===")