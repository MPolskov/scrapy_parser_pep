import csv
from collections import defaultdict
import datetime as dt


class PepPipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        pep_count = sum(self.status_count.values())
        date_time_now = dt.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        filename = f'results/status_summary_{date_time_now}.csv'
        with open(filename, 'w', newline='') as csvfile:
            pep_writer = csv.writer(csvfile)
            pep_writer.writerow(['Статус', 'Количество'])
            pep_writer.writerows(self.status_count.items())
            pep_writer.writerow(['Total', pep_count])
