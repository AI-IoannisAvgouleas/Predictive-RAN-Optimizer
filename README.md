# Predictive-RAN-Optimizer ðŸ›°ï¸ðŸ§ 
**AI-Driven Predictive Maintenance for Radio Access Networks (RAN)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![ML](https://img.shields.io/badge/Machine-Learning-green.svg)](https://github.com/AI-IoannisAvgouleas)
[![Research](https://img.shields.io/badge/PhD-Researcher-orange.svg)](https://github.com/AI-IoannisAvgouleas)

## **Project Overview**
**Predictive-RAN-Optimizer** is an industrial-scale framework designed to enhance the reliability and efficiency of **Radio Access Networks (RAN)** through **Predictive Artificial Intelligence**. 

Inspired by my research at **LinkÃ¶ping University**, this project implements a **Random Forest Regression** model to predict ambient temperatures in embedded RAN environments. By accurately forecasting temperature shifts based on CPU load and signal power, we can significantly extend hardware longevity and prevent network downtime in 5G/6G deployments.

---

## **Key Architecture**
The framework consists of two core analytical modules:
1.  **`RANTemperaturePredictor`**: A Machine Learning engine optimized for embedded environments with limited computational resources. It leverages feature importance analysis to maintain high precision with low overhead.
2.  **`OptimizationUtils`**: A suite of tools for **Industrial IoT (IIoT)**, including scaffolding for **Lagrangian Relaxation** applied to secure VPLS tunnel optimization and secrecy capacity estimation for heterogeneous traffic.

---

## **Features**
-   ðŸ“ˆ **Predictive Thermal Management**: Forecast ambient temperatures to trigger early maintenance or load balancing.
-   ðŸ”¡ **Secrecy Capacity Estimation**: Calculate information-theoretic secrecy for communication channels.
-   ðŸ§  **ML-Driven Optimization**: Optimize industrial networking tunnels (VPLS) for scalability and security.
-   ðŸ­ **Industrial Integration**: Focused on IIoT and RAN deployments where performance and reliability are paramount.

---

## **Installation**

Clone the repository and install dependencies:

```bash
git clone https://github.com/AI-IoannisAvgouleas/Predictive-RAN-Optimizer.git
cd Predictive-RAN-Optimizer
pip install -r requirements.txt
```

---

## **Example Usage**

```python
from ran_optimizer import RANTemperaturePredictor
from network_utils import OptimizationUtils
import numpy as np

# 1. Predictive Temperature Maintenance
predictor = RANTemperaturePredictor()
X, y = predictor.generate_simulated_data()
predictor.train(X, y)

# Predict for specific sensor reading [CPU Load, Signal Power, Hour]
test_sensor = np.array([[75, -95, 14]])
predicted_temp = predictor.predict(test_sensor)
print(f"Predicted Ambient Temp: {predicted_temp[0]:.2f}Â°C")

# 2. Network Secrecy Estimation
utils = OptimizationUtils()
secrecy = utils.estimate_secrecy_capacity(channel_gain=12, noise_power=0.4)
print(f"Channel Secrecy Capacity: {secrecy:.4f} bps/Hz")
```

---

## **Why This Project?**
This project represents a synthesis of my **Ph.D. Research** in Wireless Communications and **Machine Learning Industrialization**. By applying predictive AI to the physical and network layers, we can transition from reactive to proactive network management, ensuring the robustness of future connectivity infrastructures.

---

## **Connect & Contribute**
I am always open to collaborating on Wireless AI, IoT Security, and Network Optimization.

-   **LinkedIn:** [Ioannis Avgouleas, PhD](https://www.linkedin.com/in/dr-ioannis-avgouleas-15b6b85/)
-   **ResearchGate:** [Ioannis Avgouleas](https://www.researchgate.net/profile/Ioannis-Avgouleas)

---

> "Integrating intelligence into the physical layer to empower future networks."

---
*Disclaimer: This framework is a conceptual demonstration based on published research and academic simulations.*
