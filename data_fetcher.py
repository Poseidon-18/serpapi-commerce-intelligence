import os
from serpapi import GoogleSearch
import pandas as pd

def fetch_product_data(query: str, location: str = "India", num_results: int = 20) -> pd.DataFrame:
    """
    Queries SerpApi Google Shopping API and converts results into a pandas DataFrame.
    """
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        raise ValueError("SERPAPI_KEY environment variable is missing.")

    params = {
        "engine": "google_shopping",
        "q": query,
        "gl": "in" if location == "India" else "us",
        "hl": "en",
        "num": num_results,
        "api_key": api_key
    }

    # Execute SerpApi search
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results.get("shopping_results", [])

    if not shopping_results:
        return pd.DataFrame()

    extracted_items = []
    for item in shopping_results:
        extracted_items.append({
            "Title": item.get("title", "N/A"),
            "Price": item.get("extracted_price", None),
            "Merchant": item.get("source", "Unknown"),
            "Rating": item.get("rating", "N/A"),
            "Reviews": item.get("reviews", 0),
            "Link": item.get("link", "#")
        })

    df = pd.DataFrame(extracted_items)
    # Remove items where price parsing failed
    df.dropna(subset=["Price"], inplace=True)
    return df