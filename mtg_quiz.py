import streamlit as st

st.set_page_config(page_title="MTG Persönlichkeits-Test", layout="centered")
st.title("Magic: The Gathering – Persönlichkeits-Test")

questions = [
    {
        "text": "Was ist dir wichtiger?",
        "options": [
            ("Stabilität & Ordnung", ["W"]),
            ("Wissen & Kontrolle", ["U"]),
            ("Stärke & Selbstbehauptung", ["B"]),
            ("Spontanität & Leidenschaft", ["R"]),
            ("Wachstum & Harmonie", ["G"])
        ]
    },
    {
        "text": "Wie gehst du mit Rückschlägen um?",
        "options": [
            ("Ich ziehe mich zurück und analysiere", ["U"]),
            ("Ich kämpfe mich mit roher Kraft zurück", ["R", "G"]),
            ("Ich manipuliere die Situation zu meinem Vorteil", ["B"]),
            ("Ich halte mich an Prinzipien", ["W"]),
            ("Ich finde kreative neue Wege", ["U", "G"])
        ]
    },
    {
        "text": "Welche Spielweise gefällt dir am besten?",
        "options": [
            ("Ich kontrolliere und überblicke", ["W", "U"]),
            ("Ich spiele schnell und direkt", ["R", "G"]),
            ("Ich lasse Dinge sterben und wiederkehren", ["B", "R"]),
            ("Ich gehe weite Wege, um große Ziele zu erreichen", ["G", "U", "R"]),
            ("Ich bringe Struktur ins Chaos", ["W", "B", "R"])
        ]
    }
]

color_labels = {
    "W": "Weiß – Ordnung & Gemeinschaft",
    "U": "Blau – Wissen & Kontrolle",
    "B": "Schwarz – Macht & Opfer",
    "R": "Rot – Freiheit & Emotion",
    "G": "Grün – Wachstum & Natur"
}

if "answers" not in st.session_state:
    st.session_state.answers = []

if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.subheader(f"Frage {st.session_state.step + 1} von {len(questions)}")
    st.write(q["text"])

    for text, colors in q["options"]:
        if st.button(text):
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

    st.success("Dein MTG-Farbprofil:")
    for c in best:
        st.markdown(f"**{c}** – {color_labels[c]}")

    if st.button("Neu starten"):
        st.session_state.answers = []
        st.session_state.step = 0
        st.experimental_rerun()
