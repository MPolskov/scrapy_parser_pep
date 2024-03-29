from pathlib import Path

BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).resolve().parent.parent

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

# Spider pep.py
PEP_NAME = 'pep'
PEP_DOMAINS = ['peps.python.org']
PEP_URLS = ['https://peps.python.org/']
