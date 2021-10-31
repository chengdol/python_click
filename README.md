## Python Click Module

[click](https://click.palletsprojects.com/en/8.0.x/) module is used to create command line application.

This repo contains a pattern/structure that is easy to extend subcommands, [reference](https://click.palletsprojects.com/en/8.0.x/commands/#custom-multi-commands), here we have 2 commands: `apple` and `peach`, we can invoke them as the subcommand of `make.py`(wrapper).

```bash
# call for help message
python make.py --help
python make.py apple --help
python make.py peach --help

# execution
python make.py --debug apple -fc red 5
python make.py --debug peach -bc blue 5
```