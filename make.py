import os
import click
from utils import CustomCLI

@click.command(cls=CustomCLI,
               path=os.path.dirname(__file__),
               dir_name="commands")
@click.option("--debug/--no-debug",
              default=False,
              help="Display verbose message")
@click.pass_context
def cli(ctx, debug):
    """
    This is a subcommands wrapper
    """
    # ensure ctx.obj exists and a dict type
    # https://click.palletsprojects.com/en/latest/commands/#nested-handling-and-contexts
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug

if __name__ == "__main__":
    cli(obj={})
