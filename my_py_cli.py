import click

@click.command()
def hello():
    """Example script."""
    click.echo('Hello World!')