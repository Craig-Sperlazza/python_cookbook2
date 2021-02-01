import click


#How to communicate data from the group to the other functions

#have to make a config class
class Config(object):
    def __init__(self):
        self.verbose = False

#this creates a decorator function which passes a config object to each click callback function
pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home_directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory


@cli.command()
@click.option('--string', default='World', help="string name to be passed into function")
@click.option('--repeat', default=1, help="How many times you should be greeted")
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def say(config, string, repeat, out):
    """This script greets you

    Args:
        out (file): output to a file 
        
    """
    if config.verbose:
        click.echo("We are in verbose mode")
    click.echo(f"Home directory is {config.home_directory}")
    out.write("Here is some text \n")

    #use click.echo instead of print---print doesnt behave well on some terminals
    #when you put file in the command it write to a file instead of stdout
    for i in range(repeat):
        click.echo(f"Hello {string}", file=out)







# #This is with subarguments---use click.group()
# @click.group()
# @click.option('--verbose', is_flag=True)
# def cli(verbose):
#     if verbose:
#         click.echo('We are in verbose mode')
#     # hello --verbose say  --repeat 3 foo.txt   will run the verbose function and the say
#     # hello --repeat 3 foo.txt   will run only the say function


# @cli.command()
# @click.option('--string', default='World', help="string name to be passed into function")
# @click.option('--repeat', default=1, help="How many times you should be greeted")
# @click.argument('out', type=click.File('w'), default='-', required=False)
# def say(string, repeat, out):
#     """This script greets you

#     Args:
#         out (file): output to a file 
        
#     """
#     out.write("Here is some text \n")

#     #use click.echo instead of print---print doesnt behave well on some terminals
#     #when you put file in the command it write to a file instead of stdout
#     for i in range(repeat):
#         click.echo(f"Hello {string}", file=out)





#This is without subarguments
# @click.command()
# @click.option('--string', default='World', help="string name to be passed into function")
# @click.option('--repeat', default=1, help="How many times you should be greeted")
# @click.argument('out', type=click.File('w'), default='-', required=False)
# def cli(string, repeat, out):
#     """This script greets you

#     Args:
#         out (file): output to a file 
        
#     """
#     out.write("Here is some text \n")

#     #use click.echo instead of print---print doesnt behave well on some terminals
#     #when you put file in the command it write to a file instead of stdout
#     for i in range(repeat):
#         click.echo(f"Hello {string}", file=out)
