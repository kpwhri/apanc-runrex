import os

path = r'examples/data'
config = {
    'corpus': {
        'directory': os.path.join(path, 'corpus')
    },
    'output': {
        'name': 'apanc_runrex_results_{datetime}',
        'kind': 'jsonl',
        'path': os.path.join(path, 'out')
    },
}
print(config)
