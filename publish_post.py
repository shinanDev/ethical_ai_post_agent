import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Validate environment variables
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
ORGANIZATION_URN = os.getenv("LINKEDIN_ORGANIZATION_URN")

if not LINKEDIN_ACCESS_TOKEN:
    raise ValueError("LINKEDIN_ACCESS_TOKEN not found in .env file. Please add your LinkedIn access token.")
if not ORGANIZATION_URN:
    raise ValueError("LINKEDIN_ORGANIZATION_URN not found in .env file. Please add your organization URN.")

# Get the most recent post file from the posts directory
def get_latest_post_file():
    posts_dir = Path("posts")
    if not posts_dir.exists():
        raise FileNotFoundError("Posts directory does not exist.")

    # Get all .md files sorted by modification time (most recent first)
    post_files = sorted(posts_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)

    if not post_files:
        raise FileNotFoundError("No post files found in posts directory.")

    return post_files[0]

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
    # Execute once - this script is called by scheduler.py
    try:
        post_path = get_latest_post_file()
        print(f"[INFO] Publishing post from: {post_path}")
        post_content = load_post_text(post_path)
        if post_content:
            publish_to_linkedin(post_content)
    except Exception as e:
        print(f"[X] Error publishing post: {e}")