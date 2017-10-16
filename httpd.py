import argparse
import os
import sys

from server import Server
from server_config import DOCUMENT_ROOT, CPU_NUMBER


def parse_args():
    parser = argparse.ArgumentParser(description='http server for static files')
    parser.add_argument('-r', '--root', type=str, help='root directory', default=DOCUMENT_ROOT)
    parser.add_argument('-c', '--ncpu', type=int, help='numper of CPU', default=CPU_NUMBER)
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

