import socket

# 创建Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('192.168.1.101', 8899)
client_socket.connect(server_address)

# 发送消息给服务器
# client_socket.send(bytes([0x01, 0x03, 0x00, 0x00, 0x00, 0x02, 0xC4, 0x0B]))
client_socket.send(bytes([0x01, 0x03, 0x02, 0x00, 0x00, 0x03, 0x04, 0x73]))

# 接收服务器回复消息
reply = client_socket.recv(1024)
print('收到回复:', reply.decode())

# 关闭连接
client_socket.close()
