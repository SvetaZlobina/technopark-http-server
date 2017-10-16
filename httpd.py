import argparse
import os
import sys

from server import Server


def parse_args():
    parser = argparse.ArgumentParser(description='http server for static files')
    parser.add_argument('-r', '--root', type=str, help='root directory')
    parser.add_argument('-c', '--ncpu', type=int, help='numper of CPU', default=os.cpu_count())
    return parser.parse_args()


def run():
    args = parse_args()

    if not os.path.exists(args.root):
        print('Root directory is invalid!')
        sys.exit()

    server = Server(args.root, args.ncpu)
    server.start()

if __name__ == '__main__':
    run()

