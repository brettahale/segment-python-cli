import click
import json
# from app.segment.functions import functions

@click.group()
@click.pass_context
def functions(ctx):
    #override workspace api by workspace id and not name
    workspace = ctx.obj['workspace'].get()
    ctx.obj['workspace'] = ctx.obj['api'].workspace(workspace['id'])
    ctx.obj['functions'] = ctx.obj['workspace'].functions
    click.echo(ctx.obj['functions'])

@functions.command()
@click.option('--function-type' , type=click.Choice(['source', 'destination']), required = True, help='Segment API Token')
@click.pass_context
def list(ctx, function_type):
    click.echo(json.dumps(ctx.obj['functions'].list(function_type=function_type.upper(), page_size=100)))

@functions.command()
@click.argument('id')
@click.pass_context
def get(ctx, id):
    click.echo(json.dumps(ctx.obj['functions'].function(id).get()))
