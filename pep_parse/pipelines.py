import datetime as dt
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def __init__(self):
        self.counter = Counter()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_dir = result_dir / file_name
        with open(file_dir, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.counter.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{sum(self.counter.values())}')
