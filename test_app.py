import unittest
import pandas as pd
from app import load_data, compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, top_10_customers_by_revenue
from test_cases import test_cases

class TestOrderAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #Load data for tests
        self.test_files = ['test1.csv', 'test2.csv', 'test3.csv', 'test4.csv', 'test5.csv']
        self.test_cases = test_cases

    def test_load_data(self):
        #Test loading of CSV data 
        for file in self.test_files:
            df = load_data(file)
            self.assertIsInstance(df, pd.DataFrame)

    def test_compute_revenue_by_month(self):
        # Test computation of revenue by month
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_month = compute_revenue_by_month(df)
            expected = self.test_cases[f"case{i}"]["total revenue by month"]
            self.assertEqual(revenue_by_month.sort(),expected.sort())

    def test_compute_revenue_by_product(self):
        # Test computation of revenue by product 
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_product = compute_revenue_by_product(df)
            expected = self.test_cases[f"case{i}"]["total revenue by product"]
            self.assertEqual(revenue_by_product.sort(),expected.sort())

    def test_compute_revenue_by_customer(self):
        # Test computation of revenue by customer 
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_customer = compute_revenue_by_customer(df)
            expected = self.test_cases[f"case{i}"]["total revenue by customer"]
            self.assertEqual(revenue_by_customer.sort(),expected.sort())

    def test_top_10_customers_by_revenue(self):
        # Test identification of top customers by revenue 
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_customer = compute_revenue_by_customer(df)
            top_customers = top_10_customers_by_revenue(revenue_by_customer, 10)
            expected = self.test_cases[f"case{i}"]["top 10 customers by revenue"]
            self.assertEqual(top_customers.sort(),expected.sort())

if __name__ == "__main__":
    unittest.main()
    