from pathlib import Path
from os.path import dirname

def read_data(filename: str) -> str:

    file = Path(dirname(__file__)) / '..' / Path('data') / filename
    with file.open() as f:
        return f.read().strip()