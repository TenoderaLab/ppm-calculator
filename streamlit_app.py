import streamlit as st

st.set_page_config(page_title="農薬濃度計算", page_icon="🧮")

st.title("🧮 農薬 有効成分濃度 計算アプリ")

st.markdown("""
このツールは**実験用の計算補助**です。  
実際の使用量は必ず製品ラベル・公的基準に従ってください。  
結果の使用は自己責任でお願いします。
""")

# 入力UI
active = st.number_input("有効成分濃度 (%)", min_value=0.0, step=0.1)
volume_value = st.number_input("作りたい溶液量", min_value=0.0, step=0.1)

volume_unit = st.radio(
    "溶液量の単位",
    ["L", "mL"],
    horizontal=True
)

ppm = st.number_input("目標濃度 (ppm)", min_value=0.0, step=1.0)

# 単位変換
if volume_unit == "mL":
    volume_L = volume_value / 1000
else:
    volume_L = volume_value

# 計算
if st.button("計算する"):

    if active == 0:
        st.error("有効成分濃度が0%です")
    else:
        result_g = volume_L * ppm / (active * 10)
        result_mg = result_g * 1000

        st.success("✅ 計算結果")

        if result_g >= 1:
            st.write(f"必要量: **{result_g:.3f} g**")
        else:
            st.write(f"必要量: **{result_mg:.1f} mg**")

        # 両方表示
        st.caption(f"参考表示: {result_g:.4f} g / {result_mg:.1f} mg")