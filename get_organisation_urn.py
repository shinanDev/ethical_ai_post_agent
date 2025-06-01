import requests
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {access_token}",
    "X-Restli-Protocol-Version": "2.0.0"
}

url = "https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&role=ADMINISTRATOR&state=APPROVED"

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())