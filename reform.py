import streamlit as st

st.set_page_config(page_title="内装リフォーム概算くん", layout="wide")

st.title("🛠️ 内装リフォーム概算シミュレーター")
st.caption("物件案内中にその場で概算提示。顧客の『リフォームしたらいくら？』に即答します。")

# サイドバー：基本単価設定（会社の標準単価に合わせて変更可能）
with st.sidebar:
    st.header("⚙️ 単価マスタ設定")
    cloth_p = st.number_input("クロス単価(㎡)", value=1200)
    floor_p = st.number_input("フローリング単価(㎡)", value=9000)
    cleaning_p = st.number_input("クリーニング単価(㎡)", value=1000)

# メイン画面：入力セクション
col1, col2 = st.columns(2)

with col1:
    st.subheader("📏 施工面積・範囲")
    m2 = st.number_input("専有面積 (㎡)", min_value=0, value=60)
    cloth_area = st.number_input("クロス施工面積 (㎡) ※目安:専有面積×3.5", value=int(m2*3.5))
    floor_area = st.number_input("床施工面積 (㎡) ※目安:専有面積×0.7", value=int(m2*0.7))
    
with col2:
    st.subheader("🚿 設備交換")
    replace_kitchen = st.checkbox("システムキッチン (標準品)")
    replace_bath = st.checkbox("ユニットバス (標準品)")
    replace_toilet = st.checkbox("温水洗浄便座・便器交換")

# 計算ロジック
total_cloth = cloth_area * cloth_p
total_floor = floor_area * floor_p
total_cleaning = m2 * cleaning_p
total_equipment = (600000 if replace_kitchen else 0) + \
                  (800000 if replace_bath else 0) + \
                  (150000 if replace_toilet else 0)

grand_total = total_cloth + total_floor + total_cleaning + total_equipment

# 結果表示：視認性を高める
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("表層リフォーム合計", f"¥{total_cloth + total_floor + total_cleaning:,}")
c2.metric("設備交換合計", f"¥{total_equipment:,}")
c3.metric("総合計 (税込目安)", f"¥{grand_total:,}", delta="諸経費込")

# 詳細内訳
with st.expander("詳細内訳・条件を確認"):
    st.write(f"・壁紙張替 ({cloth_area}㎡): ¥{total_cloth:,}")
    st.write(f"・床張替 ({floor_area}㎡): ¥{total_floor:,}")
    st.write(f"・空室清掃 ({m2}㎡): ¥{total_cleaning:,}")
    if total_equipment > 0:
        st.write(f"・設備交換: ¥{total_equipment:,}")
    st.info("※解体・廃材処分費・養生費を含む概算です。正確な金額は現地調査が必要です。")