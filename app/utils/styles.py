"""Estilos e componentes visuais compartilhados pela aplicação."""

import html

import streamlit as st


def aplicar_estilos() -> None:
    """Aplica a identidade visual global utilizada em todas as páginas."""

    st.markdown(
        """
        <style>
        :root {
            --primary: #009E8E;
            --primary-dark: #007E73;
            --primary-soft: #EAF8F6;
            --navy: #0B1538;
            --text: #253252;
            --muted: #66728F;
            --bg: #F7F9FC;
            --surface: #FFFFFF;
            --surface-soft: #F9FBFD;
            --border: #E5EAF1;
            --border-strong: #D7DEE9;
            --info: #1976D2;
            --warning: #E79A18;
            --danger: #C94A4A;
            --shadow-sm: 0 2px 8px rgba(11, 21, 56, 0.05);
            --shadow-md: 0 8px 24px rgba(11, 21, 56, 0.07);
            --radius-sm: 10px;
            --radius-md: 14px;
            --radius-lg: 18px;
        }

        html,
        body,
        [class*="css"] {
            font-family:
                Inter,
                "Segoe UI",
                Roboto,
                Helvetica,
                Arial,
                sans-serif;
        }

        .stApp {
            background:
                radial-gradient(
                    circle at 48% 0%,
                    rgba(0, 158, 142, 0.035),
                    transparent 28rem
                ),
                var(--bg);
            color: var(--text);
        }

        .block-container {
            max-width: 1440px;
            padding-top: 1.35rem;
            padding-bottom: 3rem;
            padding-left: 1.6rem;
            padding-right: 1.6rem;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        [data-testid="stHeadingWithActionElements"] {
            color: var(--navy);
            letter-spacing: -0.025em;
        }

        h1 {
            font-weight: 760;
        }

        h2 {
            font-weight: 720;
        }

        h3 {
            font-weight: 680;
        }

        p,
        li,
        label,
        .stCaption {
            color: var(--text);
        }

        [data-testid="stCaptionContainer"] p,
        small {
            color: var(--muted);
        }

        hr {
            border-color: var(--border);
        }

        [data-testid="stHeader"] {
            background: rgba(247, 249, 252, 0.88);
            backdrop-filter: blur(10px);
        }

        [data-testid="stToolbar"] {
            right: 0.75rem;
        }

        [data-testid="stSidebar"] {
            background: var(--surface);
            border-right: 1px solid var(--border);
            box-shadow: 5px 0 18px rgba(11, 21, 56, 0.025);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 1.15rem;
        }

        [data-testid="stSidebar"] h3 {
            color: var(--navy);
            font-size: 1rem;
            font-weight: 750;
        }

        [data-testid="stSidebarNav"] {
            padding-top: 0.45rem;
        }

        [data-testid="stSidebarNav"] ul {
            gap: 0.28rem;
        }

        [data-testid="stSidebarNav"] a {
            min-height: 2.75rem;
            border-radius: 11px;
            color: var(--text);
            font-weight: 580;
            transition:
                background-color 150ms ease,
                color 150ms ease,
                transform 150ms ease;
        }

        [data-testid="stSidebarNav"] a:hover {
            background: #F0F7F6;
            color: var(--primary-dark);
            transform: translateX(2px);
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: var(--primary-soft);
            color: var(--primary-dark);
            font-weight: 700;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] svg {
            color: var(--primary);
        }

        [data-testid="stSidebar"] [data-testid="stAlert"] {
            box-shadow: none;
        }

        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 0.15rem 0.15rem 0.25rem 0.15rem;
        }

        .sidebar-brand-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 39px;
            width: 39px;
            height: 39px;
            border-radius: 11px;
            background:
                linear-gradient(
                    145deg,
                    var(--primary-dark),
                    var(--primary)
                );
            color: #FFFFFF;
            box-shadow: 0 5px 13px rgba(0, 158, 142, 0.18);
        }

        .sidebar-brand-name {
            color: var(--navy);
            font-size: 0.99rem;
            font-weight: 760;
            letter-spacing: -0.02em;
            line-height: 1.15;
        }

        .sidebar-brand-subtitle {
            margin-top: 3px;
            color: var(--muted);
            font-size: 0.71rem;
            font-weight: 550;
            line-height: 1.25;
        }

        [data-testid="stMetric"],
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetric"] {
            min-height: 118px;
            padding: 17px 18px;
            transition:
                border-color 160ms ease,
                box-shadow 160ms ease,
                transform 160ms ease;
        }

        [data-testid="stMetric"]:hover {
            border-color: #D6E8E5;
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted);
            font-size: 0.82rem;
            font-weight: 650;
        }

        [data-testid="stMetricValue"] {
            color: var(--navy);
            font-size: 1.65rem;
            font-weight: 760;
            letter-spacing: -0.035em;
        }

        [data-testid="stMetricDelta"] {
            color: var(--primary-dark);
            font-weight: 650;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            overflow: hidden;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] > div {
            padding: 0.15rem;
        }

        .hero {
            position: relative;
            overflow: hidden;
            min-height: 150px;
            padding: 30px 34px;
            margin-bottom: 22px;
            background:
                radial-gradient(
                    circle at 88% 18%,
                    rgba(0, 158, 142, 0.14),
                    transparent 12rem
                ),
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #FBFEFE 58%,
                    #F0FAF8 100%
                );
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-sm);
        }

        .hero::after {
            content: "";
            position: absolute;
            right: 38px;
            top: 30px;
            width: 112px;
            height: 112px;
            border-radius: 50%;
            background:
                radial-gradient(
                    circle,
                    rgba(0, 158, 142, 0.14) 0 2px,
                    transparent 3px
                ) 0 0 / 17px 17px;
            opacity: 0.55;
            pointer-events: none;
        }

        .hero h1 {
            position: relative;
            z-index: 1;
            max-width: 760px;
            margin: 0 0 10px 0;
            color: var(--navy);
            font-size: clamp(2rem, 3vw, 2.55rem);
            line-height: 1.12;
        }

        .hero p {
            position: relative;
            z-index: 1;
            max-width: 780px;
            margin: 0;
            color: var(--text);
            font-size: 1rem;
            line-height: 1.65;
        }

        .home-hero {
            position: relative;
            display: grid;
            grid-template-columns: minmax(0, 1.18fr) minmax(360px, 0.92fr);
            align-items: center;
            gap: 1.35rem;
            min-height: 380px;
            overflow: hidden;
            margin-bottom: 2.35rem;
            padding: 3.1rem 3.4rem;
            background:
                radial-gradient(
                    circle at 86% 22%,
                    rgba(0, 158, 142, 0.20),
                    transparent 19rem
                ),
                radial-gradient(
                    circle at 70% 105%,
                    rgba(25, 118, 210, 0.10),
                    transparent 20rem
                ),
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #FCFEFE 55%,
                    #EEF9F7 100%
                );
            border: 1px solid var(--border);
            border-radius: 22px;
            box-shadow: var(--shadow-sm);
        }

        .home-hero::before {
            content: "";
            position: absolute;
            left: -85px;
            bottom: -120px;
            width: 250px;
            height: 250px;
            border: 1px solid rgba(0, 158, 142, 0.08);
            border-radius: 50%;
            pointer-events: none;
        }

        .home-hero-content {
            position: relative;
            z-index: 2;
            max-width: 760px;
        }

        .home-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            margin-bottom: 1.2rem;
            padding: 7px 12px;
            background: rgba(234, 248, 246, 0.9);
            border: 1px solid #D8EFEC;
            border-radius: 999px;
            color: var(--primary-dark);
            font-size: 0.77rem;
            font-weight: 750;
            letter-spacing: 0.035em;
            text-transform: uppercase;
        }

        .home-eyebrow-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--primary);
            box-shadow: 0 0 0 4px rgba(0, 158, 142, 0.10);
        }

        .home-hero h1 {
            max-width: 760px;
            margin: 0 0 1.1rem 0;
            color: var(--navy);
            font-size: clamp(2.35rem, 4vw, 3.55rem);
            font-weight: 780;
            line-height: 1.06;
            letter-spacing: -0.048em;
        }

        .home-hero p {
            max-width: 690px;
            margin: 0;
            color: var(--text);
            font-size: 1.03rem;
            line-height: 1.7;
        }

        .home-hero-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 1.55rem;
        }

        .home-hero-tags span {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            min-height: 38px;
            padding: 9px 13px;
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid var(--border);
            border-radius: 10px;
            color: var(--navy);
            font-size: 0.77rem;
            font-weight: 630;
            backdrop-filter: blur(5px);
            transition:
                transform 180ms ease,
                border-color 180ms ease,
                background-color 180ms ease,
                box-shadow 180ms ease;
        }

        .home-hero-tags span:hover {
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.96);
            border-color: #CFE3E0;
            box-shadow: 0 8px 18px rgba(11, 21, 56, 0.07);
        }

        .home-hero-tags span:nth-child(1) svg {
            color: #12A995;
        }

        .home-hero-tags span:nth-child(2) svg {
            color: #1769E8;
        }

        .home-hero-tags span:nth-child(3) svg {
            color: #9650E6;
        }

        .home-hero-visual {
            position: relative;
            z-index: 1;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            min-height: 300px;
        }

        /* Imagem principal relacionada à saúde e obesidade */

        .hero-health-image-frame {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            width: 112%;
            min-height: 320px;
            margin-right: -3.25rem;
            overflow: visible;
            padding: 0;
            background:
                radial-gradient(
                    circle at 62% 48%,
                    rgba(255, 255, 255, 0.88),
                    rgba(225, 244, 241, 0.68) 54%,
                    transparent 78%
                );
            border-radius: 18px;
        }

        .hero-health-image-frame::before {
            content: "";
            position: absolute;
            inset: 9% 5%;
            z-index: 0;
            border-radius: 50%;
            background: rgba(130, 161, 235, 0.08);
            filter: blur(26px);
            pointer-events: none;
        }

        .hero-health-image {
            position: relative;
            z-index: 1;
            display: block;
            width: 118%;
            max-width: 760px;
            height: auto;
            object-fit: contain;
            mix-blend-mode: multiply;
            filter:
                saturate(0.88)
                contrast(0.98)
                brightness(1.02)
                drop-shadow(0 14px 28px rgba(25, 42, 70, 0.08));
            transition: transform 260ms ease;
        }

        .hero-health-image-frame:hover .hero-health-image {
            transform: translateY(-2px) scale(1.01);
        }

        .section-heading {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 2rem;
            margin: 0 0 1.2rem 0;
        }

        .section-heading h2 {
            margin: 0.25rem 0 0 0;
            font-size: clamp(1.45rem, 2vw, 1.9rem);
        }

        .section-heading p {
            max-width: 340px;
            margin: 0 0 0.15rem 0;
            color: var(--muted);
            font-size: 0.85rem;
            line-height: 1.5;
            text-align: right;
        }

        .section-kicker {
            color: var(--primary-dark);
            font-size: 0.73rem;
            font-weight: 760;
            letter-spacing: 0.075em;
            text-transform: uppercase;
        }

        .home-resources-heading {
            display: block;
            margin-bottom: 1.15rem;
        }

        .home-resources-heading p {
            max-width: none;
            margin-top: 0.35rem;
            color: var(--muted);
            font-size: 0.86rem;
            line-height: 1.5;
            text-align: left;
        }

        .project-card {
            position: relative;
            display: flex;
            align-items: flex-start;
            gap: 18px;
            height: 100%;
            min-height: 190px;
            padding: 22px 20px;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 14px;
            box-shadow: var(--shadow-sm);
            transition:
                transform 180ms ease,
                border-color 180ms ease,
                box-shadow 180ms ease;
        }

        .project-card::before {
            content: "";
            position: absolute;
            top: 0;
            right: 0;
            left: 0;
            height: 4px;
        }

        .project-card-dashboard::before {
            background: linear-gradient(90deg, #12A995, #69D3C4);
        }

        .project-card-prediction::before {
            background: linear-gradient(90deg, #1769E8, #6DA6F7);
        }

        .project-card-model::before {
            background: linear-gradient(90deg, #9650E6, #C18AF2);
        }

        .project-card:hover {
            transform: translateY(-4px);
            border-color: #C8DDDA;
            box-shadow: 0 16px 34px rgba(11, 21, 56, 0.11);
        }

        .project-card-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 82px;
            width: 82px;
            height: 82px;
            border-radius: 14px;
        }

        .project-card-icon svg {
            width: 34px;
            height: 34px;
        }

        .project-card-dashboard .project-card-icon {
            background: linear-gradient(145deg, #E8F8F5, #DDF4F0);
            color: #12A995;
        }

        .project-card-prediction .project-card-icon {
            background: linear-gradient(145deg, #EAF3FF, #DCEBFC);
            color: #1769E8;
        }

        .project-card-model .project-card-icon {
            background: linear-gradient(145deg, #F4EAFF, #EBDDFA);
            color: #9650E6;
        }

        .project-card-content {
            display: flex;
            flex: 1;
            flex-direction: column;
            min-width: 0;
            min-height: 142px;
        }

        .project-card-content h3 {
            margin: 0.2rem 0 0.65rem 0;
            color: var(--navy);
            font-size: 1.08rem;
            font-weight: 740;
            line-height: 1.25;
        }

        .project-card-content p {
            flex: 1;
            margin: 0;
            color: var(--text);
            font-size: 0.82rem;
            line-height: 1.65;
        }

        .project-card-link {
            display: flex;
            align-items: center;
            gap: 9px;
            margin-top: 1rem;
            color: var(--primary-dark);
            font-size: 0.78rem;
            font-weight: 730;
        }

        .project-card-link span {
            color: var(--primary);
            font-size: 1.05rem;
            transition: transform 180ms ease;
        }

        .project-card:hover .project-card-link span {
            transform: translateX(4px);
        }

        .home-section-spacer {
            height: 1.45rem;
        }

        .system-status-card {
            display: flex;
            align-items: center;
            gap: 20px;
            height: 100%;
            min-height: 205px;
            padding: 24px;
            background:
                radial-gradient(
                    circle at 15% 30%,
                    rgba(0, 190, 172, 0.15),
                    transparent 9rem
                ),
                linear-gradient(
                    135deg,
                    #0A2348,
                    #102D5D
                );
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            box-shadow: 0 12px 28px rgba(11, 21, 56, 0.15);
        }

        .system-status-illustration {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 82px;
            width: 82px;
            height: 82px;
            background: rgba(12, 187, 169, 0.14);
            border-radius: 50%;
        }

        .system-status-shield {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 57px;
            height: 57px;
            background: rgba(10, 185, 166, 0.18);
            border-radius: 17px;
            color: #3FD2C2;
        }

        .system-status-content {
            flex: 1;
            min-width: 0;
        }

        .system-status-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }

        .system-status-label {
            color: #60D4C7;
            font-size: 0.69rem;
            font-weight: 760;
            letter-spacing: 0.075em;
            text-transform: uppercase;
        }

        .system-status-indicator {
            flex: 0 0 9px;
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: #2AC6B5;
            box-shadow:
                0 0 0 5px rgba(42, 198, 181, 0.14),
                0 0 14px rgba(42, 198, 181, 0.52);
        }

        .system-status-card h3 {
            margin: 0.55rem 0 0.6rem 0;
            color: #FFFFFF;
            font-size: 1.15rem;
        }

        .system-status-card p {
            margin: 0;
            color: #D2DAE9;
            font-size: 0.82rem;
            line-height: 1.65;
        }

        .responsible-use-card {
            display: flex;
            align-items: flex-start;
            gap: 19px;
            height: 100%;
            min-height: 205px;
            padding: 26px 28px;
            background:
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #FBFEFE 100%
                );
            border: 1px solid var(--border);
            border-radius: 14px;
            box-shadow: var(--shadow-sm);
        }

        .responsible-use-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 50px;
            width: 50px;
            height: 50px;
            background: var(--primary-soft);
            border-radius: 14px;
            color: var(--primary-dark);
        }

        .responsible-use-content h3 {
            margin: 0.35rem 0 0.65rem 0;
            font-size: 1.12rem;
            font-size: 1.16rem;
        }

        .responsible-use-content p {
            margin: 0;
            color: var(--muted);
            font-size: 0.88rem;
            line-height: 1.7;
        }

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 1.1rem;
            border-bottom: 1px solid var(--border);
        }

        [data-testid="stTabs"] [data-baseweb="tab"] {
            height: 3rem;
            padding: 0 0.15rem;
            color: var(--muted);
            font-weight: 620;
        }

        [data-testid="stTabs"] [aria-selected="true"] {
            color: var(--primary-dark);
        }

        [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
            height: 2px;
            background-color: var(--primary);
        }

        .stButton > button,
        .stFormSubmitButton > button,
        .stDownloadButton > button {
            min-height: 2.8rem;
            border: 1px solid var(--border-strong);
            border-radius: 10px;
            font-weight: 700;
            transition:
                transform 150ms ease,
                box-shadow 150ms ease,
                border-color 150ms ease;
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover,
        .stDownloadButton > button:hover {
            border-color: var(--primary);
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(0, 158, 142, 0.12);
        }

        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            background:
                linear-gradient(
                    90deg,
                    var(--primary-dark),
                    var(--primary)
                );
            border-color: transparent;
            color: #FFFFFF;
        }

        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            background:
                linear-gradient(
                    90deg,
                    #007268,
                    #009E8E
                );
            color: #FFFFFF;
        }

        [data-baseweb="input"] > div,
        [data-baseweb="select"] > div,
        [data-baseweb="textarea"] > div {
            background: var(--surface);
            border-color: var(--border-strong);
            border-radius: 10px;
        }

        [data-baseweb="input"] > div:focus-within,
        [data-baseweb="select"] > div:focus-within,
        [data-baseweb="textarea"] > div:focus-within {
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(0, 158, 142, 0.10);
        }

        [data-testid="stNumberInput"] button {
            border-color: var(--border);
            color: var(--primary-dark);
        }

        [data-testid="stCheckbox"] svg,
        [data-testid="stRadio"] svg {
            color: var(--primary);
        }

        [data-testid="stAlert"] {
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stExpander"] {
            overflow: hidden;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stExpander"] summary {
            color: var(--navy);
            font-weight: 650;
        }

        [data-testid="stPlotlyChart"],
        [data-testid="stDataFrame"] {
            overflow: hidden;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        .insight {
            margin: 8px 0;
            padding: 14px 16px;
            background: var(--primary-soft);
            border: 1px solid #D5EFEB;
            border-left: 4px solid var(--primary);
            border-radius: 10px;
            color: var(--text);
        }

        .clinical-note {
            padding: 16px 18px;
            background: #F5F9FD;
            border: 1px solid #DCE9F4;
            border-left: 4px solid var(--info);
            border-radius: 12px;
            color: var(--text);
            line-height: 1.6;
        }

        .risk-low,
        .risk-medium,
        .risk-high {
            padding: 16px 18px;
            border-radius: 12px;
            line-height: 1.55;
        }

        .risk-low {
            background: var(--primary-soft);
            border: 1px solid #D5EFEB;
            border-left: 4px solid var(--primary);
        }

        .risk-medium {
            background: #FFF8EB;
            border: 1px solid #F3E1B9;
            border-left: 4px solid var(--warning);
        }

        .risk-high {
            background: #FFF2F2;
            border: 1px solid #F1D5D5;
            border-left: 4px solid var(--danger);
        }

        .bmi-card {
            display: flex;
            align-items: center;
            gap: 18px;
            width: 100%;
            min-height: 132px;
            box-sizing: border-box;
            margin: 0.45rem 0 1rem 0;
            padding: 20px 22px;
            background: var(--surface);
            border: 1px solid var(--border);
            border-left: 4px solid var(--bmi-accent);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        .bmi-card-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 52px;
            width: 52px;
            height: 52px;
            background: var(--bmi-soft);
            border-radius: 14px;
            color: var(--bmi-accent);
            font-size: 1.55rem;
        }

        .bmi-card-content {
            flex: 1;
            min-width: 0;
        }

        .bmi-card-label {
            margin-bottom: 4px;
            color: var(--muted);
            font-size: 0.78rem;
            font-weight: 750;
            letter-spacing: 0.055em;
            text-transform: uppercase;
        }

        .bmi-card-main {
            display: flex;
            align-items: baseline;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 4px;
        }

        .bmi-card-value {
            color: var(--navy);
            font-size: 2rem;
            font-weight: 780;
            line-height: 1.1;
            letter-spacing: -0.04em;
        }

        .bmi-card-unit {
            color: var(--muted);
            font-size: 0.92rem;
            font-weight: 600;
        }

        .bmi-card-classification {
            color: var(--bmi-accent);
            font-size: 1rem;
            font-weight: 720;
        }

        .bmi-card-note {
            margin-top: 7px;
            color: var(--muted);
            font-size: 0.82rem;
            line-height: 1.45;
        }

        .bmi-low {
            --bmi-accent: #4D7FA3;
            --bmi-soft: #EDF5FA;
        }

        .bmi-adequate {
            --bmi-accent: #009E8E;
            --bmi-soft: #EAF8F6;
        }

        .bmi-overweight {
            --bmi-accent: #C58A1F;
            --bmi-soft: #FFF7E7;
        }

        .bmi-obesity-one {
            --bmi-accent: #C56D32;
            --bmi-soft: #FFF1E8;
        }

        .bmi-obesity-two {
            --bmi-accent: #B95050;
            --bmi-soft: #FCEEEE;
        }

        .bmi-obesity-three {
            --bmi-accent: #934060;
            --bmi-soft: #F8EBF0;
        }

        .footer {
            margin-top: 1.8rem;
            padding-top: 1.35rem;
            border-top: 1px solid var(--border);
            color: var(--muted);
            text-align: center;
            font-size: 0.82rem;
        }

        @media (max-width: 1050px) {
            .home-hero {
                grid-template-columns: minmax(0, 1.12fr) minmax(330px, 0.88fr);
                padding: 2.65rem;
            }

            .home-hero h1 {
                font-size: clamp(2.15rem, 4vw, 3rem);
            }
        }

        @media (max-width: 900px) {
            .block-container {
                padding-right: 1rem;
                padding-left: 1rem;
            }

            .hero {
                min-height: auto;
                padding: 24px 22px;
            }

            .hero::after {
                display: none;
            }

            .home-hero {
                grid-template-columns: 1fr;
                gap: 1.5rem;
                padding: 2.35rem;
            }

            .home-hero-visual {
                min-height: 260px;
            }

            .section-heading {
                align-items: flex-start;
                flex-direction: column;
                gap: 0.35rem;
            }

            .section-heading p {
                max-width: none;
                text-align: left;
            }
        }

        @media (max-width: 700px) {
            .block-container {
                padding-top: 0.85rem;
            }

            .hero {
                border-radius: 15px;
            }

            .hero h1 {
                font-size: 1.8rem;
            }

            .hero p {
                font-size: 0.95rem;
            }

            .home-hero {
                min-height: auto;
                margin-bottom: 1.8rem;
                padding: 1.65rem 1.35rem;
                border-radius: 17px;
            }

            .home-hero h1 {
                font-size: 2rem;
                line-height: 1.1;
            }

            .home-hero p {
                font-size: 0.93rem;
            }

            .home-hero-tags {
                gap: 0.45rem;
            }

            .home-hero-visual {
                min-height: 245px;
            }

            .hero-health-image-frame {
                width: 100%;
                min-height: 235px;
                margin-right: 0;
                padding: 0;
                overflow: hidden;
            }

            .hero-health-image {
                width: min(108%, 560px);
            }

            .project-card {
                min-height: auto;
                padding: 19px;
            }

            .project-card-icon {
                flex-basis: 64px;
                width: 64px;
                height: 64px;
            }

            .project-card-content {
                min-height: 128px;
            }

            .system-status-card {
                align-items: flex-start;
                flex-direction: column;
            }

            .system-status-illustration {
                width: 68px;
                height: 68px;
                flex-basis: 68px;
            }

            .responsible-use-card {
                flex-direction: column;
                padding: 22px;
            }

            [data-testid="stMetric"] {
                min-height: 102px;
            }

            .bmi-card {
                align-items: flex-start;
                padding: 18px;
            }

            .bmi-card-value {
                font-size: 1.7rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(titulo: str, subtitulo: str) -> None:
    """Exibe o cabeçalho principal da página."""

    titulo_seguro = html.escape(titulo)
    subtitulo_seguro = html.escape(subtitulo)

    st.markdown(
        (
            '<div class="hero">'
            f"<h1>{titulo_seguro}</h1>"
            f"<p>{subtitulo_seguro}</p>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def card_imc(
    valor_imc: float,
    classificacao: str,
    classe_visual: str,
) -> None:
    """Exibe o resultado complementar do IMC em um card visual."""

    classificacao_segura = html.escape(classificacao)
    classe_visual_segura = html.escape(classe_visual)

    st.markdown(
        (
            f'<div class="bmi-card {classe_visual_segura}">'
            '<div class="bmi-card-icon" aria-hidden="true">⚖️</div>'
            '<div class="bmi-card-content">'
            '<div class="bmi-card-label">'
            "Índice de Massa Corporal"
            "</div>"
            '<div class="bmi-card-main">'
            f'<span class="bmi-card-value">{valor_imc:.2f}</span>'
            '<span class="bmi-card-unit">kg/m²</span>'
            "</div>"
            '<div class="bmi-card-classification">'
            f"{classificacao_segura}"
            "</div>"
            '<div class="bmi-card-note">'
            "Indicador complementar para adultos. "
            "O IMC não é enviado ao modelo e não substitui "
            "avaliação de um profissional de saúde."
            "</div>"
            "</div>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def placeholder_imc() -> None:
    """Exibe orientação enquanto peso e altura não foram informados."""

    st.info(
        "⚖️ **Preencha peso e altura para visualizar o IMC**\n\n"
        "O resultado será calculado automaticamente e servirá somente "
        "como informação complementar."
    )


def rodape() -> None:
    """Exibe o rodapé padrão da aplicação."""

    st.markdown(
        (
            '<div class="footer">'
            "Tech Challenge FIAP · Aplicação educacional de apoio analítico "
            "— não substitui avaliação clínica."
            "</div>"
        ),
        unsafe_allow_html=True,
    )