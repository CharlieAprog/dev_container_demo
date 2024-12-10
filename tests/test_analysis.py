import pytest
import pandas as pd
import numpy as np
from src.analysis import DataAnalyzer

@pytest.fixture
def sample_data():
    # Set a random seed for reproducibility
    np.random.seed(42)
    return pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randn(100)
    })

def test_summary_stats(sample_data):
    analyzer = DataAnalyzer(sample_data)
    stats = analyzer.generate_summary_stats()
    assert isinstance(stats, pd.DataFrame)
    assert not stats.empty

def test_scale_features(sample_data):
    analyzer = DataAnalyzer(sample_data)
    scaled_data = analyzer.scale_features(['A', 'B'])
    
    # Test mean is close to 0 (allowing for small numerical differences)
    assert abs(scaled_data['A'].mean()) < 0.1
    assert abs(scaled_data['B'].mean()) < 0.1
    
    # Test standard deviation is close to 1 (allowing for small numerical differences)
    assert abs(scaled_data['A'].std() - 1) < 0.1
    assert abs(scaled_data['B'].std() - 1) < 0.1
    
    # Verify C column wasn't modified by comparing with original
    pd.testing.assert_series_equal(scaled_data['C'], sample_data['C'])
    
    # Verify scaled columns are different from original
    with pytest.raises(AssertionError):
        pd.testing.assert_series_equal(scaled_data['A'], sample_data['A'])
    with pytest.raises(AssertionError):
        pd.testing.assert_series_equal(scaled_data['B'], sample_data['B'])

def test_correlation_matrix_generation(sample_data):
    analyzer = DataAnalyzer(sample_data)
    # Test that plot_correlation_matrix runs without error
    try:
        analyzer.plot_correlation_matrix()
        success = True
    except Exception:
        success = False
    assert success