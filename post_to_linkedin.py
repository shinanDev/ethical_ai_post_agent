import os
import requests
from dotenv import load_dotenv

# .env laden
load_dotenv()
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
ORGANIZATION_URN = "urn:li:organization:91687641"

# Test-Nachricht
post_data = {
    "author": ORGANIZATION_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello LinkedIn! This is a test post from the Ethical AI Agent 🧪"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.linkedin.com/v2/ugcPosts",
    headers=headers,
    json=post_data
)

print(f"Status Code: {response.status_code}")
print("Response:")
print(response.json())