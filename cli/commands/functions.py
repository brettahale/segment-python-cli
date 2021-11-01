import click
from app.segment.functions import

@click.group()
@click.pass_context
def destinations(ctx):
    ctx.obj['functions'] = ctx.obj['workspace'].functions
