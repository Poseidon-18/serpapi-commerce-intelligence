#  Merchant Intelligence & Price Anomaly Detector

A real-time market intelligence dashboard built for the **SerpApi India Hackathon 2026**. 

This application leverages **SerpApi's Google Shopping API** to aggregate multi-merchant product listings, identify price anomalies, and highlight market deals below average listing prices.

# Key Features
- **Real-Time Data Extraction**: Queries structured Google Shopping results using SerpApi.
- **Price Anomaly Detection**: Automatically calculates average market price and flags seller listings discounted by 15%+ below market average.
- **Visual Merchant Analytics**: Interactive price distribution bar charts powered by Plotly.
- **Merchant Comparison**: Clean tabular view comparing ratings, review counts, and direct product links.

# Tech Stack
- **Data Engine**: SerpApi (`google-search-results`)
- **Backend / UI**: Python, Streamlit
- **Data & Visualizations**: Pandas, Plotly

# Startuo
1. Clone the repository: U should know how to clone
2. Set up virtual environment: python -m venv venv
source venv/bin/activate
3. Install dependencies : pip install -r requirements.txt
4. Get ur own key: export SERPAPI_KEY="your_serpapi_api_key_here"
5. Run the application: streamlit run app.py


