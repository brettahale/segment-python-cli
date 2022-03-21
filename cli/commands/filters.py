import click
import json

@click.group()
@click.pass_context
def filters(ctx):
    pass

@filters.command()
@click.argument('source_name')
@click.argument('destination_name')
@click.pass_context
def list(ctx, source_name, destination_name):
    ctx.obj['filters'] = ctx.obj['workspace']\
        .sources.source(source_name)\
        .destinations.destination(destination_name)\
        .filters
    click.echo(json.dumps(ctx.obj['filters'].list()))

@filters.command()
@click.argument('source_name')
@click.argument('destination_name')
@click.argument('id')
@click.pass_context
def get(ctx, source_name, destination_name, id):
    ctx.obj['filters'] = ctx.obj['sources'].sources(source_name).destinations(destination_name).filters.get()
    click.echo(json.dumps(ctx.obj['filters'].filter(id).get()))

@filters.command()
@click.argument('source_name')
@click.argument('destination_name')
@click.argument('payload', type=click.File('rb'))
@click.pass_context
def create(ctx, source_name, destination_name, payload):
    ctx.obj['filters'] = ctx.obj['sources'].sources(source_name).destinations(destination_name).filters.get()
    click.echo(json.dumps(ctx.obj['filters'].create(json.dumps(get_delete_payload(payload)))))
