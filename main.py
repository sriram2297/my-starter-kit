# main.py

import os
import streamlit as st
import pandas as pd
from modules.doc_utils import extract_text_from_document
from modules.chart_utils import generate_chart, interpret_prompt
from modules.api_utils import ask_mistral_question

# Streamlit app
def main():
    st.title("IntelliDoc: Your AI-Powered Document Assistant 📄")

    # File upload section
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "pdf", "docx", "md"])

    if uploaded_file:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension in ['csv', 'xlsx']:
            df = pd.read_csv(uploaded_file) if file_extension == 'csv' else pd.read_excel(uploaded_file)
            st.write("DataFrame Head:")
            st.write(df.head())
            st.write("\nDataFrame Info:")
            st.write(df.info())

            # Sidebar for filtering options
            st.sidebar.header("Filter Options")
            selected_columns = st.sidebar.multiselect("Select columns for filtering", df.columns.tolist())
            filtered_df = df.copy()

            # Apply filtering logic
            for selected_col in selected_columns:
                column_data = df[selected_col]
                
                if pd.api.types.is_numeric_dtype(column_data):
                    min_value = column_data.min()
                    max_value = column_data.max()
                    selected_range = st.sidebar.slider(f"Select range for {selected_col}", min_value=min_value, max_value=max_value, value=(min_value, max_value))
                    filtered_df = filtered_df[filtered_df[selected_col].between(selected_range[0], selected_range[1])]
                
                elif pd.api.types.is_datetime64_any_dtype(column_data):
                    min_date = column_data.min()
                    max_date = column_data.max()
                    date_range = st.sidebar.slider(f"Select date range for {selected_col}", min_value=min_date, max_value=max_date, value=(min_date, max_date))
                    filtered_df = filtered_df[filtered_df[selected_col].between(date_range[0], date_range[1])]
                
                elif pd.api.types.is_categorical_dtype(column_data) or pd.api.types.is_object_dtype(column_data):
                    unique_values = column_data.unique()
                    selected_values = st.sidebar.multiselect(f"Select values for {selected_col}", options=unique_values, default=unique_values)
                    filtered_df = filtered_df[filtered_df[selected_col].isin(selected_values)]
                else:
                    st.warning(f"Filtering for column '{selected_col}' is not applied. Unsupported column type.")

            # Prompt for chart generation
            prompt = st.text_input("Enter your chart request (e.g., 'Create a histogram for this dataset')")

            if prompt:
                chart_type = interpret_prompt(prompt)
                if chart_type:
                    st.write(f"Generating {chart_type}...")
                    if chart_type == "scatterplot" or chart_type == "lineplot":
                        x_col = st.selectbox('Select X-axis column', filtered_df.columns)
                        y_col = st.selectbox('Select Y-axis column', filtered_df.columns)
                        generate_chart(filtered_df, chart_type, x=x_col, y=y_col)
                    elif chart_type == "histplot" or chart_type == "barplot":
                        col = st.selectbox('Select column', filtered_df.columns)
                        generate_chart(filtered_df, chart_type, x=col)
                    else:
                        generate_chart(filtered_df, chart_type)
                else:
                    st.error("Sorry, I couldn't understand the chart type from your prompt.")
            
            # Add download button for filtered data
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="Download Filtered Data as CSV",
                data=csv,
                file_name='filtered_data.csv',
                mime='text/csv'
            )

        elif file_extension in ['pdf', 'docx', 'md']:
            document_text = extract_text_from_document(uploaded_file)
            st.write("Document Text Extracted")

            # Display document text (optional)
            st.text_area("Document Text", document_text, height=300)

            user_question = st.text_input("Ask a question related to the document:")

            if user_question:
                answer = ask_mistral_question(document_text, user_question)
                st.markdown(f"**Answer:** {answer}")

        else:
            st.error("Unsupported file format")

if __name__ == "__main__":
    main()
