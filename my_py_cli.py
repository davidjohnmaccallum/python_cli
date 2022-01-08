import click

@click.group()
def cli():
    pass

@click.command()
def hello():
    """Example script."""
    click.echo('Hello World!')

@click.command()
def goodbye():
    """Example script."""
    click.echo('Goodbye!')

cli.add_command(hello)
cli.add_command(goodbye)