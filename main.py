import os
import yaml
import logging
from pathlib import Path
from slugify import slugify
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        with open(filepath, "r", encoding="utf-8") as file:
            return list(yaml.safe_load_all(file))
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

        return f"""{title}

{description}

Case Study: {case_study}
Source: [{link}]({link})

{hashtags}""".strip()
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
    topics = load_topics()  # <- lädt Liste via safe_load_all()
    prompt_template = load_prompt()

    if not topics:
        print("[X] No topics found.")
        return

    # 👉 Nur ein Topic pro Lauf – z. B. das erste
    topic = topics[0]
    if isinstance(topic, list):
        topic = topic[0]

    post = build_post(topic)
    print(post)

    print("\nIMAGE PROMPT:", topic.get("image_prompt", "(no prompt defined)"))

    filled_prompt = prompt_template.format(**topic)
    if topic.get("case_study") and topic.get("link"):
        filled_prompt += f"\n\nCase Study: {topic['case_study']}\nSource: {topic['link']}"
    print("\nGENERATED PROMPT:\n")
    print(filled_prompt)

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in ethical AI communication."},
                {"role": "user", "content": filled_prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        generated_post = response.choices[0].message.content.strip()
        print("\n✅ FINAL LINKEDIN POST:\n")
        print(generated_post)

        hashtags = " ".join(topic.get("hashtags", []))
        full_post_with_link = f"{generated_post}\n\nSource: {topic.get('link', '(no link provided)')}\n\n{hashtags}"
        save_post_to_file(topic, full_post_with_link)

    except Exception as e:
        print(f"[X] GPT API error: {e}")

if __name__ == "__main__":
    main()
