# -*- coding: utf-8 -*-

"""Top-level package for CLI App"""

import click
import os

from .segment.segment_config_api import SegmentConfigApi

from .commands.sources import sources
from .commands.destinations import destinations
from .commands.filters import filters
from .commands.functions import functions
from .commands.regulations import regulations

__author__ = """Brett Hale"""
__email__ = 'bhale@goodrx.com'
__version__ = '0.0.1'

@click.group()
@click.option('-t', '--token' , envvar='SEGMENT_TOKEN', help='Segment API Token')
@click.option('-w', '--workspace', default='default', envvar='SEGMENT_WORKSPACE', help='Which segment workspace?')
@click.option('-f', '--format', default='text', help='Output format [text:default, yaml, json]')
@click.option('-p', '--path', default=None, help='Write as file to directory')
@click.pass_context
def cli(ctx, token, workspace, format, path):
    ctx.ensure_object(dict)
    api = SegmentConfigApi(token)
    ctx.obj['api'] = api
    ctx.obj['workspace'] = api.workspace(workspace)
    ctx.obj['output_format'] = format
    ctx.obj['output_path'] = path


# Add commands
cli.add_command(sources)
cli.add_command(destinations)
cli.add_command(filters)
cli.add_command(functions)
cli.add_command(regulations)