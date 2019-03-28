#!/usr/bin/env python3

import optparse

cmd = 'Divorce with Karen --timezone -6'

parser = optparse.OptionParser(cmd)
#parser.add_option("--name", dest="groupname")
parser.add_option("--timezone", dest="timezone", default="0")


(options, args) = parser.parse_args(cmd.split(" "))
print(args)
print(options)
print("="*10)
print(f'Group name: {" ".join(args)}')
print(f'Timezone: {options.timezone}')