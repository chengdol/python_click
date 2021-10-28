import click

@click.command()
@click.argument("b1", type=int, default=1)
def cli(b1):
    print("from cmd_b dududu!")
    for i in range(b1):
        print('cmd_b')