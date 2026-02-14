import streamlit as st

# 设置页面配置
st.set_page_config(page_title="CP3 English Coach", page_icon="🏀")

st.title("🏀 CP3 地道英语进阶练习器")
st.markdown("---")

# 1. 核心表达展示
st.header("💡 核心地道表达 (Core Expressions)")
expressions = {
    "Step away from": "主动离开/淡出 (比 retire 更得体)",
    "Engrained in the DNA of": "深深植根于...的基因中",
    "Span": "横跨/跨越 (及物动词，后不加 for)",
    "Not for the weak": "弱者不适合/心理素质差的人干不了",
    "Intentions were sincere": "出发点是真诚的/问心无愧"
}

for exp, meaning in expressions.items():
    with st.expander(f"📌 {exp}"):
        st.write(f"**含义：** {meaning}")
        if exp == "Span":
            st.code("Example: The career spanned 20 years.", language="text")

st.markdown("---")

# 2. 互动翻译练习
st.header("✍️ 翻译通关挑战")
q1 = st.text_input("题目：‘这项工程横跨了30年’ (注意 Span 的用法)")
if q1:
    if "span" in q1.lower() and "for" not in q1.lower():
        st.success("✅ 太棒了！你记住了 span 后面不加 for！")
        st.balloons()
    else:
        st.info("💡 提示：试试 'The project spanned 30 years.'")

# 3. 金句模仿秀
st.header("📝 职场退役文案生成器")
name = st.text_input("输入你的名字或职位", "高级外教")
years = st.number_input("从业年限", 1, 50, 10)

if st.button("生成我的地道宣言"):
    declaration = f"""
    This is it! After {years} years, I’m **stepping away from** my role as {name}. 
    The passion for excellence is **engrained in the DNA of** my work. 
    It’s been a **demanding** journey—certainly **not for the weak**—but my **intentions were always sincere**. 
    """
    st.code(declaration, language="text")

st.markdown("---")
st.caption("Keep pushing! 你离地道表达又近了一步。")
