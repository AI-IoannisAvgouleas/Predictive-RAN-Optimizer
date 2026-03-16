import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class RANTemperaturePredictor:
    """
    Predictive Model for Ambient Temperature in RAN environments.
    Designed for embedded systems with limited computational resources.
    Inspired by research at LinkÃ¶ping University.
    """
    def __init__(self, n_estimators=100):
        self.model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)

    def generate_simulated_data(self, n_samples=1000):
        """
        Simulates RAN sensor data: CPU load, Signal Power, Time of Day, etc.
        """
        np.random.seed(42)
        cpu_load = np.random.rand(n_samples) * 100
        signal_power = np.random.rand(n_samples) * -120
        hour = np.random.randint(0, 24, n_samples)
        
        # Simulated target: Ambient Temperature with some noise
        temp = 20 + 0.1 * cpu_load + 2 * np.sin(2 * np.pi * hour / 24) + np.random.normal(0, 1, n_samples)
        
        X = np.stack([cpu_load, signal_power, hour], axis=1)
        return X, temp

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        preds = self.model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        print(f"Model trained. Mean Squared Error: {mse:.4f}")

    def predict(self, sensor_data):
        return self.model.predict(sensor_data)

if __name__ == "__main__":
    predictor = RANTemperaturePredictor()
    X, y = predictor.generate_simulated_data()
    predictor.train(X, y)
    
    # Test prediction: 85% CPU, -90dBm Power, Hour 14 (2 PM)
    test_input = np.array([[85, -90, 14]])
    predicted_temp = predictor.predict(test_input)
    print(f"Predicted Ambient Temperature: {predicted_temp[0]:.2f}Â°C")
