# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg_new>]

Options:
<arg1>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg_new>]       Takes any value (this is an positional optional argument)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(var):
    print(var)
    print(type(var))

main(opt)