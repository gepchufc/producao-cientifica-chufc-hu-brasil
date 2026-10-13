"""Identidade visual compartilhada dos dashboards CH-UFC/HU Brasil."""
from __future__ import annotations

import streamlit as st
import plotly.graph_objects as go

VERDE = "#0D9488"
VERDE_ESCURO = "#0E615F"
AZUL = "#15334D"
AMBAR = "#E8A23D"
CINZA = "#64748B"


def aplicar_tema() -> None:
    """Aplica apenas CSS estático. Não usa recursos remotos."""
    st.markdown("""<style>
    :root {color-scheme:light}
    .stApp {background: #F3F6F8; color: #15334D; font-family: 'Segoe UI', Arial, sans-serif;}
    [data-testid="stHeader"] {background: transparent;}
    [data-testid="stAppViewContainer"] > .main {background: linear-gradient(145deg,#F3F6F8 0%,#ECF3F4 100%);}
    .main .block-container {max-width: 1420px; padding-top: 2.2rem; padding-bottom: 4rem;}
    [data-testid="stSidebar"] {background: #EAF2F3; border-right: 1px solid #DAE5E8;}
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {gap: 0.7rem;}
    [data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3 {color: #15334D;}
    [data-testid="stMetric"] {background: #FFFFFF; border:1px solid #E5EEF0; border-radius: 15px; padding: 1.15rem 1.2rem; box-shadow: 0 6px 22px rgba(24,62,75,0.075);}
    [data-testid="stMetricLabel"] {color:#617588; font-weight:650;}
    [data-testid="stMetricValue"] {color:#15334D; letter-spacing:-0.04em;}
    [data-testid="stTabs"] [data-baseweb="tab-list"] {gap:0.8rem; border-bottom:1px solid #DAE6E9;}
    [data-testid="stTabs"] button[role="tab"] {font-weight:600; padding:0.7rem 0.8rem; color:#506979;}
    [data-testid="stTabs"] button[aria-selected="true"] {color:#0D9488;}
    h1,h2,h3 {color:#15334D; letter-spacing:-0.025em;}
    [data-testid="stDataFrame"] {border: 1px solid #E3ECF0; border-radius: 12px; overflow: hidden;}
    [data-testid="stExpander"] {background:white; border:1px solid #E3ECF0; border-radius:12px;}
    [data-testid="stDownloadButton"] button {background: #F0FAF8; color:#0E615F; border-color:#C8E6E1; border-radius:11px;}
    [data-testid="stDownloadButton"] button:hover {border-color:#0D9488; color:#0E615F;}
    .chufc-hero {background: linear-gradient(120deg,#15334D 0%,#125C64 58%,#0D9488 100%);color:white;border-radius:18px;padding:1.65rem 2rem;margin-bottom:1.4rem;box-shadow:0 12px 30px rgba(17,66,81,0.15);}
    .chufc-hero .chufc-kicker {font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:#B9EFDF;font-weight:750;}
    .chufc-hero h1 {color:white;font-size:2rem;margin:0.25rem 0 0.45rem 0;padding:0;}
    .chufc-hero p {color:#D2E9EC;font-size:.94rem;margin:0;}
    .chufc-eyebrow {color:#0E615F;font-weight:700;letter-spacing:.07em;font-size:.75rem;text-transform:uppercase;}
    @media(max-width:780px){.main .block-container{padding:1rem}.chufc-hero{padding:1.3rem}.chufc-hero h1{font-size:1.45rem}}
    </style>""", unsafe_allow_html=True)


def cabecalho(subtitulo: str, etiqueta: str = "INTELIGÊNCIA BIBLIOMÉTRICA") -> None:
    # Valores fornecidos internamente pelo código; não há interpolação de texto do usuário.
    st.markdown(f"""<div class="chufc-hero"><div class="chufc-kicker">{etiqueta}</div>
    <h1>Produção Científica CH-UFC / HU Brasil</h1><p>{subtitulo}</p></div>""",unsafe_allow_html=True)


def layout_fig(fig: go.Figure, *, altura: int = 340) -> go.Figure:
    fig.update_layout(
        height=altura, paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
        font=dict(family="Segoe UI, Arial, sans-serif",color="#40556A",size=12),
        margin=dict(l=22,r=26,t=22,b=45), showlegend=True,
        legend=dict(orientation="h",y=-0.2,x=0),
        hoverlabel=dict(bgcolor="#15334D", font_color="#FFFFFF"),
        xaxis=dict(showgrid=False,zeroline=False,linecolor="#E0E9ED"),
        yaxis=dict(gridcolor="#EFF3F5",zeroline=False, tickformat=",d"),
    )
    return fig
