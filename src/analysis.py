import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

class DataAnalyzer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.scaler = StandardScaler()
    
    def generate_summary_stats(self) -> pd.DataFrame:
        """Generate summary statistics for numerical columns."""
        return self.data.describe()
    
    def plot_correlation_matrix(self, save_path: str = None):
        """Create a correlation matrix heatmap."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        corr_matrix = self.data[numeric_cols].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()
    
    def scale_features(self, columns: list) -> pd.DataFrame:
        """
        Scale selected features using StandardScaler.
        Only the specified columns will be scaled, others remain unchanged.
        """
        scaled_data = self.data.copy()
        if columns:
            scaled_data[columns] = self.scaler.fit_transform(scaled_data[columns])
        return scaled_data