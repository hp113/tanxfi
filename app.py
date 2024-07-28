#importing the necessary libraries
import pandas as pd

#This function will return a dataFrame containing the order data.
def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        # print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        raise
    except pd.errors.EmptyDataError:
        print("Error: No data in file.")
        raise
    except pd.errors.ParserError:
        print("Error: Error parsing the file.")
        raise

#This function will return the total revenue by month.
def compute_revenue_by_month(df: pd.DataFrame) -> pd.Series:
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_month = df.groupby('month')['total_price'].sum()
    return list(revenue_by_month.items())

#This function will return the total revenue by product.
def compute_revenue_by_product(df: pd.DataFrame) -> pd.Series:
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_product = df.groupby('product_name')['total_price'].sum().sort_values(ascending=False)
    return list(revenue_by_product.items())

#This function will return total revenue by customer.
def compute_revenue_by_customer(df: pd.DataFrame) -> pd.Series:
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_customer = df.groupby('customer_id')['total_price'].sum().sort_values(ascending=False)
    return list(revenue_by_customer.items())

#This function will return the top 10 customers by revenue
def top_10_customers_by_revenue(revenue_by_customer: pd.Series, top_n: int = 10) -> pd.Series:
    return list(revenue_by_customer[:top_n])


def main():
    df = load_data("orders.csv")

    # calculating total revenue by month
    revenue_by_month = compute_revenue_by_month(df)
    # Since compute_revenue_by_month(df) returns a Pandas Series, convert the Series to a dataframe
    revenue_by_month_df = revenue_by_month.reset_index()
    revenue_by_month_df.columns = ['Month', 'Revenue']
    print("Total Revenue by Month:")
    print(revenue_by_month_df)

    # calculating total revenue by product
    revenue_by_product = compute_revenue_by_product(df)
    revenue_by_product_df = revenue_by_product.reset_index()
    revenue_by_product_df.columns = ['Product', 'Revenue']
    print("\nTotal revenue by product:")
    print(revenue_by_product_df)

    # calculating total revenue by customer
    revenue_by_customer = compute_revenue_by_customer(df)
    revenue_by_customer_df = revenue_by_customer.reset_index()
    revenue_by_customer_df.columns = ['Customer ID', 'Revenue']
    print("\nTotal revenue by customer:")
    print(revenue_by_customer_df)

    # calculating top 10 customers by revenue
    top_10_customers = top_10_customers_by_revenue(revenue_by_customer)
    top_10_customers_df= top_10_customers.reset_index()
    top_10_customers_df.columns = ['Customer ID', 'Revenue']
    print("\nTop 10 customers by revenue:")
    print(top_10_customers_df)


if __name__ == "__main__":
    main()
