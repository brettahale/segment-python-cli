import click
import copy
import json
import yaml


@click.group()
@click.pass_context
def sources(ctx):
    ctx.obj['sources'] = ctx.obj['workspace'].sources

@sources.command()
@click.pass_context
def list(ctx):
    click.echo(json.dumps(ctx.obj['sources'].list(page_size=100)))

@sources.command()
@click.argument('source_name')
@click.pass_context
def get(ctx, source_name):
    source_data = ctx.obj['sources'].source(source_name).get()

    if ctx.obj['output_format'] == 'yaml':
        source_data = yaml.dump(source_data)

    if ctx.obj['output_path'] != None:
        click.echo(source_name)
        sources.write_to_file([ctx.obj['output_path'],ctx.obj['workspace'],source_name, 'source.yaml'], source_data)
    else:
        click.echo(source_data)