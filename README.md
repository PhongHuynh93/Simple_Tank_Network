# Simple_Tank_Network
Game chạy trên python 2.7

Di chuyển: nhấn wsad

Bắn đạn: nhấn Space

Cách chạy 2 người chơi qua LAN:

1. Chạy server.py bằng command line  

+ Nếu ta muốn chạy 2 client trên cùng 1 máy thì ta gõ vào command line dạng: localhost:port --> ví dụ như localhost:3000 
+ Nếu ta muốn chạy 1 client trên máy này và 1 client trên máy khác (kết nối qua dây LAN) thì ta gõ command line dạng: địa chỉ IP của máy tính ta đang sử dụng trong LAN:port --> ví dụ như 192.168.1.2:3000

2. Chạy main.py trên máy client 1
Máy sẽ hỏi bạn địa chỉ+port của server. Tùy vào bước 1 mà ta nhập tương ứng.  
Sau đó chọn Start Game -> 2 players để đăng nhập người chơi thứ 1. 

3. Chạy main.py trên máy client 2
Máy sẽ hỏi bạn địa chỉ+port của server. Tùy vào bước 1 mà ta nhập tương ứng.  
Sau đó chọn Start Game -> 2 players để đăng nhập người chơi thứ 1. 
