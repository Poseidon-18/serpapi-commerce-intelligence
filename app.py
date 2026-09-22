import streamlit as st
import plotly.express as px
from data_fetcher import fetch_product_data

st.set_page_config(
    page_title="Merchant Intelligence & Price Anomaly Detector",
    layout="wide"
)

st.title("🛒 Merchant Intelligence & Price Anomaly Detector")
st.caption("Real-time market analytics powered by SerpApi Google Shopping Engine")

# Sidebar Controls
st.sidebar.header("Search Configuration")
query = st.sidebar.text_input("Product Name / Keyword:", value="M2 MacBook Air")
num_items = st.sidebar.slider("Number of Listings to Fetch:", 10, 50, 25)

if st.sidebar.button("Run Market Scan"):
    with st.spinner("Fetching live listings via SerpApi..."):
        try:
            df = fetch_product_data(query, num_results=num_items)

            if df.empty:
                st.warning("No listings found. Try adjusting your search query.")
            else:
                # Key Metrics Calculations
                avg_price = df["Price"].mean()
                min_price = df["Price"].min()
                max_price = df["Price"].max()
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Average Market Price", f"₹{avg_price:,.2f}")
                col2.metric("Lowest Listed Price", f"₹{min_price:,.2f}")
                col3.metric("Highest Listed Price", f"₹{max_price:,.2f}")

                st.markdown("---")

                # Visualizations Segment
                col_chart1, col_chart2 = st.columns(2)

                with col_chart1:
                    st.subheader("Price Distribution across Merchants")
                    fig_bar = px.bar(
                        df, 
                        x="Merchant", 
                        y="Price", 
                        color="Price", 
                        hover_data=["Title"],
                        title="Listing Prices by Merchant"
                    )
                    st.plotly_chart(fig_bar, use_container_width=True)

                with col_chart2:
                    st.subheader("Market Anomalies & Deals")
                    deal_threshold = avg_price * 0.85  # 15% below market average
                    deals_df = df[df["Price"] <= deal_threshold]

                    if not deals_df.empty:
                        st.success(f"Detected {len(deals_df)} price anomaly deal(s) (>15% below market average)!")
                        st.dataframe(deals_df[["Title", "Price", "Merchant", "Rating"]])
                    else:
                        st.info("Prices are uniform across merchants; no extreme low anomalies detected.")

                # Raw Data View
                st.subheader("All Extracted Merchant Listings")
                st.dataframe(df)

        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")