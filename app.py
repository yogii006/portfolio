import streamlit as st
import json
import streamlit.components.v1 as components
st.markdown(
    """
    <style>
    /* Remove top padding added by Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem;
    }

    /* Reduce space before first element */
    .block-container > div:first-child {
        margin-top: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Yogesh Yadav | Portfolio",
    layout="wide"
)

# Load data
with open("data/experience.json") as f:
    experiences = json.load(f)

with open("data/projects.json") as f:
    projects = json.load(f)

# ---------------- HEADER ----------------
# 
import streamlit.components.v1 as components

components.html(
    """
   
        <h1 style="
            margin:20;
            font-size:34px;
            line-height:1.15;
        ">
            Yogesh Yadav
        </h1>

        <p style="
            margin:4px 0;
            font-size:20px;
            color:blue;
            font-weight:500;
        ">
            AI / Backend Engineer
        </p>

        <p style="
            margin:0;
            font-size:20px;
            color:green;
            max-width:800px;
        ">
            Building AI-native backend systems, LLM-powered platforms, and semantic data pipelines.
        </p>
    </div>
    """,
    height=140
)

# ---------------- 50–50 LAYOUT ----------------
left_col, right_col = st.columns([1, 1])

# ==================================================
# LEFT COLUMN — EXPERIENCE
# ==================================================
with left_col:
    st.header("Experience")

    for exp in experiences:
        components.html(
            f"""
            <div style="
                border-left:4px solid #000;
                padding:14px 16px;
                margin-bottom:18px;
                background:#fafafa;
                border-radius:10px;
            ">
                <h4 style="margin:0;">{exp['role']}</h4>
                <p style="margin:4px 0 6px 0; font-weight:500;">
                    {exp['company']}
                </p>
                <p style="margin:0; font-size:13px; color:#555;">
                    {exp['duration']} | {exp['location']}
                </p>
                <ul style="padding-left:18px; margin-top:8px;">
                    {''.join(f"<li>{point}</li>" for point in exp['points'])}
                </ul>
            </div>
            """,
            height=210
        )

# ==================================================
# RIGHT COLUMN — PROJECTS (FIXED HEIGHT CARDS)
# ==================================================
with right_col:
    st.header("Projects")

    project_cols = st.columns(2)

    for i, project in enumerate(projects):
        with project_cols[i % 2]:
            components.html(
                f"""
                <div style="
                    height:520px;                 /* 🔒 FIXED CARD HEIGHT */
                    border:1px solid #e5e7eb;
                    border-radius:14px;
                    padding:14px;
                    margin-bottom:20px;
                    box-shadow:0 4px 10px rgba(0,0,0,0.06);
                    background:#ffffff;
                    box-sizing:border-box;
                ">
                    <h4 style="margin-top:0;">{project['title']}</h4>

                    <p style="font-size:13px; color:#374151;">
                        {project['description']}
                    </p>

                    <p style="font-size:12px; margin-bottom:6px;">
                        <b>Tech:</b> {", ".join(project['tech'])}
                    </p>

                    <!-- Fixed-height video -->
                    <iframe
                        src="{project['demoVideo']}"
                        width="100%"
                        height="220"
                        style="border-radius:10px; border:none; margin:10px 0;"
                        allowfullscreen>
                    </iframe>

                    <!-- Buttons stay at bottom visually -->
                    <div style="display:flex; gap:8px; margin-top:10px;">
                        <a href="{project['liveUrl']}" target="_blank"
                           style="
                             flex:1;
                             text-align:center;
                             padding:7px;
                             background:#000;
                             color:#fff;
                             text-decoration:none;
                             border-radius:7px;
                             font-size:13px;
                           ">
                           🚀 Live
                        </a>

                        <a href="{project['githubUrl']}" target="_blank"
                           style="
                             flex:1;
                             text-align:center;
                             padding:7px;
                             border:1px solid #000;
                             color:#000;
                             text-decoration:none;
                             border-radius:7px;
                             font-size:13px;
                           ">
                           💻 GitHub
                        </a>
                    </div>
                </div>
                """,
                height=540   # must be >= card height
            )
