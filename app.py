import streamlit as st
import pandas as pd
import plotly.express as px
#import os
#from dotenv import load_dotenv
#from openai import OpenAI

#load_dotenv()

#openai_api_key = os.getenv("OPENAI_API_KEY")

#client = OpenAI(api_key=openai_api_key)#

#if not os.getenv("OPENAI_API_KEY"):
    #st.error("OPENAI_API_KEY was not found in the .env file.")

st.set_page_config(
    page_title="AI Supermarket Sales Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Supermarket Sales Analyst")
st.write("Upload your supermarket sales CSV to begin.")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Load data
    df = pd.read_csv(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert numeric columns
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["cogs"] = pd.to_numeric(df["cogs"], errors="coerce")
    df["gross income"] = pd.to_numeric(df["gross income"], errors="coerce")

    st.success("Data uploaded successfully!")

    # =========================
    # KPIs
    # =========================

    total_sales = df["Sales"].sum()
    total_cogs = df["cogs"].sum()
    total_profit = df["gross income"].sum()
    total_transactions = len(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

    col2.metric(
        "Total COGS",
        f"${total_cogs:,.2f}"
    )

    col3.metric(
        "Gross Income",
        f"${total_profit:,.2f}"
    )

    col4.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

    st.divider()

    # =========================
    # Sales by Product Line
    # =========================

    st.subheader("💰 Sales by Product Line")

    product_sales = (
        df.groupby("Product line")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        product_sales,
        x="Product line",
        y="Sales",
        title="Sales by Product Line"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =========================
    # Sales by Branch
    # =========================

    st.subheader("🏢 Sales by Branch")

    branch_sales = (
        df.groupby("Branch")["Sales"]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        branch_sales,
        x="Branch",
        y="Sales",
        title="Sales by Branch"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =========================
    # Payment Methods
    # =========================

    st.subheader("💳 Payment Methods")

    payment_counts = (
        df["Payment"]
        .value_counts()
        .reset_index()
    )

    payment_counts.columns = [
        "Payment",
        "Transactions"
    ]

    fig3 = px.pie(
        payment_counts,
        names="Payment",
        values="Transactions",
        title="Transactions by Payment Method"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# =========================
# Business Analyst
# =========================

st.divider()

st.subheader("🤖 Business Analyst")

st.write(
    "Ask a business question about your supermarket sales data."
)

question = st.text_input(
    "Example: How much do I need to sell to make $18,000 profit?"
)

if st.button("Analyze"):

    if question:

        question_lower = question.lower()

        # Calculate current gross margin
        total_sales = df["Sales"].sum()
        total_profit = df["gross income"].sum()

        gross_margin = total_profit / total_sales

        # Check for profit target questions
        if "how much" in question_lower and "sell" in question_lower:

            import re

            # Find dollar amount in the question
            match = re.search(
                r"\$?\s*([\d,]+(?:\.\d+)?)\s*k?",
                question_lower
            )

            if match:

                amount = float(match.group(1).replace(",", ""))

                # Convert 18k → 18000
                if "k" in question_lower[match.start():match.end()]:
                    amount *= 1000

                required_sales = amount / gross_margin

                st.success(
                    f"To make approximately ${amount:,.0f} "
                    f"in gross profit, you would need about "
                    f"${required_sales:,.2f} in sales."
                )

                st.info(
                    f"Your historical gross margin is "
                    f"{gross_margin * 100:.2f}%."
                )

            else:
                st.warning(
                    "Please include a target profit amount, "
                    "such as $18,000."
                )

        else:

            st.info(
                "I can currently calculate profit targets. "
                "Try asking: "
                "'How much do I need to sell to make $18k profit?'"
            )

    else:

        st.warning("Please enter a question.")
