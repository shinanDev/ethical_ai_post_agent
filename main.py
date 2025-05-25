import os
import yaml
from pathlib import Path
from slugify import slugify

# Paths
POST_DIR = Path("posts")
POST_DIR.mkdir(exist_ok=True)
TOPIC_FILE = "data/topics.yaml"

def load_topics(filepath=TOPIC_FILE):
    try:
        with open(filepath, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"❌ YAML file not found: {filepath}")
        return []
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        return []

def build_post(topic):
    try:
        title = topic['title']
        description = topic['description']
        case_study = topic['case_study']
        link = topic['link']
        hashtags = " ".join(topic.get('hashtags', []))

        return f"""
# {title}

{description}

🔬 *Case Study:* {case_study}  
🔗 *Source:* [{link}]({link})

{hashtags}
""".strip()
    except KeyError as e:
        return f"❌ Missing required field: {e}"

def save_post_to_file(topic, content):
    slug = slugify(topic.get('title', 'untitled'))
    filename = f"{slug}.md"
    with open(POST_DIR / filename, "w") as f:
        f.write(content)
    print(f"✅ Saved post: {filename}")

def main():
    topics = load_topics()
    for topic in topics:
        print("\n" + "*" * 60)
        post = build_post(topic)
        print(post)
        print("\n🖼 IMAGE PROMPT:")
        print(topic.get("image_prompt", "(no prompt defined)"))
        print("*" * 60 + "\n")
        save_post_to_file(topic, post)

if __name__ == "__main__":
    main()