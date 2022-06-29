import argparse
import socket
import datetime

PORT_NUM = 200


def get_time_offset():
    with open('conf_time_lie.txt', 'r') as config:
        try:
            return int(config.read())
        except Exception:
            raise Exception("There must be an integer value")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="print '$sudo python3 {SCRIPT file_name}' to start",
                                     description="A simple lying time-server, working with a client-script")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('127.0.0.1', PORT_NUM))
        while True:
            data, addr = sock.recvfrom(1024)
            real_time = datetime.datetime.now()
            false_time = str(real_time + datetime.timedelta(0, get_time_offset()))
            sock.sendto(false_time.encode('utf-8'), addr)
