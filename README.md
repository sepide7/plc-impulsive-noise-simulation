🔬 PLC Impulsive Noise Simulation (OFDM-Based)

This project presents a simulation of an OFDM-based Power Line Communication (PLC) system under Bernoulli-Gaussian impulsive noise, which is a key challenge in PLC environments.

📌 Key Features
OFDM system with 64 subcarriers
QPSK modulation
Bernoulli-Gaussian impulsive noise modeling
AWGN background noise
Frequency-domain constellation analysis
⚙️ System Model
SNR (AWGN): 20 dB
SIR (Impulse): -10 dB
Impulse Probability: 0.1
📊 Results
Impulsive Noise (Time Domain)

Shows random high-energy spikes caused by impulsive noise.

Constellation Diagram

Demonstrates distortion of received symbols under PLC noise conditions.
▶️ How to Run
pip install -r requirements.txt
python src/simulation.py
📚 Related Work

This simulation is based on PLC channel modeling using Bernoulli-Gaussian noise, commonly used in recent literature for impulsive noise analysis.

👤 Author

PhD Student in Electrical and Electronics Engineering
Focused on PLC, signal processing, and machine learning