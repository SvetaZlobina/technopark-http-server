import os
import socket

import server_config
from request_handler import RequestHandler


class Server:
    workers = []

    def __init__(self, root_dir, workers=1):
        self.root_dir = root_dir
        self.workers_num = workers
        self.host = server_config.HOST
        self.port = server_config.PORT
        self.listeners = server_config.LISTENERS
        self.msg_size = server_config.MSGSIZE
        self.handler = RequestHandler
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def start(self):
        print('Running server: {} on host {} port: {}'
              .format(server_config.SERVER_NAME, server_config.HOST, server_config.PORT))
        print('Number of CPU: {}'.format(self.workers_num))

        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind((self.host, self.port))
        self.server_sock.listen(self.listeners)

        for _ in range(self.workers_num):
            pid = os.fork()
            if pid:
                self.workers.append(pid)
            else:
                print('Running worker with PID: {}'.format(os.getpid()))
                while True:
                    client_sock, client_address = self.server_sock.accept()
                    request = client_sock.recv(self.msg_size)

                    if request.strip() == 0:
                        client_sock.close()
                        continue

                    handler = self.handler(request, self.root_dir)
                    response = handler.handle()

                    client_sock.sendall(response.build())
                    client_sock.close()

        self.server_sock.close()

        for pid in self.workers:
            os.waitpid(pid, 0)
