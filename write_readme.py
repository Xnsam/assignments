"""Update the readme files."""

import os

path = os.getcwd()


with open('README.md', 'w') as f:
    for i in os.listdir(path):
        s = i.split('.')
        if s[0] != 'write_readme':
            f.write(s[0] + '\n')
