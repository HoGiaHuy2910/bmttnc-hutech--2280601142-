import socket
import ssl
import threading

server_address = ("localhost", 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode("utf-8"))
    except Exception as e:
        print("Lỗi nhận dữ liệu:", e)
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng")

# ===== Tạo socket TCP =====
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ===== SSL context =====
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# ===== Wrap SSL (CHỈ 1 LẦN) =====
ssl_socket = context.wrap_socket(
    client_socket,
    server_hostname="localhost"
)

# ===== Connect (CHỈ 1 LẦN) =====
ssl_socket.connect(server_address)
print("Đã kết nối tới server")

# ===== Luồng nhận =====
receive_thread = threading.Thread(
    target=receive_data,
    args=(ssl_socket,),
    daemon=True
)
receive_thread.start()

# ===== Gửi dữ liệu =====
try:
    while True:
        message = input("Nhập tin nhắn: ")
        if message.lower() == "exit":
            break
        ssl_socket.sendall(message.encode("utf-8"))
except KeyboardInterrupt:
    print("\nThoát chương trình")
finally:
    ssl_socket.close()