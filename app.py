import streamlit as st
import base64


def home():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Sammy Moruri's Portfolio",
        page_icon="🧑‍💻",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile.jpg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Sammy's Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(
        f"""<div class="title">Hi! My name is <strong>Sammy Moruri</strong>👋</div>""",
        unsafe_allow_html=True,
    )

    # Profile image
    st.write(
        f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Sammy Moruri">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)

    # Subtitle
    st.write(
        f"""<div class="subtitle" style="text-align: center;">Machine Learning and Software Engineer</div>""",
        unsafe_allow_html=True,
    )

    # Social Icons
    social_icons = {
        # Platform: [URL, Icon]
        "LinkedIn": [
            "https://www.linkedin.com/in/sammy-moruri-483364247",
            "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        ],
        "GitHub": [
            "https://github.com/TheOneNyangweso",
            "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg",
        ],
        "Twitter": [
            "https://twitter.com/CrazySa_M",
            "https://cdn-icons-png.flaticon.com/512/733/733579.png",
        ],
    }

    social_icons_html = [
        f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons[platform][1]}'' alt='{platform}''></a>"
        for platform in social_icons
    ]

    st.write(
        f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""",
        unsafe_allow_html=True,
    )

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write(
        """
    - 🧑‍💻 I am a **ML and Software Engineer** currently working on a Customer Recommendation Project at Ramana with a team of 5 people.

    - ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Software Engineering, Computer Vision, Optimization, Automation**, and more!
    
    - 🤖
    
    - 📫 How to reach me: morurisammy5@gmail.com
    
    - 🏠 Nairobi
    """
    )

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my resume",
        data=pdf_bytes,
        file_name="Sammy's Resume.pdf",
        mime="application/pdf",
    )

    st.write("##")

    st.write(
        f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Comming soon...)</div>""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    home()
