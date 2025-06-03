# ethical_ai_post_agent

The **Ethical AI Post Agent** is an automated content generation tool designed to post professional, well-crafted updates on topics such as AI Ethics, Bias, Diversity, Fairness, and Responsible AI.

It was built to reduce repetitive content creation for LinkedIn while maintaining high-quality standards and raising awareness on key issues in artificial intelligence.

---

## Key Features

- Generates posts from curated `topics.yaml` entries
- Uses a modular prompt system (`prompt.txt`)
- Supports fully automated scheduling via cron jobs
- Seamlessly integrates with OpenAI API
- Posts are:
  - Under 250 words
  - Written in a clear, professional tone
  - Focused on awareness and constructive discourse
  - Free of emojis and fluff

---

## Current Capabilities

✅ YAML-based topic curation  
✅ Dynamic prompt processing  
✅ Autonomous post generation  
✅ OpenAI API integration fully functional  
✅ Scheduled posting every Wednesday at 13:00  
⏳ LinkedIn API integration in progress  
⏳ Auto-sourcing of reference links (planned)  

---

## Tech Stack


| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python 3.11  | Core language                    |
| OpenAI GPT-4 | Text generation                  |
| PyYAML       | YAML integration                 |
| Cron         | Scheduled post execution         |
| GitHub       | Version control                  |
| Notion       | Project management (optional)    |

---

## Demo

> This short demo shows the agent running in a terminal, processing topics from a YAML file, sending prompts to GPT-4, and saving the resulting LinkedIn posts as Markdown files.

![Demo Animation](docs/demo.gif)

Each post is automatically saved to the `posts/` directory and logged in `logs/agent.log`.

---

## Goals
- Raise awareness for bias in AI
- Automate LinkedIn posts with YAML prompts
- Generate posts with GPT-4 via OpenAI API
- Structure & log posts as Markdown for traceability

---

## Motivation & Inspiration

As AI systems increasingly influence social, economic, and political realities, it's crucial to embed ethics into the development pipeline.  
This agent was built to:

- Make bias and fairness in LLMs more visible  
- Automate education on overlooked but critical topics  
- Support responsible AI communication in public discourse

`ethical_ai_post_agent` is my way of using technology to bring **awareness, reflection, and change** into the feed.

🧠 Let’s build AI with **intention** — not just with instructions.

---
## Features
- Parses topic YAML from `data/topics.yaml`
- Uses `gpt-3.5-turbo` or `gpt-4` to generate posts
- Creates `.md` files inside `/posts`
- Logs output in `/logs`
- Optional: image prompts & DALL·E support
- Secure API key handling with `.env`

---

## Project Structure

<pre lang="markdown">
## 📁 Project Structure

```
ethical_ai_post_agent/
├── data/                      # YAML input topics
│   └── topics.yaml
├── posts/                     # Generated posts (.md)
├── prompts/                   # Prompt templates (e.g. post_prompt.txt)
├── docs/                      # Demo GIFs, documentation assets
│   └── demo.gif
├── logs/                      # Logs (optional)
├── venv/                      # Python virtual environment (excluded)
├── main.py                    # Core agent logic
├── scheduler.py               # Weekly post automation with APScheduler
├── publish_post.py            # Placeholder for LinkedIn API post
├── get_access_token.py        # LinkedIn API token handler
├── get_organisation_urn.py    # Fetch organisation URN from LinkedIn
├── linkedin_callback.py       # Handles LinkedIn OAuth callback (WIP)
├── test_connection.py         # API key test script
├── config.yaml                # Global parameters & settings
├── .env                       # API key (excluded via .gitignore)
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
└── old_main.py                # Backup of previous `main.py` version
```
</pre>

---

## To Do
- [x] Connect GPT-4 for generation
- [x] APScheduler Automation
- [x] Demo GIF Integration
- [ ] Finalize LinkedIn API integration (read/write to company pages)
- [ ] Implement fallback post queue
- [ ] Build minimal frontend CLI interface
- [ ] Improve link recommendation with curated database

---

## License

This project is part of the **FemAI Community** and will be released under an open-source license once core functionality is stable.
Don't build disinfo-bots 🙏

---

## Maintainer

Made with ❤️ by [shinan.dev](https://github.com/shinanDev)  
GPG-signed & committed.  
Ambassador for Ethical AI — always open for feedback and collaboration.
