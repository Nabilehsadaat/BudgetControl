import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="BudgetControl💰 ")
st.title("BudgetControl💰 ")

transactions = []

# neue Transaktion hinzufügen
def add_transaction(datum, beschreibung, kategorie, betrag):
    transaction = {
        "Datum": datum,
        "Beschreibung": beschreibung,
        "Kategorie": kategorie,
        "Betrag": betrag
    }
    transactions.append(transaction)

#angaben
with st.form("hinzufügen"):
    datum = st.date_input("Datum", value=datetime.now())
    beschreibung = st.text_input("Beschreibung")
    kategorie = st.selectbox(
        "Kategorie",
        ["Einkauf", "Miete", "Freizeit", "Transport", "Sparen", "Schule", "Spenden", "Beauty", "Rechnungen", "Apps", "Sonstiges"]
    )
    betrag = st.number_input("Betrag (positiv = Einnahme, negativ = Ausgabe)", value=0.0, format="%.2f")
    submitted = st.form_submit_button("Transaktion hinzufügen")

# Verarbeitung nach Submit
if submitted:
    add_transaction(datum.strftime("%Y-%m-%d"), beschreibung, kategorie, float(betrag))
    st.success("Transaktion hinzugefügt!")

# Buttons
col_a, col_b = st.columns([1,1])
with col_a:
    if st.button("Letzte löschen"):
        if transactions:
            transactions.pop()
            st.success("Letzte Transaktion gelöscht!")
        else:
            st.warning("Keine Transaktionen zum Löschen vorhanden.")

with col_b:
    if st.button("Alle Transaktionen löschen"):
        transactions = []
        st.success("Alle Transaktionen gelöscht!")        


# Anzeige der Transaktionen
st.warning("Show.")

if  transactions:
    df = pd.DataFrame(transactions)
    st.write("Meine Transaktionen")
    st.dataframe(df)
    st.warning("Meine Transaktionen.")
else:
    st.warning("Noch keine Transaktionen.")