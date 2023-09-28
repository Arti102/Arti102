from datetime import datetime
from django_cron import CronJobBase

import views

class MyCronJob(CronJobBase):
    schedule = "0 10,22 * * *"  # Run twice daily at 10:00 AM and 10:00 PM

    def do(self):
        url = 'https://housing.com/'
        database_name = 'admin'  
        collection_name = 'housing'  
        views.scrape_and_save_to_mongodb(url,"admin", "housing")   
        print(f"MyCronJob ran at {datetime.now()}")


