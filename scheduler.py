from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import logging

# Logging zur Fehlerdiagnose
logging.basicConfig(level=logging.INFO)

# Funktion, die das Posting-Skript startet
def run_post_script():
    logging.info("Starte publish_post.py...")
    try:
        subprocess.run(["python3", "publish_post.py"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler beim Ausführen von publish_post.py: {e}")

# Scheduler-Instanz
scheduler = BlockingScheduler()

# Cron-Trigger: jeden Mittwoch um 13:00 Uhr
scheduler.add_job(run_post_script, 'cron', day_of_week='wed', hour=13, minute=0)

if __name__ == "__main__":
    logging.info("Scheduler läuft. Nächster Post kommt am Mittwoch um 13:00 Uhr.")
    scheduler.start()