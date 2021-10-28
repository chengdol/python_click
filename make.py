import click
from utils.custom_cli import CustomCLI

@click.command(cls=CustomCLI)
@click.pass_context
def cli(ctx):
    pass

if __name__ == "__main__":
    cli()
