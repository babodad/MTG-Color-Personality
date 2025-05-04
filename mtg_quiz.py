import streamlit as st

st.set_page_config(page_title="MTG Persönlichkeits-Test", layout="centered")
st.title("MTG Color Identity – Persönlichkeitstest")

questions = [
    {
        "text": "Wie gehst du mit Herausforderungen um?",
        "options": [
            ("Ich analysiere die Situation und plane strategisch.", ["U"]),
            ("Ich handle impulsiv und vertraue meinem Instinkt.", ["R"]),
            ("Ich suche nach einem Kompromiss und strebe Harmonie an.", ["G"]),
            ("Ich gehe über Grenzen, um mein Ziel zu erreichen.", ["B"]),
            ("Ich folge Regeln, um Stabilität zu wahren.", ["W"])
        ]
    },
    {
        "text": "Was ist dir in einer Gemeinschaft am wichtigsten?",
        "options": [
            ("Ordnung und Regeln, die für alle gelten.", ["W"]),
            ("Freiheit und individuelle Entfaltung.", ["R"]),
            ("Wissen und kontinuierliches Lernen.", ["U"]),
            ("Gleichgewicht mit der Umwelt.", ["G"]),
            ("Souveränität und Selbstbestimmung.", ["B"])
        ]
    },
    {
        "text": "Was beschreibt dich am besten?",
        "options": [
            ("Diszipliniert und moralisch.", ["W"]),
            ("Neugierig und berechnend.", ["U"]),
            ("Machtbewusst und zielorientiert.", ["B"]),
            ("Emotional und leidenschaftlich.", ["R"]),
            ("Naturverbunden und instinktiv.", ["G"])
        ]
    },
    {
        "text": "Wie triffst du Entscheidungen?",
        "options": [
            ("Basierend auf Logik und Fakten.", ["U"]),
            ("Nach meinen moralischen Überzeugungen.", ["W"]),
            ("Durch Abwägung von Nutzen und Kosten.", ["B"]),
            ("Intuitiv und schnell.", ["R"]),
            ("Durch das, was sich richtig anfühlt.", ["G"])
        ]
    },
    {
        "text": "Welcher dieser Begriffe spricht dich am meisten an?",
        "options": [
            ("Ordnung", ["W"]),
            ("Wissen", ["U"]),
            ("Macht", ["B"]),
            ("Freiheit", ["R"]),
            ("Harmonie", ["G"])
        ]
    }
]

color_labels = {
    "W": "Weiß – Ordnung & Moral",
    "U": "Blau – Wissen & Kontrolle",
    "B": "Schwarz – Macht & Opportunismus",
    "R": "Rot – Freiheit & Emotion",
    "G": "Grün – Natur & Wachstum"
}

combinations = {
    "Azorius (W/U)": ["W", "U"],
    "Dimir (U/B)": ["U", "B"],
    "Rakdos (B/R)": ["B", "R"],
    "Gruul (R/G)": ["R", "G"],
    "Selesnya (G/W)": ["G", "W"],
    "Esper (W/U/B)": ["W", "U", "B"],
    "Jund (B/R/G)": ["B", "R", "G"],
    "Temur (U/R/G)": ["U", "R", "G"],
    "Abzan (W/B/G)": ["W", "B", "G"],
    "Jeskai (W/U/R)": ["W", "U", "R"]
}

if "answers" not in st.session_state:
    st.session_state.answers = []

if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.subheader(f"Frage {st.session_state.step + 1} von {len(questions)}")
    st.write(q["text"])
    for i, (text, colors) in enumerate(q["options"]):
        if st.button(text, key=f"btn-{st.session_state.step}-{i}"):
            st.session_state.answers.append(colors)
            st.session_state.step += 1
            st.experimental_rerun()
else:
    score = {"W": 0, "U": 0, "B": 0, "R": 0, "G": 0}
    for answer in st.session_state.answers:
        for c in answer:
            score[c] += 1

    max_score = max(score.values())
    best = [c for c in score if score[c] == max_score]

    st.success("Deine dominante MTG-Farbe(n):")
    for c in best:
        st.markdown(f"**{c}** – {color_labels[c]}")

    st.markdown("### Farbbalken")
    for c, v in sorted(score.items(), key=lambda x: -x[1]):
        bar = '█' * v
        st.markdown(f"`{c}` {bar} ({v} Punkte) – {color_labels[c]}")

    st.markdown("---")
    st.subheader("🎯 Vorschläge für Farbkombinationen")
    for name, colorset in combinations.items():
        diffs = [abs(score[c] - max_score) for c in colorset]
        if max(diffs) <= 2:
            st.markdown(f"✅ **{name}**")

    if st.button("Neu starten"):
        st.session_state.answers = []
        st.session_state.step = 0
        st.experimental_rerun()
