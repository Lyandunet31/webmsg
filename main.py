import requests
import random

# URL du webhook Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1301587125334179860/g_qempPMe0lFn3T48udMMZbAUaIWBjdLQCVYnGtmhl97kHAMREdwVEnDRxgrY6n4R0uI'

# Liste de messages aléatoires
messages = [
    "Hello, Discord!",
    "This is a random message.",
    "Hope you're having a great day!",
    "Sending this from Python.",
    "Randomness is fun!"
]

# Sélectionne un message au hasard
message = random.choice(messages)

# Corps de la requête
payload = {
    "content": message
}

# Envoie la requête POST au webhook Discord
response = requests.post(WEBHOOK_URL, json=payload)

# Vérifie si la requête a réussi
if response.status_code == 204:
    print("Message envoyé avec succès!")
else:
    print(f"Erreur lors de l'envoi du message : {response.status_code} - {response.text}")
