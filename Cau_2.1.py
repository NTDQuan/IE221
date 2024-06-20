import streamlit as st

def main():
    st.title("Máy tính đơn giản")
    num1 = st.number_input("Số thứ nhất", value=0.0)
    num2 = st.number_input("Số thứ hai", value=0.0)
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    st.write(f"Tổng: {sum}")
    st.write(f"Hiệu: {difference}")
    st.write(f"Tích: {product}")
    st.write(f"Thương: {quotient}")

if __name__ == "__main__":
    main()