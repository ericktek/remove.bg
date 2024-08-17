# Requires "requests" to be installed 
import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = '4kYsg2RuqXs6SQaFfexn93sT'
IMAGE_PATH = 'images/kid.jpg'  

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(IMAGE_PATH, 'rb')},  
    data={'size': 'auto'},
    headers={'X-Api-Key': API_KEY},
)

if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
    print("Background removed successfully. Image saved as 'no-bg.png'.")
else:
    print("Error:", response.status_code, response.text)
