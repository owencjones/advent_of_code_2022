from hashlib import sha3_384
from typing import Union

def simple_hash(input: Union[str, int]) -> str:
    return sha3_384.hexdigest(
        input.encode('utf-8')
    )