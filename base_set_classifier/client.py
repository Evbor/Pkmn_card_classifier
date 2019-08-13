import requests
import base64

API_ENDPOINT = 'http://127.0.0.1:5000/base_set_classifier/predict/'

image_path_1 = '/home/dev/Downloads/PK_S49_BW_61.jpg'

b64_image_1 = ''

with open(image_path, "rb") as imageFile:
    b64_image_1 = base64.b64encode(imageFile.read())

image_path_2 = '/home/dev/Downloads/tumblr_a91cc49f842f56f2a06370bb7a76a790_982be403_500.jpg'
b64_image_2 = ''

with open(image_path_2, "rb") as imageFile:
    b64_image_2 = base64.b64encode(imageFile.read())

data = {'samples': [{'image': b64_image_1, 'label': 'not_base_set', 'pkmn_card': True},
                    {'image': b64_image_2, 'label': 'not_base_set', 'pkmn_card': False}]}

r = requests.post(url=API_ENDPOINT, data=data)

print('{}'.format(r.text))
