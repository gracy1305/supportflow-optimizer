import streamlit as st
import pandas as pd

# Sample Data
data = {
    "Ticket ID": ["T001", "T002", "T003", "T004", "T005"],
    "Department": ["Engineering", "Policy", "Product", "Engineering", "Business"],
    "Status": ["Open", "Closed", "In Progress", "Open", "Closed"],
    "Priority": ["High", "Medium", "High", "Low", "Medium"],
    "Owner": ["Gracy", "Amit", "Nina", "Gracy", "Sam"],
    "Created Date": ["2025-07-20", "2025-07-18", "2025-07-19", "2025-07-21", "2025-07-17"],
    "Resolution Time (days)": [None, 2, None, None, 3],
    "Notes": [
        "Need API integration support",
        "Resolved login issue",
        "UI flow alignment request",
        "Data mismatch in report",
        "Partner access revoked and restored"
    ]
}

df = pd.DataFrame(data)

st.title("SupportFlow Optimizer – CRM Ticket Dashboard")

with st.sidebar:
    st.header("Filter Tickets")
    dept = st.multiselect("Department", options=df["Department"].unique(), default=df["Department"].unique())
    status = st.multiselect("Status", options=df["Status"].unique(), default=df["Status"].unique())
    priority = st.multiselect("Priority", options=df["Priority"].unique(), default=df["Priority"].unique())

filtered_df = df[df["Department"].isin(dept) & df["Status"].isin(status) & df["Priority"].isin(priority)]

st.subheader("Filtered Ticket View")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("Ticket Status Overview")
st.bar_chart(filtered_df["Status"].value_counts())

st.download_button("Download CSV", data=filtered_df.to_csv(index=False), file_name="filtered_tickets.csv", mime="text/csv")
