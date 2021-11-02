import click

@click.group()
@click.pass_context
def functions(ctx):
    ctx.obj['functions'] = ctx.obj['workspace'].functions

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
