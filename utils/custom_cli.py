import click
import os

# custom multi-commands:
# https://click.palletsprojects.com/en/latest/commands/#custom-multi-commands
class CustomCLI(click.MultiCommand):

    def __init__(self, path, dir_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_dir = os.path.join(path, dir_name)

    def list_commands(self, ctx):
        """
        Override list_commands from inherited class

        :param ctx(click.Context): context
        """
        rv = []
        for filename in os.listdir(self.command_dir):
            if filename.startswith("cmd_") \
                and filename.endswith(".py"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, cmd_name):
        """
        Override get_command from inherited class

        :param ctx(click.Context): context
        :param cmd_name(str): command name
        """     
        ns = {}
        filename = os.path.join(self.command_dir, "cmd_" + cmd_name + '.py')
        with open(filename) as fn:
            # compile
            # https://docs.python.org/3/library/functions.html#compile
            code = compile(fn.read(), filename, "exec")
            # eval
            # https://docs.python.org/3/library/functions.html#eval
            # here is a good explanation of eval parameters:
            # https://www.geeksforgeeks.org/eval-in-python/
            # None is returned because of exec argument in compile
            eval(code, ns, ns)
        # builtins are inserted in globals dictionary
        # cli is the function name in command script
        return ns['cli']
