import streamlit as st
import pandas as pd
import uuid
import os

DATA_FILE = "memo_data.csv"

# 初期化
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["id", "title", "content", "x", "y", "color", "tag"])

st.title("🗂️ メモカード視覚化ツール")

# 入力フォーム
with st.form("new_memo"):
    title = st.text_input("タイトル")
    content = st.text_area("内容")
    color = st.color_picker("色", "#FFD700")
    tag = st.text_input("タグ")
    x = st.number_input("X座標", 0, 1000, step=10)
    y = st.number_input("Y座標", 0, 1000, step=10)
    submitted = st.form_submit_button("追加")
    if submitted:
        new_memo = {
            "id": str(uuid.uuid4()),
            "title": title,
            "content": content,
            "x": x,
            "y": y,
            "color": color,
            "tag": tag
        }
        df = pd.concat([df, pd.DataFrame([new_memo])], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("メモを追加しました。")
        st.experimental_rerun()

# カード表示
st.subheader("📌 メモ一覧（仮想配置）")
for _, row in df.iterrows():
    st.markdown(f"""
    <div style="
        position: relative;
        left: {row['x']}px;
        top: {row['y']}px;
        background-color: {row['color']};
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        width: 200px;
        box-shadow: 2px 2px 5px gray;
    ">
        <b>{row['title']}</b><br>
        <small>{row['tag']}</small><br>
        <p>{row['content']}</p>
    </div>
    """, unsafe_allow_html=True)
