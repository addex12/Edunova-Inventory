import streamlit as st
from app import app, db
from app.models import Item
import pandas as pd

@st.cache
def load_data():
    with app.app_context():  # Use Flask app context
        items = Item.query.all()
        return pd.DataFrame([(i.id, i.name, i.quantity) for i in items], columns=['ID', 'Name', 'Quantity'])

st.title("Inventory Management Dashboard")
data = load_data()
st.dataframe(data)

# Optionally, add interactivity such as adding and removing items through Streamlit
