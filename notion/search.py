"""Search utilities"""

from typing import List, Tuple
from .client import NotionClient
from .block import Block, CollectionViewBlock

counter = 0

def search(client: NotionClient, url_or_id: str):
    """Search for databases (colelctions) inside given block"""
    print("Searching...")
    block = client.get_block(url_or_id)
    results = _search_in(block)
    print(".")
    print("Found:\n" + "\n".join(f"{name} :: {pid}" for name, pid in results))

def _search_in(block: Block) -> List[Tuple[str, str]]:
    global counter
    counter += 1
    print(f"\r{counter}", end="", flush=True)
    results = []
    if isinstance(block, CollectionViewBlock):
        results.append((block.title, block.id))
    for child in block.children:
        results.extend(_search_in(child))
    return results
