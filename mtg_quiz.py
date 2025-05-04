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
    },
    {
        "text": "Was motiviert dich im Spiel am meisten?",
        "options": [
            ("Synergien perfekt ausnutzen", ["U", "G"]),
            ("Schneller Sieg durch Aggression", ["R", "W"]),
            ("Wissen, Kontrolle & Manipulation", ["U", "B"]),
            ("Gleichgewicht & Schutz der Gruppe", ["W", "G"]),
            ("Ressourcen zerstören & Druck erzeugen", ["B", "R"])
        ]
    },
    {
        "text": "Was schätzt du bei anderen Spieler*innen?",
        "options": [
            ("Verlässlichkeit & Fairness", ["W"]),
            ("Kreativität & Unberechenbarkeit", ["R"]),
            ("Effizienz & Planung", ["U"]),
            ("Durchhaltevermögen & Überleben", ["B"]),
            ("Verbindung zur Natur & Harmonie", ["G"])
        ]
    },
    {
        "text": "Was ist deine größte spielerische Stärke?",
        "options": [
            ("Ich denke strategisch & langfristig", ["U"]),
            ("Ich kann gut anpassen & improvisieren", ["R", "G"]),
            ("Ich kontrolliere Ressourcen & Optionen", ["B", "U"]),
            ("Ich baue starke Synergien auf", ["G", "W"]),
            ("Ich bringe das Spiel in eine stabile Ordnung", ["W"])
        ]
    },
    {
        "text": "Welche dieser Aussagen beschreibt dich am besten?",
        "options": [
            ("Ich schätze Ordnung, Wissen und Kontrolle über mich selbst.", ["W", "U", "B"]),
            ("Ich bin zäh, impulsiv und lasse mich nicht leicht aufhalten.", ["B", "R", "G"]),
            ("Ich handle klug, natürlich und mit Kraft, wenn es nötig ist.", ["U", "R", "G"]),
            ("Ich bin belastbar, fürsorglich und überlebe jedes Tief.", ["W", "B", "G"]),
            ("Ich bin kreativ, diszipliniert und intuitiv zugleich.", ["W", "U", "R"])
        ]
    },
    {
        "text": "Was ist für dich ein befriedigendes Spielerlebnis?",
        "options": [
            ("Ein langsamer Aufbau mit sicherem Sieg", ["W", "U"]),
            ("Ein mutiger, riskanter Zug, der aufgeht", ["R"]),
            ("Wenn meine Engine wie geplant funktioniert", ["U", "G"]),
            ("Wenn ich Gegner mit Ressourcen kontrolliere", ["B", "U"]),
            ("Wenn ich früh dominieren kann", ["R", "W"])
        ]
    },
    {
        "text": "Welcher dieser Begriffe spricht dich am meisten an?",
        "options": [
            ("Wissen", ["U"]),
            ("Freiheit", ["R"]),
            ("Macht", ["B"]),
            ("Harmonie", ["G"]),
            ("Gesetz", ["W"])
        ]
    },
    {
        "text": "Wenn du die Wahl hättest, würdest du lieber...",
        "options": [
            ("...alle anderen schützen.", ["W"]),
            ("...das Spiel kontrollieren.", ["U"]),
            ("...den Sieg erzwingen.", ["R"]),
            ("...aus dem Tod zurückkehren.", ["B"]),
            ("...mit allem verbunden sein.", ["G"])
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
        if st.button(text, key=f"{st.session_state.step}-{text}"):
            st.session_state.answers.append(colors)
            st.session_state.step += 1
            st.stop()
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

    st.markdown("---")
    st.subheader("🧠 Auswertung")
    st.write("Die folgenden Farben spiegeln deinen Stil, deine Entscheidungen und deine inneren Werte im Kontext von Magic: The Gathering wider:")

    for c in sorted(score.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * c[1]
        st.markdown(f"`{c[0]}` {bar} ({c[1]} Punkte) – {color_labels[c[0]]}")

    st.markdown("---")
    st.info("Dieser Test dient zur Unterhaltung und Persönlichkeitsreflexion basierend auf den Farblehren von MTG. Viel Spaß beim Deckbauen!")

    if st.button("Neu starten"):
        st.session_state.answers = []
        st.session_state.step = 0
        st.experimental_rerun()
