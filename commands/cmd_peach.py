import click

@click.command("peach")
@click.argument("count", type=int, default=1)
@click.option("-bc", "--bg-color",
              type=click.Choice(["cyan", "blue"]))
@click.pass_context
def cli(ctx, count, bg_color):
    """This is peach subcommand

    COUNT: loop count
    """
    debug = ctx.obj["DEBUG"] if ctx.obj else None
    if debug:
        click.echo(click.style("Debug", bg=bg_color) + " is enabled!")
    for idx in range(count):
        click.secho(f"loop {idx + 1}", bg=bg_color)

if __name__ == "__main__":
    cli()