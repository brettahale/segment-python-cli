import click
import copy
import json
import yaml


@click.group()
@click.pass_context
def destinations(ctx):
    ctx.obj['sources'] = ctx.obj['workspace'].sources

@destinations.command()
@click.argument('source_names', nargs=-1)
@click.pass_context
def list(ctx, source_names):
    format_func = yaml.dump if ctx.obj['output_format'] == 'yaml' else json.dumps

    if len(source_names) == 0:
        source_list = ctx.obj['sources'].list(page_size=100)
        source_names = [source['name'].rsplit('/',1)[1] for source in source_list['sources']]

    destination_list = {'destinations': []}
    for src in source_names:
        source_destinations = ctx.obj['sources'].source(src).destinations.list(page_size=100)
        if len(source_destinations['destinations']) > 0:
            destination_list['destinations'] = destination_list['destinations'] + source_destinations['destinations']

    if ctx.obj['output_path'] is not None:
        for d in destination_list['destinations']:
            ctx.obj['sources'].write_to_file([ctx.obj['output_path'],ctx.obj['workspace'],d['name'].rsplit('/',1)[1], 'destination.yaml'], format_func(d))
    else:
        click.echo(format_func(destination_list))

@destinations.command()
@click.argument('source_name')
@click.argument('destination_name')
@click.pass_context
def get(ctx, source_name, destination_name):
    destination_data = ctx.obj['sources'].source(source_name).destinations.destination(destination_name).get()

    if ctx.obj['output_format'] == 'yaml':
        destination_data = yaml.dump(destination_data)
    else:
        destination_data = json.dumps(destination_data)

    if ctx.obj['output_path'] is not None:
        click.echo(destination_name)
        destinations.write_to_file([ctx.obj['output_path'],ctx.obj['workspace'],destination_name, 'destination.yaml'], destination_data)
    else:
        click.echo(destination_data)