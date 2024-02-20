import numpy as np
np.random.seed(12)  # For reproducibility


def random_data_similar_noise(non_related_features, colinear_features, noise = 0.2, samples = 1500):
    non_related_data = np.random.randn(samples, non_related_features)
    data = np.zeros((samples, non_related_features + colinear_features))
    data[:, :non_related_features] = non_related_data
    for i in range(colinear_features):  
        coefficients = np.random.randn(non_related_features)  
        another_row = non_related_data.dot(coefficients) 
        row_noise = np.random.randn(samples) * noise
        data[:, i+non_related_features] = another_row + row_noise
    return data


def random_data_various_noise(non_related_features, colinear_features, samples = 1500):
    non_related_data = np.random.randn(samples, non_related_features)
    data = np.zeros((samples, non_related_features + colinear_features))
    data[:, :non_related_features] = non_related_data
    noise_levels = np.random.random(colinear_features)
    for i in range(colinear_features):  
        coefficients = np.random.randn(non_related_features)  
        another_row = non_related_data.dot(coefficients) 
        row_noise = np.random.randn(samples) * noise_levels[i]
        data[:, i+non_related_features] = another_row + row_noise
    return data


def random_data_with_inter_corelations(features, noise_range=(0.1,0.35), size = 1500):
    data = np.zeros((size, features))
    data[:, 0] = np.random.randn(1)
    for i in range(1,features):
        generated_data = data[:, :i]
        coefficients = np.random.randn(i)  
        another_row = generated_data.dot(coefficients) 
        row_noise = np.random.randn(size) * np.random.uniform(noise_range[0], noise_range[1])
        data[:, i] = another_row + row_noise
    return data

        
def random_data_simple_power_relation(size = 1500):
    non_related_data = np.random.randn(size, 2)
    data = np.zeros((size, 3))
    data[:, :2] = non_related_data
    data[:, 2] = data[:, 0] * data[:, 1] * data[:, 1]
    return data

def random_data_nonlinear_1(non_related_features=10, colinear_features=10, nonlinear_features=10, noise_level=0.2, samples=1500):
    data = np.random.randn(samples, non_related_features)
    # colinear features
    for i in range(colinear_features):
        idx = np.random.choice(non_related_features)
        data = np.hstack((data, data[:, [idx]] * np.random.randn() + np.random.randn(samples, 1) * noise_level))
    # nonlinear features
    for i in range(nonlinear_features):
        idx = np.random.choice(non_related_features)
        if i % 2 == 0:
            # Polynomial transformation
            data = np.hstack((data, data[:, [idx]]**2 + np.random.randn(samples, 1) * noise_level))
        else:
            # Trigonometric transformation
            data = np.hstack((data, np.sin(data[:, [idx]]) + np.random.randn(samples, 1) * noise_level)) 
    return data

def described_test_data():
    everything = {}
    everything['simple linear data without noise'] = random_data_similar_noise(2, 5, noise=0)
    everything['simple linear data with meaningfull noise'] = random_data_similar_noise(4, 3, noise=0.39)
    everything['strictly linear data with many cooeficients'] = random_data_similar_noise(7, 35, noise=0.15)
    everything['random linear data with various noise levels'] = random_data_various_noise(17, 4)
    everything['various noise and many cooeficients'] = random_data_various_noise(6, 25)
    everything['variations about one variable'] = random_data_various_noise(1, 88)
    everything['one nonlinear feature'] = random_data_nonlinear_1(5, 7, 1)
    everything['lot of nonlinear data'] = random_data_nonlinear_1(7, 5, 9)
    everything['energy as mass and speed squared'] = random_data_simple_power_relation()
    return everything