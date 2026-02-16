import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def generate_sales_dashboard(sales_data, output_file='sales_dashboard.html', time_period='monthly', highlight_threshold=None):
    """
    Generate an interactive sales dashboard with multiple visualizations.
    
    This function accepts raw sales transaction data and produces a 2x3 grid 
    of complementary visualizations to answer business questions about:
    - When sales occur (by time period)
    - What products drive revenue (product breakdown)
    - Where sales come from (by region)
    - Which products underperform (top/bottom performers)

    Args:
        sales_data: CSV file path (str) or pandas DataFrame
        output_file: Path to save interactive HTML dashboard (default: sales_dashboard.html)
        time_period: 'monthly' or 'quarterly' time bucket aggregation (default: 'monthly')
        highlight_threshold: Optional threshold value; sales exceeding this get a red ↑ marker

    Returns:
        plotly.graph_objects.Figure: The dashboard figure object
        
    Raises:
        ValueError: If input is invalid, required columns missing, or invalid time_period
    """
    # Load data
    if isinstance(sales_data, str):
        # Input is a file path.
        if sales_data.endswith('.csv'):
            # Only CSV format supported; other formats like Excel, JSON would need
            # different loading functions (pd.read_excel, pd.read_json, etc.)
            df = pd.read_csv(sales_data)
        else:
            raise ValueError("Unsupported file format. Only CSV files are supported.")
    elif isinstance(sales_data, pd.DataFrame):
        # Input is already a DataFrame; make a copy to prevent the function
        # from inadvertently modifying the caller's original data if we later
        # perform in-place operations
        df = sales_data.copy()
    else:
        raise ValueError("sales_data must be a file path or a pandas DataFrame")

    # Ensure required columns exist
    required_columns = ['date', 'product', 'region', 'sales_amount']
    for col in required_columns:
        if col not in df.columns:
            # Include the column name in error so caller knows exactly what's wrong
            raise ValueError(f"Missing required column: {col}")
        if len(df) == 0:
            raise ValueError("Cannot generate dashboard: sales_data is empty (0 rows)")

    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Aggregate data by time period
    if time_period == 'monthly':
        df['period'] = df['date'].dt.strftime('%Y-%m')
    elif time_period == 'quarterly':
        df['period'] = df['date'].dt.year.astype(str) + '-Q' + df['date'].dt.quarter.astype(str)
    else:
        raise ValueError("time_period must be 'monthly' or 'quarterly'")

    # Aggregate sales by period, product, and region
    period_sales = df.groupby(['period', 'product']).agg({'sales_amount': 'sum'}).reset_index()
    region_sales = df.groupby(['region', 'period']).agg({'sales_amount': 'sum'}).reset_index()

    # Create a figure with subplots
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=("Sales by Period", "Sales by Product", "Sales by Region", "Top Products", "Bottom Products"),
        specs=[[{"type": "bar"}, {"type": "pie"}, {"type": "bar"}],
       [{"type": "table"}, {"type": "table"}, {"type": "table"}]]
    )

    # --- Chart 1: Sales by Period (Bar Chart, Top-Left) ---
    # Shows total sales across ALL products and regions, grouped by time period.
    period_totals = df.groupby('period').agg({'sales_amount': 'sum'}).reset_index()
    fig.add_trace(
        go.Bar(x=period_totals['period'], y=period_totals['sales_amount'], name="Sales by Period"),
        row=1, col=1
    )

    # --- Chart 2: Sales by Product (Pie Chart, Top-Middle) ---
    # Shows percentage breakdown of total sales across all products.
    product_totals = df.groupby('product').agg({'sales_amount': 'sum'}).reset_index()
    fig.add_trace(
        go.Pie(labels=product_totals['product'], values=product_totals['sales_amount'], name="Sales by Product"),
        row=1, col=2
    )

    # --- Chart 3: Sales by Region (Bar Chart, Top-Right) ---
    # Shows total sales aggregated by geographic region.
    fig.add_trace(
        go.Bar(x=region_sales['region'], y=region_sales['sales_amount'], name="Sales by Region"),
        row=2, col=1
    )

    # --- Chart 4: Top 5 Products (Table, Bottom-Middle) ---
    # Shows the 5 best-selling products with exact sales amounts.
    top_products = product_totals.sort_values('sales_amount', ascending=False).head(5)
    fig.add_trace(
        go.Table(
            header=dict(values=["Product", "Sales Amount"]),
            cells=dict(values=[top_products['product'], top_products['sales_amount']])
        ),
        row=2, col=2
    )

    # --- Chart 5: Bottom 5 Products (Table, Bottom-Right) ---
    # Shows the 5 worst-selling products.
    bottom_products = product_totals.sort_values('sales_amount', ascending=True).head(5)
    fig.add_trace(
        go.Table(
            header=dict(values=["Product", "Sales Amount"]),
            cells=dict(values=[bottom_products['product'], bottom_products['sales_amount']])
        ),
        row=2, col=3
    )

    # Update layout
    fig.update_layout(
        title_text="Sales Dashboard",
        height=800,
        width=1200,
    )

    # Highlight values above threshold if provided
    if highlight_threshold is not None:
        for i, value in enumerate(period_totals['sales_amount']):
            if value > highlight_threshold:
                fig.add_annotation(
                    x=period_totals['period'][i],
                    y=value,
                    text="↑",
                    showarrow=False,
                    font=dict(size=20, color="red")
                )

    # Generate HTML file
    fig.write_html(output_file)
    print(f"Dashboard saved to {os.path.abspath(output_file)}")

    # Return figure for display
    return fig
