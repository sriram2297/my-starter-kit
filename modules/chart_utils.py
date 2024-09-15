# modules/chart_utils.py

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Function to generate a Seaborn chart
def generate_chart(df, chart_type, **kwargs):
    plt.figure(figsize=(10, 6))
    if chart_type == "histplot":
        sns.histplot(data=df, **kwargs)
    elif chart_type == "scatterplot":
        sns.scatterplot(data=df, **kwargs)
    elif chart_type == "lineplot":
        sns.lineplot(data=df, **kwargs)
    elif chart_type == "barplot":
        sns.barplot(data=df, **kwargs)
    elif chart_type == "boxplot":
        sns.boxplot(data=df, **kwargs)
    elif chart_type == "pairplot":
        sns.pairplot(df, **kwargs)
    elif chart_type == "violinplot":
        sns.violinplot(data=df, **kwargs)
    # elif chart_type == "heatmap":
    #     sns.heatmap(df.corr(), annot=True, cmap="coolwarm", **kwargs)
    elif chart_type == 'heatmap':
        # Filter only numeric columns for correlation
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        
        if not numeric_df.empty:
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", **kwargs)
            plt.show()
        else:
            print("No numeric data to plot a heatmap.")
    st.pyplot(plt)

# Function to interpret user prompt for chart type
def interpret_prompt(prompt):
    prompt = prompt.lower()
    if "histogram" in prompt:
        return "histplot"
    elif "scatter" in prompt:
        return "scatterplot"
    elif "line" in prompt:
        return "lineplot"
    elif "bar" in prompt:
        return "barplot"
    elif "box" in prompt:
        return "boxplot"
    elif "pair" in prompt:
        return "pairplot"
    elif "violin" in prompt:
        return "violinplot"
    elif "heatmap" in prompt:
        return "heatmap"
    elif "kde" in prompt:
        return "kdeplot"
    else:
        return None
