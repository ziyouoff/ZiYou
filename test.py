import os 


try:
    from colorama import init, Fore
    from colorama import Back
    from colorama import Style
except:
    os.system('pip install colorama')
    from colorama import init, Fore
    from colorama import Back
    from colorama import Style

try:
    from pystyle import Center
except:
    os.system('pip install pystyle')
    from pystyle import Center

try:
    from termcolor import colored
except:
    os.system('pip install termcolor')
    from termcolor import colored

try:
    from rich import print as rprint
    from rich.console import Console
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.tree import Tree
except:
    os.system('pip install rich')
    from rich import print as rprint
    from rich.console import Console
    from rich.layout import Layout
    from rich.tree import Tree

try:
    import pendulum
except:
    os.system('pip install pendulum')
    import pendulum


console = Console(record=True)
console.export_svg("test.svg")