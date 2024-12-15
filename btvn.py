import tkinter as tk
from tkinter import messagebox
import datetime

class Quanlynhanvien:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý nhân viên")
        self.quanlynhanvien = []
        # các ô nhập thông tin
        tk.Label(root, text="Mã:").grid(row=0, column=0)
        self.ma = tk.Entry(root)
        self.ma.grid(row=0, column=1)
        tk.Label(root, text="Tên:").grid(row=1, column=0)
        self.ten = tk.Entry(root)
        self.ten.grid(row=1, column=1)
        tk.Label(root, text="Ngày sinh :").grid(row=2, column=0)
        self.ngaysinh = tk.Entry(root)
        self.ngaysinh.grid(row=2, column=1)
        tk.Label(root, text="Giới tính:").grid(row=3, column=0)
        self.gioitinh = tk.Entry(root)
        self.gioitinh.grid(row=3, column=1)
        tk.Label(root, text="Đơn vị:").grid(row=4, column=0)
        self.donvi = tk.Entry(root)
        self.donvi.grid(row=4, column=1)
        tk.Label(root, text="Số CMND:").grid(row=5, column=0)
        self.cmnd = tk.Entry(root)
        self.cmnd.grid(row=5, column=1)
        tk.Label(root, text="Ngày cấp:").grid(row=6, column=0)
        self.ngaycap = tk.Entry(root)
        self.ngaycap.grid(row=6, column=1)
        tk.Label(root, text="Chức danh:").grid(row=7, column=0)
        self.chucdanh = tk.Entry(root)
        self.chucdanh.grid(row=7, column=1)
        tk.Label(root, text="Nơi cấp:").grid(row=8, column=0)
        self.noicap = tk.Entry(root)
        self.noicap.grid(row=8, column=1)
        self.save = tk.Button(root, text="Lưu thông tin", command=self.save_info)
        self.save.grid(row=9, column=1)
        self.sinhnhat = tk.Button(root, text="Sinh nhật ngày hôm nay", command=self.sinhnhathomnay)
        self.sinhnhat.grid(row=10, column=0, columnspan=2)
        self.xuatdanhsach = tk.Button(root, text="Xuất toàn bộ danh sách", command=self.xuatfile)
        self.xuatdanhsach.grid(row=11, column=0, columnspan=2)
    def save_info(self):
        data = [
            self.ma.get(),
            self.ten.get(),
            self.ngaysinh.get(),
            self.gioitinh.get(),
            self.donvi.get(),
            self.cmnd.get(),
            self.ngaycap.get(),
            self.chucdanh.get(),
            self.noicap.get()
        ]

        self.quanlynhanvien.append(data)
        messagebox.showinfo("Thông báo", "Lưu thông tin thành công!")
    def sinhnhathomnay(self):
        today = datetime.datetime.today().strftime('%d/%m')
        today_birthdays = []
        for row in self.quanlynhanvien:
            if row[2][0:5] == today:  # Chỉ kiểm tra ngày và tháng
                today_birthdays.append(row)
        if today_birthdays:
            birthdays_str = "\n".join([f"Mã: {row[0]}, Tên: {row[1]}, Ngày sinh: {row[2]}" for row in today_birthdays])
            messagebox.showinfo("Sinh nhật hôm nay", birthdays_str)
        else:
            messagebox.showinfo("Sinh nhật hôm nay", "Không có nhân viên nào sinh nhật hôm nay")
    def xuatfile(self):
        sorted_data = sorted(self.quanlynhanvien, key=lambda x: datetime.datetime.strptime(x[2], '%d/%m/%Y'), reverse=True)
        with open('employee_list_sorted.txt', 'w') as file:
            for row in sorted_data:
                file.write(", ".join(row) + "\n")
        messagebox.showinfo("Xuất danh sách", "Xuất danh sách thành công!")
if __name__ == "__main__":
    root = tk.Tk()
    app = Quanlynhanvien(root)
    root.mainloop()
