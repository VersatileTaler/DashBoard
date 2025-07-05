import streamlit as st
import pandas as pd
 
st.title("Transaction Dashboard from Excel")
 
# Step 2: Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
 
if uploaded_file:
    # Step 3: Read Excel into pandas DataFrame
    df = pd.read_excel(uploaded_file)
 
    # Step 4: Check for necessary columns
    required_cols = {'Date', 'Success Count', 'Failure Count'}
    if required_cols.issubset(df.columns):
        # Step 5: Calculate Total and Decline %
        df['Total'] = df['Success Count'] + df['Failure Count']
        df['Decline %'] = (df['Failure Count'] / df['Total']) * 100
 
        # Step 6: Display Data Table
        st.subheader("Data Preview")
        st.dataframe(df)
 
        # Step 7: Display Charts
        st.subheader("Success and Failure Counts Over Time")
        st.line_chart(df.set_index('Date')[['Success Count', 'Failure Count']])
 
        st.subheader("Decline Percentage Over Time")
        st.bar_chart(df.set_index('Date')['Decline %'])
 
        # Step 8: Show Average Decline %
        avg_decline = df['Decline %'].mean()
        st.metric("Average Decline %", f"{avg_decline:.2f}%")
 
    else:
        st.error(f"Excel file must contain columns: {', '.join(required_cols)}")