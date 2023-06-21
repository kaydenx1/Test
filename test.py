import requests

import img2pdf

from bs4 import BeautifulSoup

from PIL import Image

from io import BytesIO

# Define the URL of the website

url = 'https://nhentai.website/g/149671'

# Send a GET request to the URL

response = requests.get(url)

# Parse the HTML content using BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')

# Find all the img elements with the "data-src" attribute

img_elements = soup.find_all('img', {'data-src': True})

# Create a list to store the downloaded images as PIL Image objects

images = []

# Download and store each image

for img in img_elements:

    # Get the image URL from the "data-src" attribute

    img_url = img['data-src']

    

    # Send a GET request to the image URL

    img_response = requests.get(img_url)

    

    # Open the image using PIL

    img_data = BytesIO(img_response.content)

    image = Image.open(img_data)

    

    # Append the image to the list

    images.append(image)

# Create a PDF file and save the images in it

with open('images.pdf', 'wb') as f:

    f.write(img2pdf.convert(images))

print('Images downloaded and saved as "images.pdf"')
