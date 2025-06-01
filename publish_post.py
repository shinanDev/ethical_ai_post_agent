import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
ORGANIZATION_URN = os.getenv("LINKEDIN_ORGANIZATION_URN")  # Beispiel: urn:li:organization:12345678

# Lese den generierten Beitrag (z. B. aus Markdown-Datei)
def load_post_text(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[X] Datei nicht gefunden: {filepath}")
        return ""

# Sende Post an LinkedIn
def publish_to_linkedin(post_text):
    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    payload = {
        "author": ORGANIZATION_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post_text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("[OK] Beitrag erfolgreich auf LinkedIn gepostet.")
    else:
        print(f"[X] Fehler beim Posten: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    post_path = "posts/next_post.md"  # Oder automatisch den neuesten generierten Beitrag wählen
    post_content = load_post_text(post_path)
    if post_content:
        publish_to_linkedin(post_content)