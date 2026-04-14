- **Modulation:** QPSK  
- **Number of subcarriers:** 64  
- **SNR (AWGN):** 20 dB  
- **SIR (Impulsive Noise):** -10 dB  
- **Impulse Probability:** 0.1  

---

## 🧠 Key Features

- OFDM signal generation using IFFT/FFT  
- QPSK modulation  
- Bernoulli-Gaussian impulsive noise modeling  
- Combination of AWGN + impulsive noise  
- Frequency-domain constellation analysis  
- Visualization of noise behavior in time domain  

---

## 📁 Project Structure


plc-impulsive-noise-simulation/
│
├── src/
│ └── plc_impulsive_noise_simulation.py
│
├── results/
│ ├── impulsive_noise.png
│ └── constellation.png
│
├── README.md
├── requirements.txt
└── .gitignore


---

## 📊 Simulation Results

### 🔹 Impulsive Noise (Time Domain)
High-energy spikes appear randomly due to impulsive noise in PLC channels.

### 🔹 Constellation Diagram
The received symbols are distorted compared to transmitted symbols due to noise effects.

![Constellation](results/constellation.png)

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
Run the simulation:
python src/plc_impulsive_noise_simulation.py
🎯 Contribution

This project provides a simple and reproducible implementation of impulsive noise modeling in PLC systems using a Bernoulli-Gaussian approach.
It can be used for:

Research and benchmarking
Understanding PLC noise behavior
Educational purposes in communication systems
📚 Related Work

This simulation is based on widely used Bernoulli-Gaussian models in PLC literature for impulsive noise characterization.

👤 Author

PhD Student in Electrical and Electronics Engineering
Research Interests:

Power Line Communication (PLC)
Signal Processing
Machine Learning
⭐ Notes
This project is part of a broader study on PLC vs Talkative Power Conversion (TPC)
Future work may include:
Channel modeling extensions
Deep learning-based noise mitigation
Hybrid PLC-TPC systems