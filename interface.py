import streamlit as st
from inferenceEngine import MovieEngine, MovieFact

# --- PAGE CONFIG ---
# Added the popcorn emoji as the browser tab icon
st.set_page_config(page_title="K2R - Movie Expert", page_icon="🍿", layout="wide")

# --- CUSTOM CSS FOR BRANDING & LAYOUT ---
st.markdown("""
    <style>
    /* Main Background: Netflix-style dark theme */
    .stApp {
        background-color: #141414;
        color: #E5E5E5;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #181818;
        border-right: 1px solid #333;
    }

    /* K2R Branding (Replaced Netflix Logo) */
    .k2r-logo {
        color: #E50914; /* Netflix Red */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 48px;
        font-weight: bold;
        letter-spacing: -1px;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Movie Card Styling with Hover Effect */
    .movie-card {
        background-color: #2f2f2f;
        padding: 20px;
        border-radius: 4px;
        transition: transform .2s;
        border-bottom: 3px solid #39D3C7; /* Your Mint Teal accent */
        margin-bottom: 20px;
    }
    
    .movie-card:hover {
        transform: scale(1.05);
        background-color: #333;
    }

    /* Red Action Button */
    .stButton>button {
        background-color: #E50914;
        color: white;
        border: none;
        font-weight: bold;
        width: 100%;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: REPLACED LOGO WITH K2R ---
st.sidebar.markdown('<div class="k2r-logo">K2R</div>', unsafe_allow_html=True)
st.sidebar.markdown("### Find a Movie")

# Criteria requested by Dr. R. BOUGHAREB: genre, type, duration, and year [cite: 8, 29]
u_genre = st.sidebar.selectbox("Genre", ["Action", "Drama", "Comedy", "History"])
u_type = st.sidebar.selectbox("Type", ["Feature Film", "Animated Film", "TV Movie", "Documentary"])
u_years = st.sidebar.slider("Release Year", 1990, 2026, (2000, 2024))
u_durs = st.sidebar.slider("Duration (min)", 60, 240, (90, 160))

# --- MAIN CONTENT AREA ---
st.title("🍿 K2R Movie Expert System")
st.write("University of Algiers 1 - L3 Information Systems")
st.divider()

# --- LOGIC EXECUTION ---
# The interface now directly shows the results based on sidebar interaction
engine = MovieEngine(u_durs[0], u_durs[1], u_years[0], u_years[1])
engine.reset()
engine.declare(MovieFact(genre=u_genre, film_type=u_type))
engine.run()

st.subheader(f"Recommended {u_genre} Titles")

if engine.results:
    # Displaying results in a grid format
    cols = st.columns(3)
    for idx, movie in enumerate(engine.results):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="movie-card">
                    <h3 style="color: white; margin-top:0;">{movie['title']}</h3>
                    <p style="color: #999;">{movie['year']} | {movie['duration']} min</p>
                    <span style="color: #46d369; font-weight:bold;">Match Found</span>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("No titles match these filters. Adjust the sliders to see more results.")

# --- TEAM MEMBERS (Required for Video) ---
st.sidebar.markdown("---")
st.sidebar.subheader("Team Members")
st.sidebar.text("Adoum Rym")
st.sidebar.text("Ait Abdeslam Kahina")
st.sidebar.text("Belmokhtar Romeissa")
