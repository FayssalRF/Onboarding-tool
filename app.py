# CS Onboarding Tool

## Projektstruktur (til README.md)
```
cs-onboarding-tool/
├── .streamlit/
│   └── config.toml
├── assets/
│   ├── logo.png
│   ├── bell.png
│   └── default_profile.png
├── app.py
└── requirements.txt
```

## .streamlit/config.toml
```toml
[server]
headless = true
port = $PORT
enableCORS = false

[theme]
primaryColor = "#3366FF"
backgroundColor = "#F4F6FC"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#111827"
font = "sans serif"
```

## requirements.txt
```
streamlit
Pillow
pandas
```

---

# app.py
```python
import streamlit as st
from PIL import Image
import pandas as pd
import os

# --- Streamlit page config ---
st.set_page_config(
    page_title="CS Onboarding Tool",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Load assets ---
ASSETS = os.path.join(os.path.dirname(__file__), "assets")
logo = Image.open(os.path.join(ASSETS, "logo.png"))
bell = Image.open(os.path.join(ASSETS, "bell.png"))
profile_img = Image.open(os.path.join(ASSETS, "default_profile.png"))

# --- Custom CSS styling ---
st.markdown(
    """
    <style>
    body { background-color: #F4F6FC; }
    .top-bar { display: flex; justify-content: space-between; align-items: center;
                padding: 1rem 2rem; background-color: #FFFFFF; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                position: sticky; top: 0; z-index: 100; }
    .profile-menu { position: relative; display: flex; align-items: center; cursor: pointer; }
    .profile-menu-content { display: none; position: absolute; right: 0; top: 48px;
        background-color: #FFFFFF; border-radius: 8px; box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        min-width: 160px; }
    .profile-menu:hover .profile-menu-content { display: block; }
    .profile-menu-content a { display: block; padding: 0.5rem 1rem; color: #111827; text-decoration: none; }
    .profile-menu-content a.logout { color: #DC2626; border-top: 1px solid #E5E7EB; }
    .card { background-color: #FFFFFF; border-radius: 12px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .kpi-value { font-size: 1.5rem; font-weight: 600; }
    .btn-primary { background-color: #3366FF; color: white; padding: 0.5rem 1rem; border-radius: 6px; border: none; cursor: pointer; }
    .btn-filter { background-color: #FFFFFF; border: 1px solid #D1D5DB; padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True
)

# --- Top Navigation Bar ---
st.markdown(
    f"<div class='top-bar'>"
    f"<div style='display:flex; align-items:center; gap:1rem;'>"
    f"<img src='data:image/png;base64,{st._to_bytes(logo)}' height='32'/><h2>Mover CS Onboarding Tracker</h2></div>"
    f"<div style='display:flex; align-items:center; gap:1rem;'>"
    f"<img src='data:image/png;base64,{st._to_bytes(bell)}' height='24'/><div class='profile-menu'>"
    f"<img src='data:image/png;base64,{st._to_bytes(profile_img)}' height='32' style='border-radius:50%;'/><span>John Doe (Admin)</span>"
    f"<div class='profile-menu-content'>"
    f"<a href='#'>My Profile</a>"
    f"<a href='#'>Settings</a>"
    f"<a href='#'>Manage accounts</a>"
    f"<a href='#' class='logout'>Logout</a>"
    f"</div></div></div></div>",
    unsafe_allow_html=True
)

# --- Header and Buttons ---
st.markdown("## Customer Onboarding Dashboard")
col1, col2 = st.columns([1,1], gap='small')
with col1:
    if st.button('+ New Customer'):
        st.info('+ New Customer clicked')
with col2:
    if st.button('Filter'):
        st.info('Filter clicked')

# --- KPI Cards ---
kpi_cols = st.columns(4, gap='large')
kpi_data = [
    {"title": "Active Onboardings", "value": "24", "sub": "This Month", "percent": "+12%"},
    {"title": "Expected Revenue", "value": "$124,500", "sub": "Realized: $78,200", "percent": None},
    {"title": "Avg. Bookings", "value": "42", "sub": "Target: 50", "percent": None},
    {"title": "Onboarding Time", "value": "23 days", "sub": "Target: 30 days", "percent": None},
]
for col, item in zip(kpi_cols, kpi_data):
    with col:
        st.markdown(
            f"<div class='card'><h4>{item['title']}</h4>"
            f"<div class='kpi-value'>{item['value']}</div>"
            f"<small>{item['sub']}</small>"
            f"{'<span style=\"float:right; color:#3366FF;\">'+item['percent']+'</span>' if item['percent'] else ''}"  # noqa
            f"</div>", unsafe_allow_html=True
        )

# --- Table & Next Actions ---
left, right = st.columns([3,1], gap='large')
with left:
    st.markdown("### Active Onboardings")
    df = pd.DataFrame([
        ["Acme Corp", "Day 12 of 30 (40%)", "$12,500/$25,000", 18, "On Track"],
        ["Global Logistics", "Day 8 of 30 (27%)", "$5,200/$15,000", 7, "Needs Attention"],
        ["Trans Continental", "Day 25 of 30 (83%)", "$42,000/$45,000", 38, "Ahead of Schedule"],
        ["Swift Shipping", "Day 15 of 30 (50%)", "$18,500/$30,000", 22, "Meeting Expectations"],
    ], columns=["Customer", "Progress", "Revenue", "Bookings", "Status"])
    st.table(df)
with right:
    st.markdown("### Next Actions <a href='#'>+ Add</a>", unsafe_allow_html=True)
    actions = [
        {"title": "Follow-up Meeting", "company": "Acme Corp", "time": "10:30 AM - 11:15 AM", "tag": "Today", "btn": "Start", "color": "#3366FF"},
        {"title": "First Quarter Review", "company": "Trans Continental", "time": "2:00 PM - 3:00 PM", "tag": "Tomorrow", "btn": "Prepare", "color": "#8B5CF6"},
        {"title": "Risk Assessment", "company": "Global Logistics", "time": "9:00 AM - 10:00 AM", "tag": "Fri, Jun 2", "btn": "Review", "color": "#FBBF24"},
        {"title": "Onboarding Completion", "company": "Swift Shipping", "time": "1:30 PM - 2:30 PM", "tag": "Mon, Jun 5", "btn": "Prepare", "color": "#10B981"},
    ]
    for act in actions:
        st.markdown(
            f"<div class='card' style='border-left:4px solid {act['color']}; margin-bottom:1rem;'>"
            f"<h5>{act['title']}</h5><small>{act['company']}</small><br>"
            f"<small>🕒 {act['time']} <span style='float:right; background:{act['color']}; color:white; padding:2px 6px; border-radius:4px;'>{act['tag']}</span></small><br><br>"
            f"<button class='btn-primary' style='background:{act['color']};'>{act['btn']}</button> "
            f"<button>Edit</button>"
            f"</div>", unsafe_allow_html=True
        )
```
