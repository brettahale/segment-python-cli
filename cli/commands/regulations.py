import click
import copy
import json
import yaml


def get_delete_payload(users: []):
    return {
                   "regulation_type": "Suppress_With_Delete",
                   "attributes": {
                       "name": "userId",
                       "values": users
                   }
               }

@click.group()
@click.pass_context
def regulations(ctx):
    ctx.obj['regulations'] = ctx.obj['workspace'].regulations

@regulations.command()
@click.argument('user_list', type=click.File('rb'))
@click.pass_context
def create(ctx, user_list):
    users = [line.strip().decode() for line in user_list]
    click.echo(json.dumps(ctx.obj['regulations'].create(get_delete_payload(users))))

@regulations.command()
@click.pass_context
def list(ctx):
    click.echo(json.dumps(ctx.obj['regulations'].list()))

@regulations.command()
@click.argument('regulation_id')
@click.pass_context
def get(ctx, regulation_id):
    regulation_data = ctx.obj['regulations'].regulation(regulation_id).get()
    click.echo(regulation_data)

@regulations.command()
@click.argument('regulation_id')
@click.pass_context
def delete(ctx, regulation_id):
    regulation_data = ctx.obj['regulations'].regulation(regulation_id).delete()
    click.echo(regulation_data)
