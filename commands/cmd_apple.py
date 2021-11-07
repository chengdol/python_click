import click

@click.command("apple")
@click.argument("count", type=int, default=1)
@click.option("--fg-color", "-fc",
               type=click.Choice(["green", "red"]))
@click.pass_context
def cli(ctx, count, fg_color):
    """This is apple subcommand

    COUNT: loop count
    """
    debug = ctx.obj["DEBUG"] if ctx.obj else None
    if debug:
        click.echo(click.style("Debug", fg=fg_color) + " is enabled!")
    for idx in range(count):
        click.secho(f"loop {idx + 1}", fg=fg_color)

if __name__ == "__main__":
    cli()