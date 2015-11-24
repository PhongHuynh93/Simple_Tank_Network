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

Giới thiệu về game:

1. Màn chơi

Game sẽ có 2 màn chơi là màn chơi thường và màn chơi boss. Người chơi thứ 1 sẽ là chiếc xe tăng màu đỏ, người chơi thứ 2 sẽ là chiếc xe tăng màu đen. Mỗi người chơi sẽ gồm 5 máu. Khi đụng trúng bất kì quái vật nào trong màn hình thì máu của người chơi sẽ bị giảm 1. 

2. Các loại quái vật trong game:

- Xe tăng màu den: ta cần viết đủ 10 con xe tăng màu đen. Mỗi con xe tăng có máu là 5.

- Con rắn: ta không thể giết được nó, nó xuất hiện và biến mất rất nhanh. Mục đích của con rắn là trừ máu của người chơi bằng cách xuất hiện tại 1 vị trí bất thình lình.

- Boss: sau khi viết đủ 10 xe tăng màu đen ta sẽ đánh được boss. Boss có 20 máu, nó bắn đạn ra 8 hướng, xuất hiện và biến mất tại vị trí bất kì trên màn hình.

3. Vật dụng hỗ trợ trong game

- Viên màu đỏ: sẽ cho ta khả năng bắn đạn liên tiếp.
