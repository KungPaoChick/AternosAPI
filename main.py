from aternosapi import AternosAPI


headers_cookie = ""
TOKEN = ""
server = AternosAPI(headers_cookie, TOKEN)

def cmd(cmd):
	if cmd == "start":
		print(server.StartServer())
	if cmd == "stop":
		print(server.StopServer())
	if cmd == "status":
		print(server.GetStatus())
	if cmd == "info":
		print(server.GetServerInfo())
	if cmd == "playerinfo":
		print(server.GetPlayerInfo())

try:
	while True:
		icmd = input("[*] > ")
		cmd(icmd)
except KeyboardInterrupt:
	print('\nStopped!')