import os
import yaml
from pathlib import Path

# Verzeichnisse
POST_DIR = Path("posts")
POST_DIR.mkdir(exist_ok=True)

def load_topics(filepath="data/topics.yaml"):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)

def build_post(topic):
    return f"""
🔍 {topic['title']}

{topic['description']}

📚 Case Study: {topic['case_study']}
🔗 More: {topic['link']}

#{" #".join(topic['hashtags'])}
""".strip()

def save_post_to_file(topic, content):
    filename = f"{topic['title'].replace(' ', '_').lower()}.md"
    with open(POST_DIR / filename, "w") as f:
        f.write(content)
        print(f"✅ Saved post: {filename}")

def main():
    topics = load_topics()
    for topic in topics:
        post = build_post(topic)
        print("\n" + "="*60)
        print(post)
        print("\nIMAGE PROMPT:")
        print(topic.get("image_prompt", "(no prompt defined)"))
        print("="*60 + "\n")
        save_post_to_file(topic, post)

if __name__ == "__main__":
    main()