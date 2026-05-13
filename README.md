# Sign_Languade_basic

# HƯỚNG DẪN SỬ DỤNG GIT & QUY TRÌNH LÀM VIỆC 

## I. Khái niệm (Core Concepts)

Trước khi bắt đầu, cần hiểu Git quản lý code thông qua 3 khu vực:

1. **Working Directory:** Thư mục trên máy tính .
2. **Staging Area:** Khu vực đệm, nơi chứa những thay đổi đã được chọn để chuẩn bị lưu.
3. **Repository (Local & Remote):** Nơi lưu trữ chính thức các phiên bản code (Local: ở máy cá nhân, Remote: ở trên GitHub).

## II. Tra cứu lệnh Git (Command Reference)

### 1. Nhóm lệnh khởi tạo và đồng bộ

| Lệnh      | Cú pháp (Syntax)              | Chức năng                                             |
|-----------|-------------------------------|-------------------------------------------------------|                     
| **Clone** | `git clone <url>`             | Tải toàn bộ dự án từ GitHub về máy tính lần đầu tiên. |
| **Pull**  | `git pull origin <tên_nhánh>` | Cập nhật code mới nhất từ trên GitHub về máy mình.    |
| **Push**  | `git push origin <tên_nhánh>` | Đẩy code đã lưu từ máy mình lên GitHub.               |

### 2. Nhóm lệnh làm việc hàng ngày

| Lệnh       | Cú pháp (Syntax)           | Chức năng                                                    |
|------------|----------------------------|--------------------------------------------------------------|
| **Status** | `git status`               | Kiểm tra trạng thái: file nào đã sửa, file nào chưa được lưu.|
| **Add**    | `git add <tên_file>`       | Đưa file vào "Staging Area" (Chuẩn bị đóng gói).             |
| **Commit** | `git commit -m "Lời nhắn"` | Lưu chính thức các thay đổi vào lịch sử kèm ghi chú rõ ràng. |

### 3. Nhóm lệnh quản lý Nhánh (Branching)

| Lệnh           | Cú pháp (Syntax)              | Chức năng                                            |
|----------------|-------------------------------|------------------------------------------------------|
| **Branch**     | `git branch`                  | Xem danh sách các nhánh đang có.                     |
| **Checkout**   | `git checkout <tên_nhánh>`    | Di chuyển từ nhánh này sang nhánh khác.              |
| **New Branch** | `git checkout -b <tên_nhánh>` | Tạo một nhánh mới và di chuyển sang đó ngay lập tức. |

---

## III. Quy trình làm việc (Cá nhân)

Để đảm bảo dự án vận hành ổn định,  trình gồm 5 bước sau:

### Bước 1: Chuẩn bị môi trường

Lần đầu nhận dự án, mở Terminal và thực hiện:

```bash
https://github.com/DakBun/Sign_Languade_basic.git
```

### Bước 2: Tạo nhánh làm việc cá nhân

Tuyệt đối không code trực tiếp trên nhánh `main`. 


### Bước 3: Cập nhật và Viết code

Trước khi code, luôn Pull để tránh xung đột:

```bash
git pull origin main
```

### Bước 4: Lưu và Đẩy code

Sau khi hoàn thành một tính năng hoặc bài tập:

```bash

git add . (Đưa toàn bộ file vào Staging Area)
git commit -m "[Module_Name] - Nội dung thay đổi chi tiết"
git push origin dev-<tên_thành_viên>

```

### Bước 5: Hợp nhất (Merge)

Sau khi Push, lên giao diện GitHub web để tạo **Pull Request (PR)**. 
## IV. Quy tắc đặt tên và Ghi chú (Convention)

1. **Nhánh (Branch):**
* Nhánh tính năng: `feature/<tên_tính_năng>`


2. **Lời nhắn Commit:**
* Cấu trúc: `[Thư mục/Loại file] - Mô tả ngắn gọn bằng tiếng Việt có dấu hoặc tiếng Anh.`
* Ví dụ: `[src/DSA] - Hoàn thành giải thuật Sắp xếp nổi bọt`

## V. Xử lý sự cố (Troubleshooting)

1. **Khi gặp Conflict (Xung đột):** Git báo không thể Merge.
* *Cách xử lý:* Mở VS Code, tìm các đoạn code được đánh dấu `<<<< HEAD`, Add và Commit lại.
2. **Gõ sai lệnh:** Sử dụng `git status` để xem hướng dẫn gợi ý từ Git.
3. **Mất code:** Code đã Commit thì không bao giờ mất. Liên hệ Manager để dùng lệnh `git reflog` khôi phục.
