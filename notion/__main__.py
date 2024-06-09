"""Entrypoint for notion CLI"""

import argparse
import os

from .client import NotionClient

def main():
    """Main entrypoint"""
    parser = _build_cli_parser()
    args = parser.parse_args()
    token = args.token
    if not token:
        token_from_env = os.getenv("NOTION_TOKEN")
        if not token_from_env:
            raise argparse.ArgumentError(args.token, "Token is missing, either use --token argument or NOTION_TOKEN environment variable")
        token = token_from_env
    client = NotionClient(token_v2=token)
    if args.command == "export":
        export(client, args.url)
    else:
        parser.print_help()
        raise SystemExit

def export(client: NotionClient, url: str):
    """Export a Notion page from URL"""
    print("TODO export", url)


def _build_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notion",
        description="Command line tool to interface with Notion",
    )
    parser.add_argument("-t", "--token", help="Notion token (v2). Environment variable: NOTION_TOKEN")
    subparsers = parser.add_subparsers(title="command", dest="command")
    export_parser = subparsers.add_parser("export", help="Export a notion page in Markdown and CSV")
    export_parser.add_argument("url", help="Page URL")
    return parser

if __name__ == "__main__":
    main()