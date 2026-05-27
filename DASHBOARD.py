import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="TN Election 2026 · AtliQ Media",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Prata&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    background-color: #0A0D13 !important;
    color: #E6EDF3;
}
.stApp { background-color: #0A0D13 !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3.5rem 5rem 3.5rem; max-width: 1500px; }

/* scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0A0D13; }
::-webkit-scrollbar-thumb { background: #21262D; border-radius: 3px; }

/* HERO */
.hero {
    background: radial-gradient(ellipse at 20% 50%, rgba(249,115,22,0.08) 0%, transparent 60%),
                linear-gradient(135deg, #12171F 0%, #0A0D13 100%);
    border: 1px solid #1E2530;
    border-radius: 20px;
    padding: 52px 60px;
    margin-bottom: 3rem;
}
.hero-eyebrow {
    font-family: 'Cinzel', serif;
    font-size: 10px; font-weight: 600; letter-spacing: 4px;
    color: #F97316; margin-bottom: 16px; text-transform: uppercase;
}
.hero-title {
    font-family: 'Cinzel', serif;
    font-size: 48px; font-weight: 900;
    color: #F0F6FC; line-height: 1.1;
    margin-bottom: 16px;
}
.hero-title .accent { color: #F97316; }
.hero-sub {
    font-family: 'Prata', serif;
    font-size: 18px; color: #8B949E;
    max-width: 580px; line-height: 1.7;
    margin-bottom: 24px;
}
.hero-pills { display: flex; gap: 12px; flex-wrap: wrap; }
.hero-pill {
    font-family: 'Cinzel', serif;
    font-size: 10px; font-weight: 600; letter-spacing: 2px;
    padding: 7px 18px; border-radius: 100px;
    border: 1px solid; text-transform: uppercase;
}
.pill-orange { color: #F97316; border-color: rgba(249,115,22,0.4); background: rgba(249,115,22,0.08); }
.pill-teal   { color: #14B8A6; border-color: rgba(20,184,166,0.4);  background: rgba(20,184,166,0.08); }
.pill-blue   { color: #3B82F6; border-color: rgba(59,130,246,0.4);  background: rgba(59,130,246,0.08); }

/* STORY HEADER */
.story-tag {
    font-family: 'Cinzel', serif;
    font-size: 10px; font-weight: 700; letter-spacing: 3px;
    padding: 5px 14px; border-radius: 100px; text-transform: uppercase;
    display: inline-block; margin-bottom: 14px;
}
.tag-orange { background: rgba(249,115,22,0.12); color: #F97316; border: 1px solid rgba(249,115,22,0.3); }
.tag-teal   { background: rgba(20,184,166,0.12);  color: #14B8A6; border: 1px solid rgba(20,184,166,0.3); }
.tag-blue   { background: rgba(59,130,246,0.12);  color: #3B82F6; border: 1px solid rgba(59,130,246,0.3); }

.story-title {
    font-family: 'Cinzel', serif;
    font-size: 30px; font-weight: 700; color: #F0F6FC;
    margin-bottom: 10px; line-height: 1.25;
}
.story-sub {
    font-family: 'Prata', serif;
    font-size: 15px; color: #6E7681;
    margin-bottom: 2rem; line-height: 1.7;
}

/* METRIC CARDS */
.metric-card {
    background: #12171F;
    border: 1px solid #1E2530;
    border-radius: 14px;
    padding: 26px 22px 22px 22px;
    position: relative; overflow: hidden;
    height: 130px;
}
.metric-card::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    border-radius: 14px 14px 0 0;
}
.mc-orange::before { background: linear-gradient(90deg, #F97316, #FB923C); }
.mc-blue::before   { background: linear-gradient(90deg, #3B82F6, #60A5FA); }
.mc-teal::before   { background: linear-gradient(90deg, #14B8A6, #2DD4BF); }
.mc-red::before    { background: linear-gradient(90deg, #EF4444, #F87171); }
.mc-green::before  { background: linear-gradient(90deg, #22C55E, #4ADE80); }
.mc-yellow::before { background: linear-gradient(90deg, #EAB308, #FDE047); }

.metric-big {
    font-family: 'Cinzel', serif;
    font-size: 36px; font-weight: 900; line-height: 1;
    margin-bottom: 8px;
}
.mc-orange .metric-big { color: #F97316; }
.mc-blue   .metric-big { color: #3B82F6; }
.mc-teal   .metric-big { color: #14B8A6; }
.mc-red    .metric-big { color: #EF4444; }
.mc-green  .metric-big { color: #22C55E; }
.mc-yellow .metric-big { color: #EAB308; }

.metric-label {
    font-family: 'Inter', sans-serif;
    font-size: 11.5px; color: #6E7681;
    font-weight: 500; line-height: 1.5;
}

/* FLIP BARS */
.flip-section {
    background: #12171F;
    border: 1px solid #1E2530;
    border-radius: 14px;
    padding: 28px 24px;
    height: 100%;
}
.flip-section-title {
    font-family: 'Cinzel', serif;
    font-size: 10px; font-weight: 600; letter-spacing: 3px;
    color: #444C56; text-transform: uppercase;
    margin-bottom: 20px;
}
.flip-item { margin-bottom: 16px; }
.flip-top {
    display: flex; justify-content: space-between;
    margin-bottom: 6px;
}
.flip-name {
    font-family: 'Inter', sans-serif;
    font-size: 13px; color: #8B949E; font-weight: 500;
}
.flip-num {
    font-family: 'Cinzel', serif;
    font-size: 13px; color: #F97316; font-weight: 700;
}
.flip-track {
    background: #1E2530; border-radius: 6px; height: 7px; overflow: hidden;
}
.flip-fill {
    height: 100%; border-radius: 6px;
    background: linear-gradient(90deg, #F97316 0%, #FB923C 100%);
    transition: width 0.6s ease;
}

/* DIVIDER */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #1E2530 20%, #1E2530 80%, transparent);
    margin: 3rem 0;
}

/* SECTION LABEL */
.section-label {
    font-family: 'Cinzel', serif;
    font-size: 9px; font-weight: 600; letter-spacing: 3px;
    color: #444C56; text-transform: uppercase;
    margin-bottom: 12px;
}

/* FOOTER */
.footer {
    text-align: center; padding: 3rem 0 1rem 0;
    font-family: 'Inter', sans-serif;
    font-size: 12px; color: #2D333B; line-height: 2.2;
}
</style>
""", unsafe_allow_html=True)

# ── Plotly theme ───────────────────────────────
BG    = "#0A0D13"
PANEL = "#12171F"
GRID  = "#1E2530"
MUTED = "#6E7681"
WHITE = "#F0F6FC"
PARTY_COLORS = {
    "TVK": "#F97316", "DMK": "#3B82F6", "AIADMK": "#6366F1",
    "INC": "#22C55E", "NTK": "#A855F7", "BJP":  "#EF4444", "PMK": "#EAB308",
}

def chart_style(fig, height=360):
    fig.update_layout(
        height=height,
        paper_bgcolor=PANEL, plot_bgcolor=PANEL,
        font=dict(family="Inter", color=MUTED, size=12),
        margin=dict(l=8, r=8, t=36, b=8),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED, size=11),
                    orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        xaxis=dict(gridcolor=GRID, zerolinecolor=GRID, tickfont=dict(color="#8B949E", family="Inter")),
        yaxis=dict(gridcolor=GRID, zerolinecolor=GRID, tickfont=dict(color=MUTED)),
    )
    fig.update_traces(marker_line_width=0)
    return fig

# ══════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">AtliQ Media · Codebasics RPC · ECI Data Only</div>
  <div class="hero-title">Decoding the <span class="accent">2026</span><br>Tamil Nadu Assembly Election</div>
  <div class="hero-sub">Three data stories. 234 constituencies. One fact-based show for AtliQ Media.</div>
  <div class="hero-pills">
    <span class="hero-pill pill-orange">01 · The Flip Story</span>
    <span class="hero-pill pill-teal">02 · The Vote Share Story</span>
    <span class="hero-pill pill-blue">03 · The Margin Story</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# STORY 01 — FLIP
# ══════════════════════════════════════════════
st.markdown('<div class="story-tag tag-orange">Story 01 · The Flip Story</div>', unsafe_allow_html=True)
st.markdown('<div class="story-title">163 of 234 seats changed hands.</div>', unsafe_allow_html=True)
st.markdown('<div class="story-sub">70% of Tamil Nadu\'s political map was redrawn in a single election.</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
for col, big, label, cls in zip(
    [c1, c2, c3, c4],
    ["163", "71", "70%", "65"],
    ["Constituencies flipped<br>2021 → 2026", "Constituencies held<br>by same party", "Of the map changed<br>in one election", "Biggest single flow<br>DMK → TVK"],
    ["mc-orange", "mc-blue", "mc-teal", "mc-yellow"]
):
    with col:
        st.markdown(f'<div class="metric-card {cls}"><div class="metric-big">{big}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns([1.15, 1])

with col_left:
    st.markdown('<div class="section-label">Seat count — 2021 vs 2026</div>', unsafe_allow_html=True)
    parties   = ["TVK", "DMK", "AIADMK", "INC", "BJP", "PMK"]
    seats_21  = [0, 133, 66, 18, 4, 5]
    seats_26  = [108, 59, 47, 5, 1, 4]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="2021", x=parties, y=seats_21,
        marker_color=[PARTY_COLORS.get(p) for p in parties], marker_opacity=0.25,
        text=seats_21, textposition="outside", textfont=dict(color=MUTED, size=11, family="Inter")))
    fig.add_trace(go.Bar(name="2026", x=parties, y=seats_26,
        marker_color=[PARTY_COLORS.get(p) for p in parties],
        text=seats_26, textposition="outside", textfont=dict(color=WHITE, size=12, family="Inter")))
    fig.update_layout(barmode="group", bargap=0.25, bargroupgap=0.06,
        yaxis=dict(range=[0,165], gridcolor=GRID, zerolinecolor=GRID, tickfont=dict(color=MUTED)),
        xaxis=dict(tickfont=dict(color=WHITE, size=13, family="Inter")))
    chart_style(fig, 360)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

with col_right:
    flips = [
        ("DMK → TVK", 65), ("AIADMK → TVK", 26), ("DMK → AIADMK", 22),
        ("AIADMK → DMK", 15), ("INC → TVK", 11), ("DMK → PMK", 3),
        ("BJP → DMK", 2), ("PMK → AIADMK", 2),
    ]
    items_html = "".join([
        f'<div class="flip-item">'
        f'<div class="flip-top"><span class="flip-name">{lbl}</span><span class="flip-num">{n} seats</span></div>'
        f'<div class="flip-track"><div class="flip-fill" style="width:{n/65*100:.1f}%"></div></div>'
        f'</div>'
        for lbl, n in flips
    ])
    st.markdown(f'<div class="flip-section"><div class="flip-section-title">Top flip flows</div>{items_html}</div>', unsafe_allow_html=True)

st.markdown('<p style="text-align:right;font-size:11px;color:#2D333B;margin-top:6px;">Source: ECI · tn_2021_results.csv & tn_2026_results.csv</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# STORY 02 — VOTE SHARE
# ══════════════════════════════════════════════
st.markdown('<div class="story-tag tag-teal">Story 02 · The Vote Share Story</div>', unsafe_allow_html=True)
st.markdown('<div class="story-title">TVK debuted at 34.9% — ahead of both DMK and AIADMK.</div>', unsafe_allow_html=True)
st.markdown('<div class="story-sub">A party that did not exist in 2021 became Tamil Nadu\'s single largest vote-getter.</div>', unsafe_allow_html=True)

c1,c2,c3,c4,c5 = st.columns(5)
for col, big, label, cls in zip(
    [c1,c2,c3,c4,c5],
    ["34.9%","24.2%","21.2%","−13.5pp","−12.1pp"],
    ["TVK vote share<br>2026 debut","DMK vote share<br>2026 (was 37.7%)","AIADMK vote share<br>2026 (was 33.3%)","DMK points lost<br>2021 → 2026","AIADMK points lost<br>2021 → 2026"],
    ["mc-orange","mc-blue","mc-teal","mc-red","mc-red"]
):
    with col:
        st.markdown(f'<div class="metric-card {cls}" style="height:120px"><div class="metric-big" style="font-size:28px">{big}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="section-label">Vote share by party — 2021 vs 2026</div>', unsafe_allow_html=True)
    parties = ["TVK","DMK","AIADMK","NTK","INC","BJP","PMK"]
    vs_21   = [0.0, 37.7, 33.3, 6.6, 4.3, 2.6, 3.8]
    vs_26   = [34.9, 24.2, 21.2, 4.0, 3.4, 3.0, 2.2]
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name="2021", x=parties, y=vs_21,
        marker_color=[PARTY_COLORS.get(p) for p in parties], marker_opacity=0.25,
        text=[f"{v}%" if v>0 else "" for v in vs_21], textposition="outside",
        textfont=dict(color=MUTED, size=10)))
    fig2.add_trace(go.Bar(name="2026", x=parties, y=vs_26,
        marker_color=[PARTY_COLORS.get(p) for p in parties],
        text=[f"{v}%" for v in vs_26], textposition="outside",
        textfont=dict(color=WHITE, size=10)))
    fig2.update_layout(barmode="group", bargap=0.25,
        yaxis=dict(range=[0,45], ticksuffix="%", gridcolor=GRID, zerolinecolor=GRID),
        xaxis=dict(tickfont=dict(color=WHITE, size=12, family="Inter")))
    chart_style(fig2, 360)
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

with col_right:
    st.markdown('<div class="section-label">Vote share vs seat share — 2026</div>', unsafe_allow_html=True)
    parties_cs = ["TVK","DMK","AIADMK","INC","BJP"]
    vote_sh    = [34.9, 24.2, 21.2, 3.4, 3.0]
    seat_sh    = [46.2, 25.2, 20.1, 2.1, 0.4]
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name="Vote %", x=parties_cs, y=vote_sh,
        marker_color="#14B8A6",
        text=[f"{v}%" for v in vote_sh], textposition="outside", textfont=dict(color=WHITE, size=10)))
    fig3.add_trace(go.Bar(name="Seat %", x=parties_cs, y=seat_sh,
        marker_color="#F97316",
        text=[f"{v}%" for v in seat_sh], textposition="outside", textfont=dict(color=WHITE, size=10)))
    fig3.update_layout(barmode="group", bargap=0.25,
        yaxis=dict(range=[0,58], ticksuffix="%", gridcolor=GRID, zerolinecolor=GRID),
        xaxis=dict(tickfont=dict(color=WHITE, size=12, family="Inter")))
    chart_style(fig3, 360)
    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

st.markdown('<p style="text-align:right;font-size:11px;color:#2D333B;margin-top:6px;">Source: ECI · All-constituency vote totals</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# REGIONAL BREAKDOWN
# ══════════════════════════════════════════════
st.markdown('<div class="story-tag tag-blue">Regional Breakdown</div>', unsafe_allow_html=True)
st.markdown('<div class="story-title">Every region flipped. Chennai Metro most completely.</div>', unsafe_allow_html=True)
st.markdown('<div class="story-sub">TVK swept Chennai with 29 seats. AIADMK resurged in North and Central.</div>', unsafe_allow_html=True)

regions = ["Chennai Metro","North","Central","Kongu","Delta","South"]
fig4 = go.Figure()
fig4.add_trace(go.Bar(name="DMK 2021", x=regions, y=[29,19,21,10,23,31],
    marker_color="#3B82F6", marker_opacity=0.2,
    text=[29,19,21,10,23,31], textposition="outside", textfont=dict(color=MUTED, size=10)))
fig4.add_trace(go.Bar(name="TVK 2026", x=regions, y=[29,15,12,16,10,26],
    marker_color="#F97316",
    text=[29,15,12,16,10,26], textposition="outside", textfont=dict(color=WHITE, size=10)))
fig4.add_trace(go.Bar(name="DMK 2026", x=regions, y=[2,4,8,9,14,22],
    marker_color="#3B82F6",
    text=[2,4,8,9,14,22], textposition="outside", textfont=dict(color=WHITE, size=10)))
fig4.add_trace(go.Bar(name="AIADMK 2026", x=regions, y=[1,15,15,7,4,5],
    marker_color="#6366F1",
    text=[1,15,15,7,4,5], textposition="outside", textfont=dict(color=WHITE, size=10)))
fig4.update_layout(barmode="group", bargap=0.2, bargroupgap=0.04,
    yaxis=dict(range=[0,42], gridcolor=GRID, zerolinecolor=GRID),
    xaxis=dict(tickfont=dict(color=WHITE, size=12, family="Inter")))
chart_style(fig4, 400)
st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# STORY 03 — MARGIN
# ══════════════════════════════════════════════
st.markdown('<div class="story-tag tag-blue">Story 03 · The Margin Story</div>', unsafe_allow_html=True)
st.markdown('<div class="story-title">Winning got harder. Average margin fell 26.6%.</div>', unsafe_allow_html=True)
st.markdown('<div class="story-sub">The election looked decisive on seats. The numbers tell a tighter story.</div>', unsafe_allow_html=True)

c1,c2,c3,c4,c5 = st.columns(5)
for col, big, label, cls in zip(
    [c1,c2,c3,c4,c5],
    ["22,871","16,784","−26.6%","64 seats","13 seats"],
    ["Avg winning margin<br>2021","Avg winning margin<br>2026","Drop in avg margin<br>2021 → 2026","Winner got < 35%<br>of valid votes","Winner got > 50%<br>of valid votes"],
    ["mc-blue","mc-orange","mc-red","mc-yellow","mc-green"]
):
    with col:
        st.markdown(f'<div class="metric-card {cls}" style="height:120px"><div class="metric-big" style="font-size:26px">{big}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="section-label">Avg margin by winning party — 2026</div>', unsafe_allow_html=True)
    m_parties = ["TVK","DMK","AIADMK","INC","PMK"]
    m_vals    = [18200, 19500, 12400, 14800, 11200]
    fig5 = go.Figure(go.Bar(
        x=m_parties, y=m_vals,
        marker_color=[PARTY_COLORS.get(p) for p in m_parties],
        text=[f"{v:,}" for v in m_vals], textposition="outside",
        textfont=dict(color=WHITE, size=11, family="Inter")))
    fig5.update_layout(showlegend=False,
        yaxis=dict(range=[0,24000], gridcolor=GRID, zerolinecolor=GRID),
        xaxis=dict(tickfont=dict(color=WHITE, size=13, family="Inter")))
    chart_style(fig5, 360)
    st.plotly_chart(fig5, use_container_width=True, config={"displayModeBar": False})

with col_right:
    st.markdown('<div class="section-label">Win percentage distribution — 2026 (234 seats)</div>', unsafe_allow_html=True)
    fig6 = go.Figure(go.Pie(
        labels=["< 35% of votes\n(Multi-cornered)", "35%–50%\n(Contested)", "> 50% of votes\n(Dominant)"],
        values=[64, 157, 13],
        marker=dict(colors=["#EAB308","#3B82F6","#22C55E"], line=dict(color=PANEL, width=3)),
        hole=0.58,
        textfont=dict(color=WHITE, size=11, family="Inter"),
        hovertemplate="%{label}: %{value} seats<extra></extra>",
    ))
    fig6.add_annotation(text="234<br>seats", x=0.5, y=0.5, showarrow=False,
        font=dict(size=18, color=WHITE, family="Cinzel"))
    fig6.update_layout(
        showlegend=True,
        legend=dict(orientation="v", x=0.72, y=0.5, font=dict(color=MUTED, size=11, family="Inter")),
        paper_bgcolor=PANEL, plot_bgcolor=PANEL,
        margin=dict(l=8, r=8, t=36, b=8), height=360,
    )
    st.plotly_chart(fig6, use_container_width=True, config={"displayModeBar": False})

st.markdown('<p style="text-align:right;font-size:11px;color:#2D333B;margin-top:6px;">Source: ECI · Constituency-level vote totals</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────
st.markdown("""
<div class="footer">
  Non-partisan analysis · Public ECI data only · No exit polls · No causal claims<br>
  Codebasics Resume Project Challenge · May 2026
</div>
""", unsafe_allow_html=True)
