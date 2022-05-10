import os

path = r'examples/data'
config = {
    'corpus': {
        'directory': os.path.join(path, 'corpus'),
        'connections': [
            {
                'name': os.path.join(path, 'corpus.csv'),
                'name_col': 'doc_id',
                'text_col': 'text',
            }
        ]
    },
    'output': {
        'name': 'apanc_runrex_results_{datetime}',
        'kind': 'jsonl',
        'path': os.path.join(path, 'out')
    },
}
print(config)
