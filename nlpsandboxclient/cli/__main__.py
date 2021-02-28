#!/usr/bin/env python3
import click

from .. import __version__
from . import annotator_cli, community, datanode_cli, evaluate


@click.group()
@click.version_option(__version__)
def cli():
    """NLP Sandbox Client"""


def main():
    cli.add_command(community.cli)
    cli.add_command(evaluate.evaluate_prediction)
    cli.add_command(datanode_cli.cli)
    cli.add_command(annotator_cli.cli)
    cli()
