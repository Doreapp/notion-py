"""Export utilities"""

from .client import NotionClient


def export(client: NotionClient, url: str):
    """Export a page from URL"""
    block = client.get_block(url)
    block.export("export")
