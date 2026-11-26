import json
from pathlib import Path

def source(name, index):
    nb=json.loads((Path(__file__).resolve().parents[1]/'notebooks'/f'{name}.ipynb').read_text())
    return ''.join(nb['cells'][index]['source'])

import ast
ast.parse(source('diabetes-classification-baseline', 1))

print('Targeted regression passed; no original-data performance claim.')
