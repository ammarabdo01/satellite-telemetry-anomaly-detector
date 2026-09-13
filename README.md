# Satellite Telemetry Anomaly Detector

A student-scale machine learning pipeline designed to identify unusual temperature, voltage, and sensor telemetry patterns from satellite data.

## Features
- **Data Simulation:** Generates synthetic satellite sensor metrics (Temperature, Voltage, Current).
- **Anomaly Detection:** Utilizes an `Isolation Forest` unsupervised learning algorithm to flag sensor spikes and drops.
- **Pipeline Structure:** Clean separation between data generation, model training, and execution.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ammarabdo01/satellite-telemetry-anomaly-detector.git](https://github.com/ammarabdo01/satellite-telemetry-anomaly-detector.git)
   cd satellite-telemetry-anomaly-detector
   
