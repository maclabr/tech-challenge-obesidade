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

        /* ======================================================
           MENU LATERAL
        ====================================================== */

        [data-testid="stSidebar"] {
            background:
                radial-gradient(
                    circle at 18% 0%,
                    rgba(0, 158, 142, 0.10),
                    transparent 13rem
                ),
                linear-gradient(
                    180deg,
                    #FFFFFF 0%,
                    #FBFDFD 58%,
                    #F7FAFC 100%
                );
            border-right: 1px solid #E1E8EE;
            box-shadow: 8px 0 28px rgba(11, 21, 56, 0.045);
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
            padding-top: 0.5rem;
        }

        [data-testid="stSidebarNav"]::before {
            content: "NAVEGAÇÃO";
            display: block;
            margin: 0.1rem 0.85rem 0.55rem;
            color: #8A94A8;
            font-size: 0.66rem;
            font-weight: 780;
            letter-spacing: 0.13em;
        }

        [data-testid="stSidebarNav"] ul {
            gap: 0.34rem;
        }

        [data-testid="stSidebarNav"] li {
            position: relative;
        }

        [data-testid="stSidebarNav"] a {
            position: relative;
            min-height: 2.85rem;
            padding: 0.55rem 0.75rem 0.55rem 2.75rem;
            border: 1px solid transparent;
            border-radius: 12px;
            color: var(--text);
            font-weight: 610;
            transition:
                background-color 150ms ease,
                border-color 150ms ease,
                color 150ms ease,
                box-shadow 150ms ease,
                transform 150ms ease;
        }

        [data-testid="stSidebarNav"] a::before {
            position: absolute;
            left: 0.72rem;
            top: 50%;
            width: 1.48rem;
            height: 1.48rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transform: translateY(-50%);
            border-radius: 8px;
            background: #F1F5F7;
            color: #53617A;
            font-size: 0.86rem;
            line-height: 1;
            transition:
                background-color 150ms ease,
                color 150ms ease,
                transform 150ms ease;
        }

        [data-testid="stSidebarNav"] li:nth-child(1) a::before {
            content: "⌂";
        }

        [data-testid="stSidebarNav"] li:nth-child(2) a::before {
            content: "◎";
        }

        [data-testid="stSidebarNav"] li:nth-child(3) a::before {
            content: "▥";
        }

        [data-testid="stSidebarNav"] li:nth-child(4) a::before {
            content: "✦";
        }

        [data-testid="stSidebarNav"] li:nth-child(5) a::before {
            content: "◈";
        }

        [data-testid="stSidebarNav"] li:nth-child(6) a::before {
            content: "♙";
        }

        [data-testid="stSidebarNav"] a:hover {
            background: rgba(255, 255, 255, 0.82);
            border-color: #DDE9E7;
            color: var(--primary-dark);
            box-shadow: 0 5px 14px rgba(11, 21, 56, 0.045);
            transform: translateX(2px);
        }

        [data-testid="stSidebarNav"] a:hover::before {
            background: var(--primary-soft);
            color: var(--primary-dark);
            transform: translateY(-50%) scale(1.03);
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background:
                linear-gradient(
                    90deg,
                    rgba(0, 158, 142, 0.14),
                    rgba(0, 158, 142, 0.07)
                );
            border-color: rgba(0, 158, 142, 0.18);
            color: var(--primary-dark);
            box-shadow: inset 3px 0 0 var(--primary);
            font-weight: 720;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"]::before {
            background: var(--primary);
            color: #FFFFFF;
            box-shadow: 0 4px 10px rgba(0, 158, 142, 0.22);
        }

        [data-testid="stSidebarNav"] a svg {
            display: none;
        }

        [data-testid="stSidebar"] [data-testid="stAlert"] {
            margin-top: 0.25rem;
            border: 1px solid #DCEBE8;
            border-radius: 13px;
            background: rgba(239, 249, 247, 0.88);
            box-shadow: none;
        }

        [data-testid="stSidebar"] [data-testid="stAlert"] p {
            color: #40516A;
            font-size: 0.79rem;
            line-height: 1.5;
        }

        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 0.2rem 0.15rem 0.35rem;
        }

        .sidebar-brand-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 43px;
            width: 43px;
            height: 43px;
            border-radius: 13px;
            background:
                linear-gradient(
                    145deg,
                    var(--primary-dark),
                    var(--primary)
                );
            color: #FFFFFF;
            box-shadow: 0 7px 17px rgba(0, 158, 142, 0.22);
        }

        .sidebar-brand-name {
            color: var(--navy);
            font-size: 1rem;
            font-weight: 780;
            letter-spacing: -0.025em;
            line-height: 1.12;
        }

        .sidebar-brand-subtitle {
            margin-top: 4px;
            color: var(--muted);
            font-size: 0.7rem;
            font-weight: 570;
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


        /* Cards de KPI do dashboard */
        .kpi-card {
            position: relative;
            display: flex;
            flex-direction: column;
            min-height: 156px;
            height: 100%;
            overflow: hidden;
            padding: 19px 18px 17px;
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            transition:
                transform 170ms ease,
                border-color 170ms ease,
                box-shadow 170ms ease;
        }

        .kpi-card::before {
            content: "";
            position: absolute;
            inset: 0 auto 0 0;
            width: 4px;
            background: var(--kpi-accent, var(--primary));
        }

        .kpi-card-blue {
            --kpi-accent: #1769E8;
        }

        .kpi-card-orange {
            --kpi-accent: #D9820B;
        }

        .kpi-card-purple {
            --kpi-accent: #8750C7;
        }

        .kpi-card-rose {
            --kpi-accent: #C94A64;
        }

        .kpi-card-green {
            --kpi-accent: #008F7F;
        }

        .kpi-card:hover {
            transform: translateY(-2px);
            border-color: #CFE3E0;
            box-shadow: var(--shadow-md);
        }

        .kpi-card-header {
            display: flex;
            align-items: center;
            gap: 9px;
            margin-bottom: 12px;
        }

        .kpi-card-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 38px;
            width: 38px;
            height: 38px;
            border: 1px solid transparent;
            border-radius: 11px;
            line-height: 1;
        }

        .kpi-card-icon svg {
            width: 20px;
            height: 20px;
            stroke: currentColor;
            stroke-width: 1.9;
            stroke-linecap: round;
            stroke-linejoin: round;
            fill: none;
        }

        .kpi-icon-blue {
            color: #1769E8;
            background: rgba(23, 105, 232, 0.10);
            border-color: rgba(23, 105, 232, 0.16);
        }

        .kpi-icon-orange {
            color: #D9820B;
            background: rgba(231, 154, 24, 0.12);
            border-color: rgba(231, 154, 24, 0.18);
        }

        .kpi-icon-purple {
            color: #8750C7;
            background: rgba(135, 80, 199, 0.11);
            border-color: rgba(135, 80, 199, 0.17);
        }

        .kpi-icon-rose {
            color: #C94A64;
            background: rgba(201, 74, 100, 0.10);
            border-color: rgba(201, 74, 100, 0.16);
        }

        .kpi-icon-green {
            color: #008F7F;
            background: rgba(0, 158, 142, 0.11);
            border-color: rgba(0, 158, 142, 0.17);
        }

        .kpi-card-title {
            color: var(--muted);
            font-size: 0.78rem;
            font-weight: 690;
            line-height: 1.25;
        }

        .kpi-card-value {
            margin: auto 0 5px;
            color: var(--navy);
            font-size: clamp(1.48rem, 2vw, 1.88rem);
            font-weight: 780;
            letter-spacing: -0.04em;
            line-height: 1.08;
        }

        .kpi-card-subtitle {
            color: var(--muted);
            font-size: 0.72rem;
            font-weight: 520;
            line-height: 1.35;
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

        /* Dashboard — gráficos e containers analíticos */

        [data-testid="stTabs"] {
            margin-top: 1.35rem;
        }

        [data-testid="stTabs"] [data-testid="stVerticalBlockBorderWrapper"] {
            height: 100%;
            padding: 0.35rem 0.45rem 0.15rem;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            box-shadow: var(--shadow-sm);
            transition: border-color 160ms ease, box-shadow 160ms ease;
        }

        [data-testid="stTabs"] [data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: #D5E7E4;
            box-shadow: var(--shadow-md);
        }

        [data-testid="stPlotlyChart"] {
            overflow: hidden;
            border-radius: 13px;
        }

        .dashboard-note {
            margin: 0.7rem 0 0.15rem;
            padding: 0.8rem 0.95rem;
            background: #F6FAFA;
            border: 1px solid #E2EFED;
            border-radius: 11px;
            color: var(--muted);
            font-size: 0.8rem;
            line-height: 1.55;
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


        /* Predição — estrutura em duas colunas */
        .prediction-info-card {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            margin: 0 0 1.35rem;
            padding: 16px 18px;
            background: #F4F8FD;
            border: 1px solid #DCE8F4;
            border-left: 4px solid #1769E8;
            border-radius: 13px;
            box-shadow: var(--shadow-sm);
        }

        .prediction-info-icon,
        .prediction-panel-icon,
        .prediction-placeholder-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 auto;
            border-radius: 11px;
        }

        .prediction-info-icon {
            width: 38px;
            height: 38px;
            background: rgba(23, 105, 232, 0.10);
            color: #1769E8;
        }

        .prediction-info-icon svg,
        .prediction-panel-icon svg,
        .prediction-placeholder-icon svg,
        .bmi-card-icon svg {
            width: 21px;
            height: 21px;
            fill: none;
            stroke: currentColor;
            stroke-width: 1.9;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .prediction-info-content strong {
            display: block;
            margin: 1px 0 4px;
            color: var(--navy);
            font-size: 0.88rem;
            font-weight: 760;
        }

        .prediction-info-content p {
            margin: 0;
            color: var(--muted);
            font-size: 0.82rem;
            line-height: 1.55;
        }

        .prediction-panel-heading {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 0 0 0.9rem;
        }

        .prediction-panel-icon {
            width: 40px;
            height: 40px;
            background: var(--primary-soft);
            color: var(--primary-dark);
        }

        .prediction-panel-heading h2 {
            margin: 0;
            color: var(--navy);
            font-size: 1.16rem;
            font-weight: 750;
            letter-spacing: -0.025em;
        }

        .prediction-panel-heading p {
            margin: 3px 0 0;
            color: var(--muted);
            font-size: 0.78rem;
            line-height: 1.4;
        }

        .prediction-side-title {
            margin: 1.25rem 0 0.4rem;
            color: var(--navy);
            font-size: 0.93rem;
            font-weight: 740;
        }

        .prediction-side-caption {
            margin: 0 0 0.75rem;
            color: var(--muted);
            font-size: 0.78rem;
            line-height: 1.5;
        }

        .prediction-placeholder-card {
            display: flex;
            align-items: flex-start;
            gap: 13px;
            min-height: 118px;
            margin-top: 0.55rem;
            padding: 17px;
            background: #FFFFFF;
            border: 1px dashed #CBD5E2;
            border-radius: 13px;
        }

        .prediction-placeholder-icon {
            width: 38px;
            height: 38px;
            background: #F0F3F8;
            color: #66728F;
        }

        .prediction-placeholder-card strong {
            display: block;
            margin: 2px 0 5px;
            color: var(--navy);
            font-size: 0.86rem;
        }

        .prediction-placeholder-card p {
            margin: 0;
            color: var(--muted);
            font-size: 0.78rem;
            line-height: 1.5;
        }

        .prediction-result-card {
            position: relative;
            overflow: hidden;
            margin-top: 0.65rem;
            padding: 20px;
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-left: 4px solid var(--result-accent, var(--primary));
            border-radius: 14px;
            box-shadow: var(--shadow-sm);
        }

        .prediction-result-card::after {
            content: "";
            position: absolute;
            top: -42px;
            right: -42px;
            width: 118px;
            height: 118px;
            background: var(--result-soft, var(--primary-soft));
            border-radius: 50%;
            opacity: 0.68;
        }

        .prediction-result-low {
            --result-accent: #009E8E;
            --result-soft: #EAF8F6;
        }

        .prediction-result-medium {
            --result-accent: #D9820B;
            --result-soft: #FFF7E7;
        }

        .prediction-result-high {
            --result-accent: #C94A4A;
            --result-soft: #FFF0F0;
        }

        .prediction-result-label {
            position: relative;
            z-index: 1;
            color: var(--muted);
            font-size: 0.72rem;
            font-weight: 760;
            letter-spacing: 0.07em;
            text-transform: uppercase;
        }

        .prediction-result-class {
            position: relative;
            z-index: 1;
            margin: 7px 0 13px;
            color: var(--navy);
            font-size: 1.38rem;
            font-weight: 790;
            line-height: 1.18;
            letter-spacing: -0.035em;
        }

        .prediction-result-grid {
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 9px;
        }

        .prediction-result-item {
            padding: 10px 11px;
            background: #F8FAFC;
            border: 1px solid #E8EDF3;
            border-radius: 10px;
        }

        .prediction-result-item span {
            display: block;
            color: var(--muted);
            font-size: 0.68rem;
            font-weight: 630;
        }

        .prediction-result-item strong {
            display: block;
            margin-top: 3px;
            color: var(--navy);
            font-size: 0.89rem;
            font-weight: 750;
        }

        .prediction-summary-card {
            margin-top: 0.7rem;
            padding: 15px 16px;
            background: #F8FAFC;
            border: 1px solid #E5EAF1;
            border-radius: 12px;
        }

        .prediction-summary-card strong {
            color: var(--navy);
            font-size: 0.79rem;
        }

        .prediction-summary-card p {
            margin: 7px 0 0;
            color: var(--muted);
            font-size: 0.76rem;
            line-height: 1.55;
        }

        @media (max-width: 900px) {
            .prediction-result-grid {
                grid-template-columns: 1fr;
            }
        }



        /* Predição — refinamento exclusivo do formulário em etapas */
        .form-step-tabs {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px;
            margin: 0.15rem 0 1rem;
        }

        .form-step-tab {
            display: flex;
            align-items: center;
            gap: 9px;
            min-height: 58px;
            padding: 9px 10px;
            color: var(--muted);
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 11px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .form-step-tab.is-active {
            color: var(--navy);
            border-color: color-mix(in srgb, var(--tab-accent) 38%, white);
            box-shadow: inset 0 -3px 0 var(--tab-accent), var(--shadow-sm);
        }

        .form-step-tab.is-complete {
            border-color: color-mix(in srgb, var(--tab-accent) 22%, white);
        }

        .form-step-icon,
        .form-section-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 auto;
            color: var(--tab-accent);
            background: color-mix(in srgb, var(--tab-accent) 11%, white);
            border-radius: 9px;
        }

        .form-step-icon {
            width: 31px;
            height: 31px;
        }

        .form-step-icon svg,
        .form-section-icon svg {
            width: 18px;
            height: 18px;
            fill: none;
            stroke: currentColor;
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .form-step-tab small,
        .form-step-tab strong {
            display: block;
        }

        .form-step-tab small {
            margin-bottom: 1px;
            color: var(--tab-accent);
            font-size: 0.61rem;
            font-weight: 750;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        .form-step-tab strong {
            font-size: 0.71rem;
            line-height: 1.2;
        }

        .form-section-heading {
            display: flex;
            align-items: center;
            gap: 11px;
            margin: 0.2rem 0 1rem;
            padding-bottom: 0.7rem;
            border-bottom: 1px solid var(--border);
        }

        .form-section-icon {
            width: 39px;
            height: 39px;
        }

        .form-section-heading span {
            color: var(--tab-accent);
            font-size: 0.67rem;
            font-weight: 760;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        .form-section-heading h3 {
            margin: 1px 0 0;
            color: var(--navy);
            font-size: 1.08rem;
            font-weight: 760;
        }

        div[data-testid="stButton"] > button[kind="primary"],
        div[data-testid="stButton"] > button[data-testid="stBaseButton-primary"] {
            color: #FFFFFF !important;
            font-weight: 750 !important;
        }

        div[data-testid="stButton"] > button[kind="primary"] p,
        div[data-testid="stButton"] > button[data-testid="stBaseButton-primary"] p {
            color: #FFFFFF !important;
            font-weight: 750 !important;
        }

        @media (max-width: 900px) {
            .form-step-tabs {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 520px) {
            .form-step-tabs {
                grid-template-columns: 1fr;
            }
        }

        

        /* Predição — apresentação do resultado (Fase 4.2) */
        .prediction-result-card {
            position: relative;
            overflow: hidden;
            margin-top: 0.65rem;
            padding: 22px 20px 19px;
            background: linear-gradient(145deg, #FFFFFF 0%, #FBFCFE 100%);
            border: 1px solid var(--border);
            border-left: 1px solid var(--border);
            border-radius: 15px;
            box-shadow: 0 10px 28px rgba(11, 21, 56, 0.08);
        }

        .prediction-result-card::after {
            top: -54px;
            right: -48px;
            width: 138px;
            height: 138px;
            opacity: 0.52;
        }

        .prediction-result-topbar {
            position: absolute;
            inset: 0 0 auto 0;
            height: 5px;
            background: linear-gradient(90deg, var(--result-accent), var(--result-accent-soft));
        }

        .prediction-result-healthy {
            --result-accent: #009E8E;
            --result-accent-soft: #69D3C4;
            --result-soft: #EAF8F6;
        }

        .prediction-result-underweight {
            --result-accent: #4B82D0;
            --result-accent-soft: #8FB5EA;
            --result-soft: #EDF5FF;
        }

        .prediction-result-overweight {
            --result-accent: #D39A15;
            --result-accent-soft: #F0C967;
            --result-soft: #FFF8E6;
        }

        .prediction-result-obesity-one {
            --result-accent: #E07A22;
            --result-accent-soft: #F1AA69;
            --result-soft: #FFF3E9;
        }

        .prediction-result-obesity-two {
            --result-accent: #C94A4A;
            --result-accent-soft: #E18484;
            --result-soft: #FFF0F0;
        }

        .prediction-result-obesity-three {
            --result-accent: #8750C7;
            --result-accent-soft: #B687E8;
            --result-soft: #F5EEFC;
        }

        .prediction-result-header {
            position: relative;
            z-index: 1;
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 14px;
            margin-bottom: 17px;
        }

        .prediction-result-check {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 34px;
            width: 34px;
            height: 34px;
            color: #FFFFFF;
            background: var(--result-accent);
            border-radius: 50%;
            font-size: 1rem;
            font-weight: 800;
            box-shadow: 0 6px 14px color-mix(in srgb, var(--result-accent) 25%, transparent);
        }

        .prediction-result-badge {
            display: inline-flex;
            align-items: center;
            max-width: 100%;
            margin-top: 8px;
            padding: 8px 12px;
            color: var(--result-accent);
            background: var(--result-soft);
            border: 1px solid color-mix(in srgb, var(--result-accent) 22%, white);
            border-radius: 999px;
            font-size: 1rem;
            font-weight: 780;
            line-height: 1.25;
        }

        .prediction-confidence-block {
            position: relative;
            z-index: 1;
            margin-bottom: 14px;
            padding: 13px 14px;
            background: #F8FAFC;
            border: 1px solid #E7ECF2;
            border-radius: 11px;
        }

        .prediction-confidence-heading {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 9px;
        }

        .prediction-confidence-heading span {
            color: var(--text);
            font-size: 0.76rem;
            font-weight: 680;
        }

        .prediction-confidence-heading strong {
            color: var(--result-accent);
            font-size: 1rem;
            font-weight: 800;
        }

        .prediction-confidence-track {
            width: 100%;
            height: 8px;
            overflow: hidden;
            background: #E6EBF1;
            border-radius: 999px;
        }

        .prediction-confidence-track span {
            display: block;
            height: 100%;
            background: linear-gradient(90deg, var(--result-accent), var(--result-accent-soft));
            border-radius: inherit;
        }

        .prediction-confidence-block small {
            display: block;
            margin-top: 7px;
            color: var(--muted);
            font-size: 0.68rem;
            font-weight: 600;
        }

        .prediction-result-grid {
            gap: 10px;
        }

        .prediction-result-item {
            min-height: 66px;
            padding: 11px 12px;
            background: #FFFFFF;
            border-color: #E5EAF1;
        }

        .prediction-summary-card {
            padding: 16px 17px;
            background: linear-gradient(135deg, #F8FAFC, #FFFFFF);
            border-left: 3px solid #AAB5C6;
        }

        .clinical-interpretation-card {
            display: flex;
            align-items: flex-start;
            gap: 15px;
            margin: 1rem 0 1.15rem;
            padding: 19px 20px;
            border-radius: 14px;
            box-shadow: var(--shadow-sm);
        }

        .clinical-interpretation-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 43px;
            width: 43px;
            height: 43px;
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid currentColor;
            border-radius: 12px;
        }

        .clinical-interpretation-icon svg {
            width: 22px;
            height: 22px;
            fill: none;
            stroke: currentColor;
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .clinical-interpretation-content {
            min-width: 0;
        }

        .clinical-interpretation-content > span {
            display: block;
            margin-bottom: 3px;
            color: inherit;
            font-size: 0.68rem;
            font-weight: 770;
            letter-spacing: 0.075em;
            text-transform: uppercase;
        }

        .clinical-interpretation-content h3 {
            margin: 0 0 7px;
            color: var(--navy);
            font-size: 0.98rem;
            font-weight: 750;
        }

        .clinical-interpretation-content p {
            margin: 0;
            color: var(--text);
            font-size: 0.82rem;
            line-height: 1.62;
        }

        .clinical-interpretation-card.risk-low {
            color: #007E73;
        }

        .clinical-interpretation-card.risk-medium {
            color: #B87508;
        }

        .clinical-interpretation-card.risk-high {
            color: #B83F3F;
        }


        /* Predição — fluxo vertical contínuo */
        .prediction-main-heading {
            margin-top: 0.2rem;
            margin-bottom: 1rem;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-color: #E2E8F0;
            border-radius: 15px;
            box-shadow: 0 5px 18px rgba(11, 21, 56, 0.045);
        }

        .prediction-flow-section {
            margin: -0.15rem 0 0.95rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid #E8EDF3;
        }

        .prediction-flow-heading {
            display: flex;
            align-items: center;
            gap: 11px;
        }

        .prediction-flow-number {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 29px;
            width: 29px;
            height: 29px;
            color: #FFFFFF;
            background: var(--section-accent);
            border-radius: 50%;
            font-size: 0.72rem;
            font-weight: 800;
        }

        .prediction-flow-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 38px;
            width: 38px;
            height: 38px;
            color: var(--section-accent);
            background: color-mix(in srgb, var(--section-accent) 11%, white);
            border-radius: 10px;
        }

        .prediction-flow-icon svg {
            width: 20px;
            height: 20px;
            fill: none;
            stroke: currentColor;
            stroke-width: 1.85;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .prediction-flow-heading h3 {
            margin: 0;
            color: var(--navy);
            font-size: 1rem;
            font-weight: 770;
        }

        .prediction-flow-heading p {
            margin: 3px 0 0;
            color: var(--muted);
            font-size: 0.76rem;
            line-height: 1.45;
        }

        .prediction-complement-note {
            margin-top: 0.65rem;
            padding: 12px 14px;
            background: #F4F8FD;
            border: 1px solid #DDE8F3;
            border-radius: 11px;
        }

        .prediction-complement-note strong {
            color: var(--navy);
            font-size: 0.76rem;
        }

        .prediction-complement-note p {
            margin: 5px 0 0;
            color: var(--muted);
            font-size: 0.73rem;
            line-height: 1.52;
        }

        .prediction-review-heading {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 1.25rem 0 0.45rem;
            text-align: center;
        }

        .prediction-review-heading strong {
            color: var(--navy);
            font-size: 0.92rem;
        }

        .prediction-review-heading span {
            margin-top: 3px;
            color: var(--muted);
            font-size: 0.76rem;
        }

        .prediction-result-divider {
            height: 1px;
            margin: 1.8rem 0 1.35rem;
            background: linear-gradient(90deg, transparent, #D7DFE9 16%, #D7DFE9 84%, transparent);
        }

        .prediction-result-heading {
            margin-bottom: 0.85rem;
        }

        .prediction-placeholder-wide {
            min-height: auto;
            margin-top: 0;
            padding: 19px 20px;
            background: #FBFCFE;
        }

        .prediction-summary-main {
            margin-top: 0.65rem;
            min-height: 146px;
        }

        @media (max-width: 760px) {
            .prediction-flow-heading {
                align-items: flex-start;
            }

            .prediction-flow-number {
                margin-top: 4px;
            }
        }

        @media (max-width: 640px) {
            .prediction-result-card {
                padding: 21px 16px 17px;
            }

            .prediction-result-badge {
                font-size: 0.9rem;
            }

            .clinical-interpretation-card {
                padding: 17px;
            }
        }
</style>
        """,
        unsafe_allow_html=True,
    )


def configurar_grafico(figura, altura: int = 430, legenda_horizontal: bool = False):
    """Padroniza gráficos Plotly com a identidade visual da aplicação."""

    layout_legenda = dict(
        title_text="",
        font=dict(size=12, color="#66728F"),
        bgcolor="rgba(0,0,0,0)",
    )
    if legenda_horizontal:
        layout_legenda.update(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
        )

    figura.update_layout(
        height=altura,
        margin=dict(l=18, r=18, t=62, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, Segoe UI, sans-serif", color="#253252", size=12),
        title=dict(
            x=0,
            xanchor="left",
            font=dict(size=17, color="#0B1538", family="Inter, Segoe UI, sans-serif"),
        ),
        legend=layout_legenda,
        hoverlabel=dict(
            bgcolor="#0B1538",
            bordercolor="#0B1538",
            font=dict(color="#FFFFFF", family="Inter, Segoe UI, sans-serif"),
        ),
    )
    figura.update_xaxes(
        showgrid=False,
        zeroline=False,
        linecolor="#E5EAF1",
        tickfont=dict(color="#66728F", size=11),
        title_font=dict(color="#66728F", size=12),
    )
    figura.update_yaxes(
        gridcolor="#EDF1F5",
        griddash="dot",
        zeroline=False,
        linecolor="#E5EAF1",
        tickfont=dict(color="#66728F", size=11),
        title_font=dict(color="#66728F", size=12),
    )
    return figura


def card_kpi(
    coluna,
    icone: str,
    cor: str,
    titulo: str,
    valor: str,
    subtitulo: str,
) -> None:
    """Exibe um indicador em um card visual reutilizável."""

    icones = {
        "pacientes": (
            '<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>'
            '<circle cx="9" cy="7" r="4"/>'
            '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/>'
            '<path d="M16 3.13a4 4 0 0 1 0 7.75"/>'
            '</svg>'
        ),
        "idade_media": (
            '<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="M3 3v18h18"/>'
            '<path d="m7 16 4-5 3 3 5-7"/>'
            '<path d="M19 7h-4"/>'
            '<path d="M19 7v4"/>'
            '</svg>'
        ),
        "idade_predominante": (
            '<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<circle cx="12" cy="12" r="9"/>'
            '<circle cx="12" cy="12" r="5"/>'
            '<circle cx="12" cy="12" r="1.5"/>'
            '</svg>'
        ),
        "historico_familiar": (
            '<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="M12 21s-7-4.35-9.33-8.28C.84 9.63 2.12 6 5.73 5.23 8 4.74 10 6 12 8c2-2 4-3.26 6.27-2.77 3.61.77 4.89 4.4 3.06 7.49C19 16.65 12 21 12 21Z"/>'
            '<path d="M8.5 12h2l1-2 1.5 4 1-2h2"/>'
            '</svg>'
        ),
        "transporte_ativo": (
            '<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<circle cx="12" cy="4" r="2"/>'
            '<path d="m10 22 1-7-3-3 2-4 4 3 3 1"/>'
            '<path d="m14 22-2-6"/>'
            '<path d="m6 22 2-6"/>'
            '</svg>'
        ),
    }
    cores_permitidas = {"blue", "orange", "purple", "rose", "green"}

    titulo_seguro = html.escape(str(titulo))
    valor_seguro = html.escape(str(valor))
    subtitulo_seguro = html.escape(str(subtitulo))
    icone_svg = icones.get(icone, icones["pacientes"])
    cor_segura = cor if cor in cores_permitidas else "green"

    coluna.markdown(
        (
            f'<div class="kpi-card kpi-card-{cor_segura}">'
            '<div class="kpi-card-header">'
            f'<span class="kpi-card-icon kpi-icon-{cor_segura}">{icone_svg}</span>'
            f'<span class="kpi-card-title">{titulo_seguro}</span>'
            '</div>'
            f'<div class="kpi-card-value">{valor_seguro}</div>'
            f'<div class="kpi-card-subtitle">{subtitulo_seguro}</div>'
            '</div>'
        ),
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
            '<div class="bmi-card-icon" aria-hidden="true">'
            '<svg viewBox="0 0 24 24">'
            '<path d="M5 20h14"/>'
            '<path d="M7 20 5.8 8.8A3 3 0 0 1 8.8 5.5h6.4a3 3 0 0 1 3 3.3L17 20"/>'
            '<path d="M9 10a3 3 0 0 1 6 0"/>'
            '<path d="m12 10 1.6-1.4"/>'
            '</svg></div>'
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

    st.markdown(
        (
            '<div class="prediction-placeholder-card">'
            '<span class="prediction-placeholder-icon" aria-hidden="true">'
            '<svg viewBox="0 0 24 24">'
            '<path d="M5 20h14"/>'
            '<path d="M7 20 5.8 8.8A3 3 0 0 1 8.8 5.5h6.4a3 3 0 0 1 3 3.3L17 20"/>'
            '<path d="M9 10a3 3 0 0 1 6 0"/>'
            '</svg>'
            '</span>'
            '<div><strong>IMC aguardando dados</strong>'
            '<p>Preencha peso e altura para visualizar automaticamente o indicador complementar.</p>'
            '</div></div>'
        ),
        unsafe_allow_html=True,
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