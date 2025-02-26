sogiolam = float(input("Nhập số giờ làm mỗi tuần"))
luonggio = float(input("Nhập thù lao trên số giờ làm tiêu chuẩn"))
giotieuchuan = 44
giovuotchuan =  max(0,sogiolam - giotieuchuan)
thuclinh = giotieuchuan * giovuotchuan * luonggio * 1.5
print(f"số tiền thực lĩnh của nhân viên: {thuclinh}")