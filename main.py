import requests
from bs4 import BeautifulSoup

def extract_product_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        product_name_tag = soup.find('h1')
        product_name = product_name_tag.text.strip() if product_name_tag else "Nom du produit non trouvé"

        price_elements = soup.find_all('span', class_='woocommerce-Price-amount')
        if len(price_elements) >= 2:
            product_price = price_elements[1].find('bdi').text.strip()
        else:
            product_price = "Prix du produit non trouvé"
        return product_name, product_price
    except Exception as e:
        print("Une erreur s'est produite lors de l'extraction des informations du produit:", str(e))
        return None, None

product_url = "https://www.example.com/product/12345"

product_name, product_price = extract_product_info(product_url)

if product_name and product_price:
    print(f"Nom du produit : {product_name}")
    print(f"Prix du produit : {product_price}")
else:
    print("Impossible de récupérer les informations du produit.")
