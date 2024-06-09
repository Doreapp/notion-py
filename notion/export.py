"""Export utilities"""

from .block import CollectionViewBlock
from .client import NotionClient


def export(client: NotionClient, url: str, only_csv: bool = False):
    """Export a page from URL"""
    block = client.get_block(url)
    if only_csv and not isinstance(block, CollectionViewBlock):
        raise Exception("--only-csv can only be used with a collection id/url")
    if only_csv:
        block.export("export", True)
    else:
        block.export("export")
