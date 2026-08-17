# 📊 AI Supermarket Sales Analyst

An interactive supermarket sales analysis application built with Python, Pandas, Plotly, and Streamlit.

The project analyzes supermarket transaction data and provides business-focused insights through an interactive web dashboard.

> 🚧 This project is currently under development. AI model integration will be added in a future version.

---

## 🚀 Project Overview

The AI Supermarket Sales Analyst is a data analytics project designed to turn supermarket transaction data into useful business insights.

The application currently allows users to:

- Upload supermarket sales data
- Calculate key business metrics
- Analyze sales by product line
- Analyze sales by branch
- Analyze payment methods
- Calculate gross income and COGS
- Ask basic business questions using Python-based analysis

The long-term goal is to integrate an AI model that can understand natural-language questions and provide data-driven business insights.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data cleaning and analysis |
| Streamlit | Interactive web application |
| Plotly | Interactive data visualization |
| OpenAI API | Planned AI integration |
| Git & GitHub | Version control and portfolio |

---

## 📁 Project Structure

```text
AI-Supermarket-Sales-Analyst/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── SuperMarket_Analysis.csv
│
└── screenshots/

📊 Dataset

The project uses a supermarket sales dataset containing transaction-level information such as:

Invoice ID
Branch
City
Customer Type
Gender
Product Line
Unit Price
Quantity
Tax
Sales
Date
Time
Payment
COGS
Gross Income
Rating

The dataset contains 1,000 transactions.

📈 Current Features
Key Performance Indicators

The dashboard calculates:

Total Sales
Total COGS
Gross Income
Total Transactions
Sales Analysis

The application provides visualizations for:

Sales by Product Line
Sales by Branch
Payment Methods
Business Analysis

The application can perform basic business calculations using Python.

For example:

"How much do I need to sell to make $18,000 profit?"

The application calculates the required sales using the historical gross profit margin.

🤖 AI Integration

AI integration is currently being developed.

The planned AI functionality will allow users to ask natural-language questions such as:

Which product line generates the most sales?
Which branch performs the best?
How much do I need to sell to make $18,000 profit?
What are the main business trends in this dataset?

The goal is to combine traditional Python data analysis with an AI model that can explain the results in natural language.

💻 Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project
cd AI-Supermarket-Sales-Analyst
3. Install dependencies
pip install -r requirements.txt
4. Run the application
streamlit run app.py

The application will open in your browser.

🔐 Environment Variables

API keys and other secrets should never be committed to GitHub.

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

The .env file is excluded from Git using .gitignore.

📸 Screenshots

Screenshots of the application will be added here as the project develops.

🗺️ Future Improvements

Planned features include:

 Interactive Branch and City filters
 More advanced data profiling
 Natural-language AI analyst
 AI-generated business insights
 Automated business reports
 Additional interactive visualizations
 AI model comparison
 Deployment
 Improved UI/UX
📚 What I'm Learning

This project is being used to practice:

Python
Pandas
Data analysis
Data visualization
Streamlit
APIs
AI integration
Git & GitHub
Business analytics
📌 Project Status

Version: v0.1.0

Status: 🚧 In Development

The initial Streamlit dashboard and Python-based business analysis functionality are working. AI model integration and additional features are planned for future versions.

👨‍💻 Author

Trishant Basnet

Built as a portfolio project to practice data analytics, Python, visualization, and AI integration.

### One important thing

Your README currently says **OpenAI API = planned AI integration**, which is accurate because we've stopped the API calls due to the quota issue.

Once we add another AI model later, we'll update the README to reflect the actual model you're using.

After you create `README.md`, **save it with Ctrl + S**. Then we'll check `git status` and upload the project safely to GitHub.