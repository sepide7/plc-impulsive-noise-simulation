# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:52:54 2026

@author: sepid
"""
import numpy as np
import matplotlib.pyplot as plt

# --- System Parameters ---
num_subcarriers = 64  # Number of OFDM subcarriers
snr_db = 20           # Signal-to-Noise Ratio for background noise (AWGN)
p_impulsive = 0.1     # Probability of impulsive noise occurrence (Bernoulli)
sir_db = -10          # Signal-to-Impulse Ratio (representing strong interference)

# 1. Random Data Generation (QPSK Modulation)
data_bits = np.random.randint(0, 2, num_subcarriers * 2)
symbols = (2 * data_bits[::2] - 1) + 1j * (2 * data_bits[1::2] - 1)

# 2. Transition to Time Domain (IFFT)
time_domain_signal = np.fft.ifft(symbols)

# 3. Bernoulli-Gaussian Noise Modeling (Main PLC Challenge)
# Background Noise (Gaussian)
std_awgn = np.sqrt(10**(-snr_db/10))
awgn_noise = (np.random.normal(0, std_awgn, num_subcarriers) + 
              1j * np.random.normal(0, std_awgn, num_subcarriers))

# Impulsive Noise Modeling
std_impulsive = np.sqrt(10**(-sir_db/10))
bernoulli_trigger = np.random.binomial(1, p_impulsive, num_subcarriers)
impulsive_noise = bernoulli_trigger * (np.random.normal(0, std_impulsive, num_subcarriers) + 
                                       1j * np.random.normal(0, std_impulsive, num_subcarriers))

# Received signal in the power line network environment
received_signal = time_domain_signal + awgn_noise + impulsive_noise

# 4. Transition back to Frequency Domain (FFT)
received_symbols = np.fft.fft(received_signal)

# --- Result Visualization ---
plt.figure(figsize=(12, 5))

# Plot Impulsive Noise in Time Domain
plt.subplot(1, 2, 1)
plt.stem(np.abs(impulsive_noise), linefmt='r-', markerfmt='ro', basefmt=' ')
plt.title("Impulsive Noise (Bernoulli-Gaussian)")
plt.xlabel("Sample Index")
plt.ylabel("Magnitude")

# Plot Constellation Diagram showing noise impact
plt.subplot(1, 2, 2)
plt.scatter(received_symbols.real, received_symbols.imag, color='blue', label='Received Symbols')
plt.scatter(symbols.real, symbols.imag, color='red', marker='x', s=100, label='Transmitted Symbols')
plt.title("Constellation Diagram (Effect of PLC Noise)")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()