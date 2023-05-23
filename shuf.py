import random, sys
import argparse

class shuf:

    def __init__(self):
        self.lines = []
   
def chooselines(lines, args, extra):
    ct = len(lines)
    if args.head_count:
        if args.head_count < ct:
            ct = args.head_count

    if args.repeat and args.head_count:
        for linect in range(args.head_count):
            line = random.choice(lines)
            strline = str(line)
            print(strline.rstrip("\n"))
    elif args.repeat and args.head_count is None:
        while True:
            line = random.choice(lines)
            strline = str(line)
            print(strline.rstrip("\n"))

    else:

        for line in random.sample(lines,ct):
            strline = str(line)
            print(strline.rstrip("\n"))


def main():

    parser = argparse.ArgumentParser( description = 'Shuffles input' , usage='shuf.py [-h] [-e | -i LO-HI] [-n COUNT] [-r] [FILENAME]')

    parser.add_argument("-n","--head-count",metavar="COUNT" ,type=int, help="Output at most COUNT lines")
    parser.add_argument("-r", "--repeat", action="store_true", help="output lines can be repeated")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e","--echo", action="store_true", help="Treat each argument as an input line")
    group.add_argument("-i","--input-range", metavar="LO-HI",help="treat each number LO through HI as an input line ")

    args, extra = parser.parse_known_args()

    if args.echo:
        lines = extra
    elif args.input_range:
        low, high = args.input_range.split("-")
        if int(low) > int(high) :
            parser.error("Invalid range. HI must be greater than LO")
            return
        lines = list(range(int(low), int(high)+1))
    elif len(extra) == 0: 
        lines = sys.stdin.readlines()
    elif sys.argv[1] == "-": 
        lines = sys.stdin.readlines()
    else:
        if len(extra) != 1:
            parser.error("extra operand '%s' " % extra[1])
            return
        filename =  extra[0]
        f = open(filename)
        lines = f.readlines()
        f.close
 
    chooselines(lines, args, extra)

    generator = shuf()

if __name__ == "__main__":
 main()
