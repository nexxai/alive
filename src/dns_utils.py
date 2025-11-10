import socket


def check_alive(hostnames):
    alive = []
    for hostname in hostnames:
        try:
            socket.gethostbyname(hostname)
            alive.append(hostname)
        except socket.gaierror:
            pass
    return alive
