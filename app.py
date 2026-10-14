
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")

st.title("📚 QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm, xếp loại và thống kê kết quả học tập")

# 1. Tạo bảng dữ liệu 10 sinh viên
data = {
    "Họ tên": [
        "huynh", "ngan", "Minh", "khang", "Ha",
        "Hung", "tien", "long", "duy", "Kiet"
    ],
    "Chuyên cần": [9, 8, 10, 7, 9, 6, 8, 10, 7, 9],
    "Giữa kỳ": [8, 7, 9, 6, 8, 5, 7, 9, 6, 8],
    "Cuối kỳ": [9, 6, 10, 5, 8, 4, 6, 9, 5, 7]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df["Điểm tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# 3. Xếp loại học lực
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Điểm tổng kết"].apply(xep_loai)

# Hiển thị bảng điểm
st.subheader("1. Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# 4. Thống kê
st.subheader("2. Thống kê kết quả")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Điểm trung bình", round(df["Điểm tổng kết"].mean(), 2))
col2.metric("Điểm cao nhất", df["Điểm tổng kết"].max())
col3.metric("Điểm thấp nhất", df["Điểm tổng kết"].min())
col4.metric("Sinh viên đạt", int((df["Điểm tổng kết"] >= 5).sum()))

# 5. Biểu đồ
st.subheader("3. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ tên"], df["Điểm tổng kết"])
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_ylim(0, 10)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
