import os
import yaml
import logging
from pathlib import Path
from slugify import slugify

# Logging configuration
logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Paths
POST_DIR = Path("posts")
POST_DIR.mkdir(exist_ok=True)
TOPIC_FILE = "data/topics.yaml"
PROMPT_FILE = "prompts/post_prompt.txt"

# Load YAML topics
def load_topics(filepath=TOPIC_FILE):
    try:
        with open(filepath, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"[X] YAML file not found: {filepath}")
        return []
    except yaml.YAMLError as e:
        print(f"[X] YAML parsing error: {e}")
        return []

# Load prompt from external file
def load_prompt(filepath=PROMPT_FILE):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"[X] Prompt file not found: {filepath}")
        return ""

# Build post markdown string
def build_post(topic):
    try:
        title = topic['title']
        description = topic['description']
        case_study = topic['case_study']
        link = topic['link']
        hashtags = " ".join(topic.get('hashtags', []))

        return f"""
{title}

{description}

Case Study: {case_study}
Source: [{link}]({link})

{hashtags}
""".strip()
    except KeyError as e:
        return f"[X] Missing required field: {e}"

# Save post as markdown file
def save_post_to_file(topic, content):
    slug = slugify(topic.get('title', 'untitled'))
    filename = f"{slug}.md"
    with open(POST_DIR / filename, "w") as f:
        f.write(content)
    print(f"[✓] Saved post: {filename}")

# Main execution
def main():
    topics = load_topics()
    prompt_template = load_prompt()

    for topic in topics:
        print("\n" + "=" * 60)
        post = build_post(topic)
        print(post)
        print("\nIMAGE PROMPT:", topic.get('image_prompt', '(no prompt defined)'))
        print("=" * 60 + "\n")

        # Generate full prompt and print it
        filled_prompt = prompt_template.format(topic=topic)
        print("\nGENERATED PROMPT:\n")
        print(filled_prompt)

        save_post_to_file(topic, post)

if __name__ == "__main__":
    main()