import streamlit as st

def switch_page(page_name: str):
    """
    Switches the current page to the specified page name using the official Streamlit API.
    
    This function relies on Streamlit's built-in page management and is the
    recommended way to navigate programmatically. It requires Streamlit 1.32.0 or higher.

    Args:
        page_name (str): The name of the page to switch to (e.g., "Professional Screen").
    """
    try:
        st.switch_page(page_name)
    except Exception as e:
        # This will catch errors if the page name is incorrect
        st.error(f"Could not find page '{page_name}'. Please check the page name and file.")
        print(f"Error: {e}")
