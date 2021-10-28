import click

@click.command()
@click.argument("a1", type=int, default=1)
def cli(a1):
    print("from cmd_a hahaha!")
    for item in range(a1):
        print("cmd_a")