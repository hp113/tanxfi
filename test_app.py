import unittest
import pandas as pd
from app import load_data, compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, top_10_customers_by_revenue

class TestOrderAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Load data for tests
        cls.df = load_data("orders.csv")

    def test_load_data(self):
        #Test loading of CSV data 
        self.assertIsInstance(self.df, pd.DataFrame)
        print("Unit test 4 completed successfully")

    def test_compute_revenue_by_month(self):
        # Test computation of revenue by month
        revenue_by_month = compute_revenue_by_month(self.df)
        self.assertIsInstance(revenue_by_month, pd.Series)
        self.assertGreater(len(revenue_by_month), 0)
        print("Unit test 2 completed successfully")

    def test_compute_revenue_by_product(self):
        # Test computation of revenue by product 
        revenue_by_product = compute_revenue_by_product(self.df)
        self.assertIsInstance(revenue_by_product, pd.Series)
        self.assertGreater(len(revenue_by_product), 0)
        print("Unit test 3 completed successfully")

    def test_compute_revenue_by_customer(self):
        # Test computation of revenue by customer 
        revenue_by_customer = compute_revenue_by_customer(self.df)
        self.assertIsInstance(revenue_by_customer, pd.Series)
        self.assertGreater(len(revenue_by_customer), 0)
        print("Unit test 1 completed successfully")

    def test_top_10_customers_by_revenue(self):
        # Test identification of top customers by revenue 
        revenue_by_customer = compute_revenue_by_customer(self.df)
        top_customers = top_10_customers_by_revenue(revenue_by_customer)
        self.assertIsInstance(top_customers, pd.Series)
        self.assertEqual(len(top_customers), 10)
        print("Unit test 5 completed successfully")

if __name__ == "__main__":
    unittest.main()
    