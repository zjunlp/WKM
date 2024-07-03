import requests

def Chat_Model(messages,system="",url="http://localhost:8080/v1/chat/completions",model="gpt-3.5-turbo",temperature=0.5,top_p=0,n=1,max_tokens=128):
    response = requests.post(
        url=url,
        json={
            "model": model,
            "messages": messages,
            "system": system,
            "tools": [],
            "do_sample": True,
            "temperature": temperature,
            "top_p": top_p,
            "n": n,
            "max_tokens": max_tokens,
            "stream": False
        }
    )
    return response.json()["choices"]
# response = requests.post(
#     url="http://localhost:8080/v1/chat/completions",
#     json={
#         "model": "gpt-3.5-turbo",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "Please provide a comprehensive list of gastronomical establishments worldwide that have consistently been recognized by reputable culinary experts and publications for their exemplary execution of traditional French cuisine, including but not limited to classic dishes such as bouillabaisse, coq au vin, and escargots. Additionally, please include any relevant information pertaining to the establishment's atmosphere, history, and notable chefs. The list should be organized by geographical location and must include at least 15 distinct establishments."
#             },
#             {
#                 "role": "assistant",
#                 "content": "Certainly! Here is a list of 15 renowned French restaurants worldwide that have been recognized by culinary experts and publications for their exemplary execution of traditional French cuisine:\n1. Le Bernardin - New York City, USA\n2. L'Ambroisie - Paris, France\n3. Arpège - Paris, France\n4. Alain Ducasse au Plaza Athénée - Paris, France\n5. Osteria Francescana - Modena, Italy\n6. Mirazur - Menton, France\n7. Le Jules Verne - Paris, France\n8. Le Grand Véfour - Paris, France\n9. Le Comptoir du Relais - Paris, France\n10. L'Auberge du Pont de Collonges - Lyon, France\n11. La Grenouillère - La Madelaine-sous-Montreuil, France\n12. Les Prés d'Eugénie - Eugénie-les-Bains, France\n13. Guy Savoy - Paris, France\n14. Le Bristol Paris - Paris, France\n15. Le Meurice - Paris, France\nLe Bernardin, located in New York City, has been awarded three Michelin stars and is known for its seafood dishes. L'Ambroisie in Paris is a classic French restaurant that has been around since the 18th century and has been awarded three Michelin stars. Arpège, also in Paris, is known for its vegetarian dishes and has been awarded three Michelin stars. Alain Ducasse au Plaza Athénée, also in Paris, has been awarded three Michelin stars and is known for its contemporary French cuisine.\nOsteria Francescana in Modena, Italy, has been awarded three Michelin stars and is known for its modern take on traditional Italian cuisine. Mirazur in Menton, France, has been awarded three Michelin stars and is known for its Mediterranean-inspired dishes.\nLe Jules Verne in Paris is located in the Eiffel Tower and offers stunning views of the city. Le Grand Véfour in Paris is a historic restaurant that has been around since the 18th century and has been awarded three Michelin stars. Le Comptoir du Relais in Paris is a casual bistro that is known for its traditional French cuisine.\nL'Auberge du Pont de Collonges in Lyon, France, is a classic French restaurant that has been around since 1965 and has been awarded three Michelin stars. La Grenouillère in La Madelaine-sous-Montreuil, France, is known for its innovative take on traditional French cuisine. Les Prés d'Eugénie in Eugénie-les-Bains, France, is a luxury hotel and restaurant that has been awarded three Michelin stars.\nGuy Savoy in Paris has been awarded three Michelin stars and is known for its contemporary French cuisine. Le Bristol Paris in Paris is a luxury hotel that is home to the three Michelin-starred restaurant Epicure. Le Meurice in Paris is another luxury hotel that is home to the three Michelin-starred restaurant Le Meurice Alain Ducasse."
#             },
#             {
#                 "role": "user",
#                 "content": "What are the key differences between French cuisine and Italian cuisine?"
#             }
#         ],
#         "system": "",
#         "tools": [],
#         "do_sample": True,
#         "temperature": 0,
#         "top_p": 0,
#         "n": 1,
#         "max_tokens": 1024,
#         "stream": False
#     }
# )

# print(response.json()["choices"][0]["message"]["content"])

