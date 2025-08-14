import os
import requests
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
ORGANIZATION_URN = os.getenv("LINKEDIN_ORGANIZATION_URN")

# Lese den generierten Beitrag aus der Markdown-Datei
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
    # post_path = "posts/next_post.md"
    # post_content = load_post_text(post_path)
    # if post_content:
    #     publish_to_linkedin(post_content)

    def scheduled_job():
        post_path = "posts/next_post.md"
        post_content = load_post_text(post_path)
        if post_content:
            publish_to_linkedin(post_content)

    # Plane wöchentliche Veröffentlichung: jeden Mittwoch um 13:00 Uhr
    schedule.every().wednesday.at("13:00").do(scheduled_job)

    print("[INFO] Scheduler aktiviert. Warte auf nächsten Termin...")

    while True:
        schedule.run_pending()
        time.sleep(60)