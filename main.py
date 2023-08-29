import requests
from bs4 import BeautifulSoup

# Fonction pour extraire les informations du produit à partir de l'URL
def extract_product_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        product_name = soup.find('h1', class_='product-title').text.strip()
        product_price = soup.find('span', class_='product-price').text.strip()
        return product_name, product_price
    except Exception as e:
        print("Une erreur s'est produite lors de l'extraction des informations du produit:", str(e))
        return None, None

product_url = "https://www.example.com/product"

product_name, product_price = extract_product_info(product_url)

if product_name and product_price:
    print(f"Nom du produit : {product_name}")
    print(f"Prix du produit : {product_price}")
else:
    print("Impossible de récupérer les informations du produit.")
