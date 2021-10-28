import click
import logging
import os

logger = logging.getLogger(__name__)

class CustomCLI(click.MultiCommand):
    """Complex Group initiator
    """

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx: click.Context, cmd_name: str):
        """
        Override get_command from inherited class

        :param ctx: context
        :param cmd_name: command name
        """
        #print(cmd_name)
        #import_path = self.plugin_folder.replace('/', '.').strip('.')
        #mod = __import__("utils.commands" + "." + cmd_name, fromlist=['cli'])
        #print(dir(mod))
        #print(type(mod))
        #return mod.cli

        ns = {}
        fn = os.path.join(self.plugin_folder, cmd_name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']







