# Ethical AI Post Agent – FemAI x GenAI Hackathon Submission

> Developed by Philipp Prinzen as part of the **FemAI community** – empowering ethical, feminist AI from Europe to the world.

---

## 🌐 Project Vision

The Ethical AI Post Agent is an open-source tool that automatically publishes **bias-aware LinkedIn posts** to foster public discourse on responsible AI, fairness, and diversity in LLMs.

Built within the **FemAI network** – a feminist AI governance initiative in Europe – this agent transforms curated YAML topics into short, professional LinkedIn content (<250 words) and aims to raise awareness, inspire reflection, and support ethical communication around generative AI.

This submission brings the FemAI voice into the **#LeadWithAIAgents** Hackathon hosted by GenAI.

This project is submitted as a solo entry for the #LeadWithAIAgents Hackathon hosted by GenAI. It demonstrates the potential of ethical agent communication at scale.

---

## 💡 What the Agent Does

- Reads curated YAML topic files (e.g., on bias, fairness, representation)
- Generates short LinkedIn-style posts using GPT-4-tuned prompts
- Stores or displays results for manual or automatic publishing
- Offers command-line interface for preview, test, and content rotation
- (Planned) Publishes via LinkedIn API to organizational accounts (currently under setup)

---

## 🔍 Why It Matters

Responsible AI needs more than just guardrails – it needs **public awareness**. This agent helps:
- bridge research and communication
- amplify underrepresented ethical narratives
- automate high-quality, inclusive content for professional platforms

---

## 🚧 Current Limitations

- **LinkedIn API** integration is not active during submission due to ongoing OAuth restrictions, but the structure is complete and tested with dummy endpoints.
- Deployment to a production workflow is planned post-hackathon.

---

## Tech Stack


| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python 3.11  | Core language                    |
| OpenAI GPT-4 | Text generation                  |
| PyYAML       | YAML integration                 |
| Cron         | Scheduled post execution         |
| GitHub       | Version control                  |
| Notion       | Project management               |


---

## Demo

> This short demo shows the agent running in a terminal, processing topics from a YAML file, sending prompts to GPT-4, and saving the resulting LinkedIn posts as Markdown files.

![Demo Animation](docs/demo.gif)

Each post is automatically saved to the `posts/` directory and logged in `logs/agent.log`.

---

## 🧪 Quick Start (Local Agent Run)

```bash
# Clone repo and enter project
git clone https://github.com/shinanDev/ethical_ai_post_agent.git
cd ethical_ai_post_agent

# (Optional) Create virtual env & install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the agent (YAML topics preloaded)
python main.py
```

---

## 🔧 Integration with GenAI AgentOS (Optional)

If needed, the agent can be wrapped as a `GenAI Agent`:
```bash
# Register (via GenAI CLI)
cd cli
python cli.py register_agent --name ethical_post_agent --description "Bias-aware post generator for LinkedIn"

# Run inside agents/
python ethical_post_agent.py
```

---

## Credits

- Project Lead: **Philipp Prinzen** (@shinanDev)
- Supported by: **FemAI** – feminist AI network for ethical tech futures by Alexandra Wudel (CEO)
- Submission: GenAI #LeadWithAIAgents Hackathon, 2025

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

## License

This project is part of the **FemAI Community** and will be released under an open-source license once core functionality is stable.
Don't build disinfo-bots 🙏

---

## Maintainer

Made with ❤️ by [shinan.dev](https://github.com/shinanDev)  
GPG-signed & committed.  
Ambassador for Ethical AI — always open for feedback and collaboration.