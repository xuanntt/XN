# Import required libraries
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from math import sqrt

class DataProcessor:
    def __init__(self, training_data_file, ideal_functions_file, test_data_file):
        # Create SQLAlchemy engine
        self.engine = create_engine("sqlite:///data.db")
        # Load training data, ideal functions, and test data from CSV files
        self.training_data = pd.read_csv("train.csv")
        self.ideal_functions = pd.read_csv("ideal.csv")
        self.test_data = pd.read_csv("test.csv")
        # Initialize empty lists to store best fits and deviations
        self.best_fits = []
        self.deviations = []