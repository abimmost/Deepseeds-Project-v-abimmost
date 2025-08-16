import streamlit as st

# Initialize inventory in session_state if it doesn't exist
if 'inventory' not in st.session_state:
    st.session_state.inventory = {}

def format_currency(value):
    return f"${value:.2f}"

def add_item_callback():
    name = st.session_state.new_item_name.strip().title()
    price_str = st.session_state.new_item_price.strip()
    stock_str = st.session_state.new_item_stock.strip()
    category = st.session_state.new_item_category.strip().title()

    if not name or not price_str or not stock_str or not category:
        st.error("All fields are required.")
        return

    if name in st.session_state.inventory:
        st.warning("Item already exists.")
        return

    try:
        price = float(price_str)
        stock = int(stock_str)
        if price < 0 or stock < 0:
            st.error("Price and stock cannot be negative.")
            return

        st.session_state.inventory[name] = {"price": price, "stock": stock, "category": category}
        st.success(f"{name} added successfully.")
        st.session_state.new_item_name = ""
        st.session_state.new_item_price = ""
        st.session_state.new_item_stock = ""
        st.session_state.new_item_category = ""
    except ValueError:
        st.error("Invalid input for price or stock. Please enter numbers.")

def update_stock_callback():
    name = st.session_state.update_item_name.strip().title()
    change_str = st.session_state.stock_change.strip()

    if not name or not change_str:
        st.error("All fields are required.")
        return

    if name not in st.session_state.inventory:
        st.error("Item not found.")
        return

    try:
        change = int(change_str)
        st.session_state.inventory[name]["stock"] += change
        if st.session_state.inventory[name]["stock"] < 0:
            st.session_state.inventory[name]["stock"] = 0
        st.success(f"{name} stock updated. New stock: {st.session_state.inventory[name]["stock"]}")
        st.session_state.stock_change = ""
    except ValueError:
        st.error("Invalid input for stock change. Please enter a number.")

st.title("Smart Inventory Manager")

# Use tabs for navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Add New Item", "Update Stock", "Search by Category", "Low Stock Alert", "Total Inventory Value"])

with tab1:
    st.header("Add New Item")
    with st.form("add_item_form"):
        st.text_input("Item Name", key="new_item_name")
        st.text_input("Item Price", key="new_item_price")
        st.text_input("Item Stock", key="new_item_stock")
        st.text_input("Item Category", key="new_item_category")
        st.form_submit_button("Add Item", on_click=add_item_callback)

with tab2:
    st.header("Update Stock")
    with st.form("update_stock_form"):
        st.selectbox("Select Item", options=[""] + list(st.session_state.inventory.keys()), key="update_item_name")
        st.text_input("Stock Change (use - for removal)", key="stock_change")
        st.form_submit_button("Update Stock", on_click=update_stock_callback)

with tab3:
    st.header("Search by Category")
    category_to_search = st.text_input("Enter Category to Search").strip().title()
    if category_to_search:
        found_items = False
        st.subheader(f"Items in {category_to_search}:")
        for name, item in st.session_state.inventory.items():
            if item["category"] == category_to_search:
                st.write(f"• {name} - {format_currency(item['price'])} ({item['stock']} in stock)")
                found_items = True
        if not found_items:
            st.info("No items found in this category.")
    else:
        st.info("Enter a category to search.")

with tab4:
    st.header("Low Stock Alert")
    low_stock_found = False
    st.warning("⚠️ LOW STOCK ALERT:")
    for name, item in st.session_state.inventory.items():
        if item["stock"] <= 5:
            st.write(f"- {name} ({item['stock']} units remaining)")
            low_stock_found = True
    if not low_stock_found:
        st.info("No items currently have low stock.")

with tab5:
    st.header("Total Inventory Value")
    total_value = sum(item["price"] * item["stock"] for item in st.session_state.inventory.values())
    st.success(f"Current Inventory Value: {format_currency(total_value)}")