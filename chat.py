import socket 
import threading


def send_func():
	while True:
		send = input()
		connection.send(str.encode(send))
def rec_func():
	while True:
		received_data = connection.recv(1024)
		print(str(received_data))



if __name__ == "__main__":

	friend_ip='localhost'
	friend_port=4444
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect((friend_ip, friend_port))
	thread1 = threading.Thread(target = send_func)
	thread1.start()
	thread2 = threading.Thread(target = rec_func)
	thread2.start()