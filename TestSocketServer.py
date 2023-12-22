import socket
import threading


def send_data():
    # 发送回复消息给客户端
    client_socket.send(bytes([0x01, 0x03, 0x02, 0x00, 0x00, 0x03, 0x04, 0x73]))

    data = client_socket.recv(1024)
    print('收到消息:', data)


# 创建Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_address = ('192.168.1.100', 8234)
server_socket.bind(server_address)

# 监听客户端连接
server_socket.listen(10)
print('服务器已启动，等待客户端连接...')

# 接受客户端连接
client_socket, client_address = server_socket.accept()
print('客户端已连接:', client_address)

threading.Timer(interval=5, function=send_data).start()

# 接收客户端消息
data = client_socket.recv(1024)
print('收到消息:', data)

# 关闭连接
client_socket.close()
server_socket.close()
