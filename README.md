# ethical_ai_post_agent

🚀 Automatisierter LinkedIn-Bot für Ethical AI Content  
Ein Python-basierter Agent, der auf Basis kuratierter YAML-Themen Thought-Leadership-Posts über Bias, Fairness und Diversity in LLMs erstellt, mit GPT-4 generiert und als Markdown speichert.

---

## Highlights

✅ YAML-gesteuertes Topic-Management  
✅ GPT-4 Content-Generierung über OpenAI API  
✅ Markdown-Output + Logging  
✅ Clean Code & CLI-freundlich  
✅ Bereit für LinkedIn-Scheduling & DALL·E Erweiterung

---

## Tech Stack

| Tool            | Einsatzgebiet               |
|-----------------|-----------------------------|
| Python 3.13     | Core Language               |
| OpenAI API      | Textgenerierung             |
| PyYAML          | YAML-Einbindung             |
| Schedule        | Zeitbasierte Ausführung     |
| dotenv          | API-Schlüssel-Handling      |

---

## Demo

Das folgende GIF zeigt, wie ein YAML-Thema in Markdown-Text umgewandelt und lokal gespeichert wird.

📍 *Ablageort: `posts/` + Logs in `logs/`*

![Demo Animation](docs/demo.gif)

*Automatisch generierter Beitrag durch den `ethical_ai_post_agent`.*

---

## Goals
- Raise awareness for bias in AI
- Automate LinkedIn posts with YAML prompts
- Generate posts with GPT-4 via OpenAI API
- Structure & log posts as Markdown for traceability

---

## Motivation & Inspiration

In einer Welt, in der Künstliche Intelligenz immer häufiger Entscheidungen trifft, ist es entscheidend, die **ethischen Fragen** nicht zu übersehen.

Dieses Projekt entstand aus dem Wunsch, einen Beitrag zu leisten für:

- **Mehr Sichtbarkeit** für Bias & Fairness in LLMs  
- **Automatisierte Bildung** über Themen, die oft im Schatten technischer Euphorie stehen  
- **Verantwortungsvollere KI-Systeme**, die Menschen einschließen statt ausschließen  

Der `ethical_ai_post_agent` ist mein Weg, mit Technologie **Aufklärung, Reflexion und Veränderung** in die Feeds zu bringen.

🧠✨ Let's build AI with **intention** – not just with instructions.

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
ethical_ai_post_agent/
│
├── data/                # YAML input topics
│   └── topics.yaml
│
├── posts/               # Generated posts (.md)
├── logs/                # Logs (optional)
├── main.py              # Agent logic
├── config.yaml          # Parameters & settings
├── test_connection.py   # Optional API test script
├── .env                 # API key (excluded via .gitignore)
└── README.md

---

## To Do
- [x] Connect GPT-4 for generation
- [ ] Add LinkedIn scheduling (via API)
- [ ] Integrate DALL·E for visual content
- [ ] Web dashboard (optional)
- [ ] Post-validation with regex / review

---

## License

MIT License – Use responsibly.  
Don't build disinfo-bots 🙏

---

## Maintainer

Made with ❤️ by [shinan.dev](https://github.com/shinanDev)  
GPG-signed & committed.  
Ambassador for Ethical AI ✨
