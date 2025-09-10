import schedule
import time
from disk_usage_checker.disk_usage_cli import check_disk_usage

def job():
    print("Running disk usage check...")
    check_disk_usage(path="/") 

if __name__ == "__main__":
    schedule.every(1).minutes.do(job)  
    print("Scheduler for checking disk usage started")
    while True:
        schedule.run_pending()
        time.sleep(1)
