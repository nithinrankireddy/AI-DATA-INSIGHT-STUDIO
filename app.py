import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")
# PAGE CONFIG 
st.set_page_config(page_title="AI Data Insight Studio", layout="wide")


# SIDEBAR 
st.sidebar.title("AI Data Insight Studio")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📂 Upload Data", "🧹 Data Cleaning", "📊 Dashboard", "💡 AI Insights", "🤖 AI Prediction"]
)

 
# HOME PAGE 
if page == "🏠 Home":

         
    st.markdown("""
    <style>
    .home-kpi-card {
        background: linear-gradient(145deg, #0f1c2e, #12243b);
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 8px 22px rgba(0,0,0,0.30);
        border: 1px solid rgba(255,255,255,0.04);
        transition: 0.3s ease-in-out;
    }

    .home-kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0px 14px 28px rgba(0,0,0,0.40);
    }

    .home-kpi-title {
        font-size: 18px;
        color: #cfd8dc;
        margin-bottom: 12px;
    }

    .home-kpi-value {
        font-size: 34px;
        font-weight: bold;
        color: white;
    }

    .step-card {
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.22);
        border: 1px solid rgba(255,255,255,0.04);
    }

    .feature-card {
        padding: 24px;
        border-radius: 18px;
        background: linear-gradient(145deg, #11233d, #152a44);
        box-shadow: 0px 8px 24px rgba(0,0,0,0.28);
        border: 1px solid rgba(255,255,255,0.04);
        transition: 0.3s ease-in-out;
        min-height: 140px;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0px 14px 28px rgba(0,0,0,0.38);
    }

    .feature-title {
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 12px;
    }

    .feature-text {
        font-size: 18px;
        color: #d0d7de;
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown("""
        <h1 style='text-align:center;
        font-size:52px;
        background: linear-gradient(90deg,#4facfe,#00f2fe);
        -webkit-background-clip: text;
        color: transparent;'>
        🧠 AI Data Insight Studio
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h4 style='text-align:center; color:#9aa0a6;'>
        AI-Driven Data Science Platform for Smart Analytics & Predictions
        </h4>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")


    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown("""
        <div class="home-kpi-card">
            <div class="home-kpi-title">⚡ Smart Analysis</div>
            <div class="home-kpi-value">Auto</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown("""
        <div class="home-kpi-card">
            <div class="home-kpi-title">🤖 AI Engine</div>
            <div class="home-kpi-value">Active</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown("""
        <div class="home-kpi-card">
            <div class="home-kpi-title">📊 Analytics</div>
            <div class="home-kpi-value">Live</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown("""
        <div class="home-kpi-card">
            <div class="home-kpi-title">💡 Insights</div>
            <div class="home-kpi-value">Enabled</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.divider()

    st.markdown("## How to Use AI Data Insight Studio")
    st.write("")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown("""
        <div class="step-card" style="background:rgba(34,197,94,0.18); color:#4ade80;">
            📂 Upload Data
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class="step-card" style="background:rgba(59,130,246,0.18); color:#60a5fa;">
            🧹 Data Cleaning
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown("""
        <div class="step-card" style="background:rgba(234,179,8,0.18); color:#facc15;">
            📊 Dashboard
        </div>
        """, unsafe_allow_html=True)

    with s4:
        st.markdown("""
        <div class="step-card" style="background:rgba(244,63,94,0.18); color:#fb7185;">
            💡 AI Insights
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")


    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📂 Smart Data Upload</div>
            <div class="feature-text">
                Upload CSV datasets instantly and prepare them for analysis.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🧹 Data Cleaning Studio</div>
            <div class="feature-text">
                Handle missing values, duplicates, and outliers with ease.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📊 Smart Analytics Dashboard</div>
            <div class="feature-text">
                Auto charts, KPIs, trends, and dashboard visualizations.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">💡 AI Insight Engine</div>
            <div class="feature-text">
                Generate meaningful insights and smart analysis from your dataset.
            </div>
        </div>
        """, unsafe_allow_html=True)


# UPLOAD PAGE
elif page == "📂 Upload Data":

    st.markdown("""
    <style>
    .upload-hero-box {
        background: linear-gradient(135deg, rgba(17,34,64,0.9), rgba(8,18,35,0.95));
        padding: 28px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.35);
        margin-bottom: 25px;
    }

    .upload-hero-title {
        font-size: 38px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
        text-align: center;
    }

    .upload-hero-sub {
        color: #aeb8c2;
        font-size: 17px;
        text-align: center;
    }

    .upload-kpi-card {
        background: linear-gradient(145deg, #0f1c2e, #12243b);
        padding: 28px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
        border: 1px solid rgba(255,255,255,0.04);
        transition: 0.3s ease-in-out;
    }

    .upload-kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0px 14px 28px rgba(0,0,0,0.45);
    }

    .upload-kpi-title{
        font-size:18px;
        color:#cfd8dc;
        margin-bottom:10px;
    }

    .upload-kpi-value{
        font-size:42px;
        font-weight:bold;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="upload-hero-box">
        <div class="upload-hero-title">📂 Upload Dataset</div>
        <div class="upload-hero-sub">
            Upload your CSV file and prepare it for smart analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload your CSV dataset",
        type=["csv"]
    )

    import pandas as pd

    # If user uploads a new file
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Store dataset in session memory
        st.session_state["data"] = df

        st.success("Dataset Uploaded Successfully ✅")

  
    if "data" in st.session_state:

        df = st.session_state["data"]

        st.write("")
        st.subheader("📊 Dataset Overview")
        st.write("")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="upload-kpi-card">
                <div class="upload-kpi-title">Rows</div>
                <div class="upload-kpi-value">{df.shape[0]}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="upload-kpi-card">
                <div class="upload-kpi-title">Columns</div>
                <div class="upload-kpi-value">{df.shape[1]}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="upload-kpi-card">
                <div class="upload-kpi-title">Missing Values</div>
                <div class="upload-kpi-value">{df.isnull().sum().sum()}</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # CENTER PREVIEW BUTTON
        c1, c2, c3 = st.columns([1,2,1])

        with c2:
            show_preview = st.button("Preview Dataset", use_container_width=True)

        if show_preview:
            st.subheader("Preview of Dataset")
            st.dataframe(df)


# CLEANING
elif page == "🧹 Data Cleaning":

    st.markdown("""
    <style>
    .clean-hero-box {
        background: linear-gradient(135deg, rgba(17,34,64,0.9), rgba(8,18,35,0.95));
        padding: 28px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.35);
        margin-bottom: 25px;
    }

    .clean-title {
        font-size: 38px;
        font-weight: 800;
        color: white;
        text-align: center;
        margin-bottom: 8px;
    }

    .clean-sub {
        text-align: center;
        color: #aeb8c2;
        font-size: 17px;
    }

    .clean-kpi-card {
        background: linear-gradient(145deg, #0f1c2e, #12243b);
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 8px 22px rgba(0,0,0,0.30);
        border: 1px solid rgba(255,255,255,0.04);
        transition: 0.3s ease-in-out;
    }

    .clean-kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0px 14px 28px rgba(0,0,0,0.40);
    }

    .clean-kpi-title {
        font-size: 16px;
        color: #cfd8dc;
        margin-bottom: 10px;
    }

    .clean-kpi-value {
        font-size: 32px;
        font-weight: bold;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div class="clean-hero-box">
        <div class="clean-title">🧹 Data Cleaning & Preprocessing</div>
        <div class="clean-sub">
            Clean, refine, and prepare your dataset for accurate analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "data" not in st.session_state:
        st.warning("⚠️ Please upload a dataset first.")
    else:
        import pandas as pd
        import numpy as np
        import plotly.express as px

        df = st.session_state["data"]

        
        st.subheader("🩺 Data Overview")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(f"""
            <div class="clean-kpi-card">
                <div class="clean-kpi-title">Rows</div>
                <div class="clean-kpi-value">{df.shape[0]}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="clean-kpi-card">
                <div class="clean-kpi-title">Columns</div>
                <div class="clean-kpi-value">{df.shape[1]}</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="clean-kpi-card">
                <div class="clean-kpi-title">Missing Values</div>
                <div class="clean-kpi-value">{df.isnull().sum().sum()}</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="clean-kpi-card">
                <div class="clean-kpi-title">Duplicate Rows</div>
                <div class="clean-kpi-value">{df.duplicated().sum()}</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")


        with st.expander("📑 Data Type Summary"):
            dtype_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
            st.dataframe(dtype_df)

      
        with st.expander("🔍 Missing Value Handling", expanded=True):

            missing_per_column = df.isnull().sum()
            missing_df = missing_per_column[missing_per_column > 0]

            if len(missing_df) == 0:
                st.success("No Missing Values Found 🎉")
            else:
                st.dataframe(missing_df)

                col_select = st.selectbox("Select Column to Handle", missing_df.index)

                numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

                if col_select in numeric_cols:
                    methods = ["Fill with Mean", "Fill with Median", "Fill with Mode", "Drop Column"]
                else:
                    methods = ["Fill with Mode", "Drop Column"]

                method = st.selectbox("Select Cleaning Method", methods)

                if st.button("Apply Cleaning"):

                    if method == "Fill with Mean":
                        df[col_select] = df[col_select].fillna(df[col_select].mean())

                    elif method == "Fill with Median":
                        df[col_select] = df[col_select].fillna(df[col_select].median())

                    elif method == "Fill with Mode":
                        df[col_select] = df[col_select].fillna(df[col_select].mode()[0])

                    elif method == "Drop Column":
                        df = df.drop(columns=[col_select])

                    st.session_state["data"] = df
                    st.success("Cleaning Applied Successfully ✅")
                    st.rerun()

       
        with st.expander("📑 Duplicate Handling"):

            duplicate_count = df.duplicated().sum()

            if duplicate_count == 0:
                st.success("No Duplicate Rows Found 🎉")
            else:
                st.write(f"Duplicate Rows: {duplicate_count}")

                if st.button("Remove Duplicates"):
                    df = df.drop_duplicates()
                    st.session_state["data"] = df
                    st.success("Duplicate Rows Removed ✅")
                    st.rerun()

    
        with st.expander("📊 Outlier Detection (Numeric Columns)"):

            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

            if len(numeric_cols) == 0:
                st.warning("No numeric columns available.")
            else:
                selected_numeric = st.selectbox("Select Numeric Column", numeric_cols)

               
                Q1 = df[selected_numeric].quantile(0.25)
                Q3 = df[selected_numeric].quantile(0.75)
                IQR = Q3 - Q1

                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR

               
                outliers = df[(df[selected_numeric] < lower) | (df[selected_numeric] > upper)]
                outlier_count = outliers.shape[0]

                
                fig = px.box(df, y=selected_numeric, title=f"Boxplot of {selected_numeric}")
                st.plotly_chart(fig, use_container_width=True)

                st.write(f"Lower Bound: {lower:.2f}")
                st.write(f"Upper Bound: {upper:.2f}")
                st.write(f"Outliers Detected: {outlier_count}")

                if outlier_count > 0:
                    if st.button("Remove Detected Outliers"):
                        df = df[(df[selected_numeric] >= lower) & (df[selected_numeric] <= upper)]
                        st.session_state["data"] = df
                        st.success(f"{outlier_count} outlier rows removed successfully ✅")
                        st.rerun()
                else:
                    st.info("No outliers detected in this column.")

#dashboard


elif page == "📊 Dashboard":

    import plotly.express as px
    import numpy as np

    if "data" not in st.session_state:
        st.warning("Please upload dataset first.")
        st.stop()

    df = st.session_state["data"]

    if "charts" not in st.session_state:
        st.session_state.charts = []

    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = False




    def detect_kpi_column(df):

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) == 0:
            return None

        priority_keywords = [
            "score","sales","revenue","amount",
            "profit","marks","price","income"
        ]

        for col in numeric_cols:
            for keyword in priority_keywords:
                if keyword in col.lower():
                    return col

        variances = df[numeric_cols].var()

        return variances.idxmax()




    if not st.session_state.dashboard_mode:

        st.markdown("""
        <style>
        .dash-hero-box {
            background: linear-gradient(135deg, rgba(17,34,64,0.9), rgba(8,18,35,0.95));
            padding: 28px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: 0px 10px 30px rgba(0,0,0,0.35);
            margin-bottom: 25px;
        }

        .dash-title {
            font-size: 42px;
            font-weight: 800;
            color: white;
            text-align: center;
            margin-bottom: 10px;
        }

        .dash-sub {
            text-align: center;
            color: #aeb8c2;
            font-size: 17px;
        }

        .dash-panel {
            background: rgba(15, 28, 46, 0.78);
            padding: 24px;
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.28);
            margin-top: 10px;
            margin-bottom: 18px;
        }

        .dash-panel-title {
            font-size: 28px;
            font-weight: 700;
            color: white;
            margin-bottom: 8px;
        }

        .dash-panel-sub {
            color: #aab2bd;
            font-size: 15px;
            margin-bottom: 18px;
        }

        .suggest-box {
            background: linear-gradient(145deg, #0f1c2e, #12243b);
            padding: 18px 22px;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.04);
            margin-bottom: 12px;
            color: white;
            font-size: 16px;
            box-shadow: 0px 8px 18px rgba(0,0,0,0.22);
        }
        </style>
        """, unsafe_allow_html=True)

        # HERO SECTION
        st.markdown("""
        <div class="dash-hero-box">
            <div class="dash-title">📊 Dashboard Builder</div>
            <div class="dash-sub">
                Build your own analytics dashboard with interactive charts and smart visual suggestions.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # BUILDER PANEL
        st.markdown("""
        <div class="dash-panel">
            <div class="dash-panel-title">🛠 Build Your Charts</div>
            <div class="dash-panel-sub">
                Select chart type and dataset columns to create your dashboard.
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        chart_type = col1.selectbox(
            "Chart Type",
            ["Histogram","Boxplot","Bar Chart","Pie Chart","Scatter Plot","Line Chart"]
        )

        x_column = col2.selectbox("X Column", df.columns)

        y_column = None

        if chart_type in ["Scatter Plot","Line Chart","Bar Chart"]:
            y_column = col3.selectbox("Y Column", df.columns)

        c1, c2, c3 = st.columns([1, 1.4, 1])

        with c2:
            if st.button("➕ Add Chart", use_container_width=True):
                st.session_state.charts.append({
                    "type": chart_type,
                    "x": x_column,
                    "y": y_column
                })
                st.rerun()

        st.write("")

        # CHARTS ADDED PANEL
        st.markdown("""
        <div class="dash-panel">
            <div class="dash-panel-title">📌 Charts Added</div>
            <div class="dash-panel-sub">
                Manage the charts you want to include in your dashboard.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if len(st.session_state.charts) == 0:
            st.info("No charts added yet. Add a chart to begin building your dashboard.")
        else:
            for i, chart in enumerate(st.session_state.charts):

                c1, c2 = st.columns([8, 1])

                with c1:
                    st.markdown(f"""
                    <div class="suggest-box">
                        <b>{i+1}. {chart['type']}</b> &nbsp;&nbsp;|&nbsp;&nbsp; 
                        X: <b>{chart['x']}</b> &nbsp;&nbsp;|&nbsp;&nbsp; 
                        Y: <b>{chart['y']}</b>
                    </div>
                    """, unsafe_allow_html=True)

                with c2:
                    if st.button("❌", key=f"del{i}"):
                        st.session_state.charts.pop(i)
                        st.rerun()

        c1, c2, c3 = st.columns([1, 1.5, 1])

        with c2:
            if st.button("🗑 Clear All Charts", use_container_width=True):
                st.session_state.charts = []
                st.rerun()

        st.divider()

                # SMART SUGGESTIONS PANEL
        #st.markdown("""
        #<div class="dash-panel">
        #   <div class="dash-panel-title">💡 Smart Chart Suggestions</div>
        #    <div class="dash-panel-sub">
        #       Based on your dataset, here are some recommended visualizations.
        #   </div>
        #</div>
        #""", unsafe_allow_html=True)

        numeric_cols = df.select_dtypes(include="number").columns
        categorical_cols = df.select_dtypes(exclude="number").columns

        suggestions = []

        if len(numeric_cols) >= 1:
            suggestions.append(f"Histogram of {numeric_cols[0]}")

        if len(categorical_cols) >= 1:
            suggestions.append(f"Pie Chart of {categorical_cols[0]}")

        if len(numeric_cols) >= 2:
            suggestions.append(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")

        with st.expander("📂 View Suggested Charts", expanded=False):
            if len(suggestions) == 0:
                st.info("No suggestions available for this dataset.")
            else:
                for s in suggestions:
                    st.markdown(f"""
                    <div class="suggest-box">📈 {s}</div>
                    """, unsafe_allow_html=True)

        st.write("")

        c1, c2, c3 = st.columns([1, 1.8, 1])

        with c2:
            if st.button("🚀 Generate Dashboard", use_container_width=True):
                st.session_state.dashboard_mode = True
                st.rerun()

    else:

        st.markdown("""
        <style>

        header {visibility:hidden;}
        footer {visibility:hidden;}
        section[data-testid="stSidebar"] {display:none;}

        .kpi-card {
            background-color:#0f1c2e;
            padding:25px;
            border-radius:12px;
            text-align:center;
            box-shadow:0px 6px 20px rgba(0,0,0,0.4);
        }

        .kpi-title{
            font-size:18px;
            color:#cfd8dc;
        }

        .kpi-value{
            font-size:36px;
            font-weight:bold;
        }

        </style>
        """,unsafe_allow_html=True)
#st.title("📊 Analytics Dashboard")
# ============================================
# FILTER BAR
# ============================================

        categorical_cols = df.select_dtypes(exclude="number").columns

        if len(categorical_cols)>0:

            st.subheader("Filters")

            filter_cols = st.columns(min(3,len(categorical_cols)))

            for i,col_name in enumerate(categorical_cols[:3]):

                with filter_cols[i]:

                    selected = st.selectbox(
                        col_name,
                        ["All"]+list(df[col_name].unique())
                    )

                    if selected!="All":
                        df=df[df[col_name]==selected]




        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols)>0:

            main_col = detect_kpi_column(df)

            total_rows = len(df)
            avg_val = round(df[main_col].mean(),2)
            max_val = df[main_col].max()
            std_val = round(df[main_col].std(),2)

            st.caption(f"Primary metric detected: {main_col}")

            k1,k2,k3,k4 = st.columns(4)

            with k1:
                st.markdown(f"""
                <div class="kpi-card">
                <div class="kpi-title">Total Records</div>
                <div class="kpi-value">{total_rows}</div>
                </div>
                """,unsafe_allow_html=True)

            with k2:
                st.markdown(f"""
                <div class="kpi-card">
                <div class="kpi-title">Average {main_col}</div>
                <div class="kpi-value">{avg_val}</div>
                </div>
                """,unsafe_allow_html=True)

            with k3:
                st.markdown(f"""
                <div class="kpi-card">
                <div class="kpi-title">Highest {main_col}</div>
                <div class="kpi-value">{max_val}</div>
                </div>
                """,unsafe_allow_html=True)

            with k4:
                st.markdown(f"""
                <div class="kpi-card">
                <div class="kpi-title">{main_col} Variability</div>
                <div class="kpi-value">{std_val}</div>
                </div>
                """,unsafe_allow_html=True)


        st.divider()



        charts = st.session_state.charts[:6]

        row1 = st.columns(2)
        row2 = st.columns(2)
        row3 = st.columns(2)

        grid=[row1,row2,row3]

        chart_index=0

        for row in grid:

            for col in row:

                if chart_index>=len(charts):
                    break

                chart=charts[chart_index]

                chart_title = f"{chart['type']} of {chart['x']}"

                with col:

                    if chart["type"]=="Pie Chart":

                        if chart["x"] in numeric_cols:

                            st.warning("Pie chart requires categorical data")

                        else:

                            fig = px.pie(
                                df,
                                names=chart["x"],
                                title=chart_title
                            )

                            fig.update_traces(
                                hovertemplate="%{label}<br>Count: %{value}<br>Percentage: %{percent}"
                            )


                    elif chart["type"]=="Histogram":

                        fig = px.histogram(
                            df,
                            x=chart["x"],
                            title=chart_title
                        )

                        fig.update_traces(
                            hovertemplate=f"{chart['x']}: %{{x}}<br>Count: %{{y}}"
                        )


                    elif chart["type"]=="Boxplot":

                        fig = px.box(
                            df,
                            y=chart["x"],
                            title=chart_title
                        )

                        fig.update_traces(
                            hovertemplate=f"{chart['x']}: %{{y}}"
                        )


                    elif chart["type"]=="Bar Chart":

                        fig = px.bar(
                            df,
                            x=chart["x"],
                            y=chart["y"],
                            title=chart_title
                        )

                        fig.update_traces(
                            hovertemplate=f"{chart['x']}: %{{x}}<br>{chart['y']}: %{{y}}"
                        )


                    elif chart["type"]=="Scatter Plot":

                        fig = px.scatter(
                            df,
                            x=chart["x"],
                            y=chart["y"],
                            title=chart_title
                        )

                        fig.update_traces(
                            hovertemplate=f"{chart['x']}: %{{x}}<br>{chart['y']}: %{{y}}"
                        )


                    elif chart["type"]=="Line Chart":

                        fig = px.line(
                            df,
                            x=chart["x"],
                            y=chart["y"],
                            title=chart_title
                        )

                        fig.update_traces(
                            hovertemplate=f"{chart['x']}: %{{x}}<br>{chart['y']}: %{{y}}"
                        )


                    fig.update_layout(
                        height=300,
                        transition_duration=400
                    )

                    st.plotly_chart(fig,use_container_width=True)

                chart_index+=1


        st.divider()

        if st.button("⬅ Back to Dashboard Builder"):

            st.session_state.dashboard_mode=False
            st.rerun()


# AI INSIGHTS PAGE 
# ============================================
# AI INSIGHTS PAGE (PREMIUM UI VERSION)
# ============================================

elif page == "💡 AI Insights":

    import numpy as np
    import pandas as pd

    if "data" not in st.session_state:
        st.warning("Please upload dataset first.")
        st.stop()

    df = st.session_state["data"]

    # --------------------------------------------
    # CHECK API KEY
    # --------------------------------------------
    if not os.getenv("GEMINI_API_KEY"):
        st.error("AI API Key not found. Please check your .env file.")
        st.stop()

    # --------------------------------------------
    # PREMIUM PAGE STYLE
    # --------------------------------------------
    st.markdown("""
    <style>
    .kpi-card {
        background: linear-gradient(145deg, #0f1c2e, #12243b);
        padding: 28px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
        border: 1px solid rgba(255,255,255,0.04);
        transition: 0.3s ease-in-out;
    }

    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0px 14px 28px rgba(0,0,0,0.45);
    }

    .kpi-title{
        font-size:18px;
        color:#cfd8dc;
        margin-bottom:10px;
    }

    .kpi-value{
        font-size:42px;
        font-weight:bold;
        color:white;
    }

    .hero-box {
        background: linear-gradient(135deg, rgba(17,34,64,0.9), rgba(8,18,35,0.95));
        padding: 28px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.35);
        margin-bottom: 25px;
    }
    .hero-title {
        font-size: 38px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
        text-align: center;
    }

    .hero-sub {
        color: #aeb8c2;
        font-size: 17px;
        text-align: center;
    }

    .panel-box {
        background: rgba(15, 28, 46, 0.78);
        padding: 24px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.28);
        margin-top: 10px;
        margin-bottom: 18px;
    }

    .panel-title {
        font-size: 30px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .panel-sub {
        color: #aab2bd;
        font-size: 15px;
        margin-bottom: 18px;
    }

    .result-box {
        background: linear-gradient(145deg, rgba(14,22,38,0.98), rgba(10,16,28,0.98));
        padding: 30px;
        border-radius: 20px;
        border-left: 5px solid #00c2ff;
        border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
        margin-top: 25px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 18px;
    }

    .mini-badge {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(0, 194, 255, 0.15);
        color: #7adfff;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 16px;
    }

    .divider-space {
        margin-top: 18px;
        margin-bottom: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

    # --------------------------------------------
    # HERO SECTION
    # --------------------------------------------
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">💡 AI Insights Studio</div>
        <div class="hero-sub">
            Generate smart, presentation-ready insights from your dataset using our AI engine.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------
    # DATASET OVERVIEW
    # --------------------------------------------
    rows, cols = df.shape
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=np.number).columns.tolist()

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
        <div class="kpi-title">Rows</div>
        <div class="kpi-value">{rows}</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
        <div class="kpi-title">Columns</div>
        <div class="kpi-value">{cols}</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
        <div class="kpi-title">Numeric Columns</div>
        <div class="kpi-value">{len(numeric_cols)}</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
        <div class="kpi-title">Categorical Columns</div>
        <div class="kpi-value">{len(categorical_cols)}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='divider-space'></div>", unsafe_allow_html=True)
    st.divider()

    # --------------------------------------------
    # SMALL DATASET PREVIEW FOR AI
    # --------------------------------------------
    preview_df = df.head(20).copy()
    dataset_preview = preview_df.to_csv(index=False)

    # --------------------------------------------
    # BASIC STAT SUMMARY
    # --------------------------------------------
    stats_text = ""

    try:
        if len(numeric_cols) > 0:
            stats_text = df[numeric_cols].describe().to_string()
        else:
            stats_text = "No numeric summary available."
    except:
        stats_text = "No numeric summary available."

    # --------------------------------------------
    # OPTIONAL: INCLUDE DASHBOARD CHART INFO
    # --------------------------------------------
    chart_info = "No dashboard charts selected."

    if "charts" in st.session_state and len(st.session_state["charts"]) > 0:
        chart_lines = []
        for i, ch in enumerate(st.session_state["charts"], start=1):
            chart_lines.append(
                f"{i}. {ch['type']} | X = {ch['x']} | Y = {ch['y']}"
            )
        chart_info = "\n".join(chart_lines)

    # --------------------------------------------
    # SESSION STATE FOR SAVED OUTPUT
    # --------------------------------------------
    if "ai_insights_output" not in st.session_state:
        st.session_state["ai_insights_output"] = None

    if "ai_insight_mode_selected" not in st.session_state:
        st.session_state["ai_insight_mode_selected"] = "Executive Summary"

    # --------------------------------------------
    # AI GENERATION PANEL
    # --------------------------------------------
    st.markdown("""
    <div class="panel-box">
        <div class="panel-title">🧠 Generate AI Insights</div>
        <div class="panel-sub">
            Choose the type of insight you want and let the AI engine analyze your dataset.
        </div>
    </div>
    """, unsafe_allow_html=True)

    insight_mode = st.selectbox(
        "Choose Insight Mode",
        [
            "Executive Summary",
            "Business Insights",
            "Data Patterns",
            "Chart-Based Insights",
            "Full AI Analysis"
        ],
        index=[
            "Executive Summary",
            "Business Insights",
            "Data Patterns",
            "Chart-Based Insights",
            "Full AI Analysis"
        ].index(st.session_state["ai_insight_mode_selected"])
    )

    st.session_state["ai_insight_mode_selected"] = insight_mode

    generate_btn = st.button("🚀 Generate AI Insights", use_container_width=True)

    # --------------------------------------------
    # GENERATE AI OUTPUT
    # --------------------------------------------
    if generate_btn:

        with st.spinner("Generating smart AI insights..."):

            try:

                if insight_mode == "Executive Summary":
                    mode_instruction = """
Generate ONLY a short executive summary.
Return exactly:
- 1 short heading
- 8 to 10 bullet points
- 1 final conclusion line

Keep it short, clear, and presentation-friendly.
"""

                elif insight_mode == "Business Insights":
                    mode_instruction = """
Generate ONLY business-style insights.
Return exactly:
- 1 short heading
- 8 to 10 bullet points
- Focus on decision-making, performance gaps, high/low performing segments, and improvement opportunities
- End with 1 recommendation line

Make it practical and useful.
"""

                elif insight_mode == "Data Patterns":
                    mode_instruction = """
Generate ONLY data pattern insights.
Return exactly:
- 1 short heading
- 8 to 10 bullet points
- Focus on trends, relationships, comparisons, distributions, and unusual patterns
- End with 1 key takeaway line

Do not write business recommendations here.
"""

                elif insight_mode == "Chart-Based Insights":
                    mode_instruction = """
Generate ONLY chart-based insights.
Return exactly:
- 1 short heading
- 8 to 10 bullet points
- Explain what the dashboard charts indicate
- Mention visible patterns, category dominance, spread, trend direction, or comparisons
- End with 1 chart conclusion line

Do not generate general dataset summary here.
"""

                else:
                    mode_instruction = """
Generate a complete professional AI analysis.
Return:
- Executive Summary
- Key Insights
- Important Patterns
- Segment Comparisons
- Risk / Anomaly Findings
- Final Conclusion

Keep it readable, structured, and professional.
"""

                prompt = f"""
You are an expert Data Analyst and AI Insight Generator.

Your job is to analyze the dataset and generate useful, realistic, professional insights.

STRICT RULES:
- Do NOT repeat raw column names unnecessarily.
- Do NOT produce very long paragraphs unless needed.
- Prefer short bullet points.
- Make the output natural, human-like, and presentation-ready.
- Focus only on what can reasonably be inferred from the data.
- If the dataset resembles student data, use educational analysis language.
- If the dataset resembles business/sales/customer data, use business analysis language.
- If unsure, remain general but useful.
- Do not mention technical backend or model provider.
- Avoid generic filler text.

MODE INSTRUCTION:
{mode_instruction}

DATASET SHAPE:
Rows: {rows}
Columns: {cols}

NUMERIC COLUMNS:
{numeric_cols}

CATEGORICAL COLUMNS:
{categorical_cols}

NUMERIC SUMMARY:
{stats_text}

DASHBOARD CHARTS SELECTED:
{chart_info}

DATASET SAMPLE (FIRST 20 ROWS):
{dataset_preview}

Now generate the output exactly according to the selected mode.
"""

                response = model.generate_content(prompt)
                ai_output = response.text

                st.session_state["ai_insights_output"] = ai_output

            except Exception as e:
                st.error(f"AI Engine Error: {e}")

    # --------------------------------------------
    # DISPLAY SAVED OUTPUT
    # --------------------------------------------
    if st.session_state["ai_insights_output"] is not None:

        st.success("AI Insights Generated Successfully ✅")

        st.markdown("""
        <div class="result-box">
            <div class="mini-badge">AI Generated Report</div>
            <div class="result-title">📘 Insight Output</div>
        """, unsafe_allow_html=True)

        st.markdown(st.session_state["ai_insights_output"])

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")

        col_a, col_b = st.columns([1, 1])

        with col_a:
            if st.button("🗑 Clear AI Insights", use_container_width=True):
                st.session_state["ai_insights_output"] = None
                st.rerun()

        with col_b:
            st.download_button(
                label="📥 Download Insights",
                data=st.session_state["ai_insights_output"],
                file_name="ai_insights.txt",
                mime="text/plain",
                use_container_width=True
            )


# AI PREDICTION PAGE 
elif page == "🤖 AI Prediction":
    st.title("🤖 AI Prediction")
    st.info("...........COMMING SOON...........")