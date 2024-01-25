import sys

class CompatibleArgParser:
    '''Checks the python version of the system and imports the proper arg parsers'''
    def __init__(self):
        if sys.version_info[0] < 3:
            # Python 2.x
            from optparse import OptionParser
            self.parser = OptionParser()
        else:
            # Python 3.x
            import argparse
            self.parser = argparse.ArgumentParser(description="Change MAC address of a network interface.")

    def add_option(self, *args, **kwargs):
        if hasattr(self.parser, 'add_argument'):
            # argparse
            self.parser.add_argument(*args, **kwargs)
        else:
            # optparse
            self.parser.add_option(*args, **kwargs)

    def parse_args(self):
        if hasattr(self.parser, 'parse_args'):
            # argparse
            return self.parser.parse_args()
        else:
            # optparse
            return self.parser.parse_args()[0]


class ArgParser:
    def __init__(self):
        self.parser = CompatibleArgParser()

    def add_options(self):
        self.parser.add_option("-i", "--interface", dest="interface", help="Interface to have its MAC address changed", required=True)

    def parse_args(self):
        return self.parser.parse_args()