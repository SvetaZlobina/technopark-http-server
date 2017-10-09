import argparse

from http_server import HttpServer

def parse_args():
    parser = argparse.ArgumentParser(description='http server for static files')
    parser.add_argument('-r', '--root', type=str, help='Root directory')
    parser.add_argument('-c', '--ncpu', type=int, help='Numper of CPU')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    server = HttpServer()
    # todo: server.start()
