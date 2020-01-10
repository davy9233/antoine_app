# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:39:21 2020

@author: utilisateur
"""



# exo 1
"""
Lister les 10 derniers livres par leur date de publication
"""

import requests
r = requests.get('https://demo.api-platform.com/books?order[publicationDate]=desc&page=1')
data1=(r.json())
s=0 
print('Lister les 10 derniers livres par leur date de publication')
while s< 11:
    print(data1["hydra:member"][s]['title'])
    s+=1
    

# ex0 2
"""
Lister le livre écrit par l’auteur « Dr. Kaitlyn Ratke »
"""    
    
import requests
r2 = requests.get('https://demo.api-platform.com/books?author=Dr.%20Kaitlyn%20Ratke&page=1')
data2=(r2.json())
print("\n") 
print("livre écrit par l’auteur « Dr. Kaitlyn Ratke »")
for i in range(len(data2["hydra:member"])):
   
    print(data2["hydra:member"][i]['title'])

   
# exo3
"""
Lister tous les commentaires du livre dont l’id est « 1d52ba85-97c8-4cc3-b81a-
40582f3aff64 »
"""    
    
import requests   
r3 = requests.get('https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a-40582f3aff64')
data3=(r3.json())
print("\n")
print("les commentaires du livre dont l’id est « 1d52ba85-97c8-4cc3-b81a-40582f3aff64")
for el in data3['reviews']:
    print(el["body"])

    


#exo 4
"""
Créer un nouveau commentaire avec le texte et la note de votre choix pour le livre
dont l’id est « 1b08c9ab-6254-4015-ad14-bac3e5c008df »
"""
import requests
data4={
  "body": "test_dca_2",
  "rating": 5,
  "author": "dca_2",
  "publicationDate": "2020-01-10T09:00:40.196Z",
  "book": "/books/1b08c9ab-6254-4015-ad14-bac3e5c008df"
}
r = requests.post('https://demo.api-platform.com/reviews', json=data4)



#exo 5


"""
Modifier votre nouveau commentaire en utilisant l’id qui vous a été fourni lors de sa
création
"""

import requests

url = "https://demo.api-platform.com/reviews/00421975-a3c2-44ab-88af-99ceda201e91"

payload = "{\n\t\"body\" : \"trop dur\"\n}"
headers = {
    'cookie': "__cfduid=dd0757c4290287936d03f1028b00579661578569236",
    'content-type': "application/merge-patch+json"
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
