# 📈 Monte Carlo Option Pricing Engine

This repository contains a high-performance (vectorized) implementation of a Monte Carlo simulator to price European Options.

## 🧠 Mathematical Framework

### Geometric Brownian Motion (GBM)
We assume that the underlying asset price $S_t$ follows a Stochastic Differential Equation (SDE):

$$dS_t = r S_t dt + \sigma S_t dW_t$$

To simulate the price at maturity $T$, we use the analytical solution derived from **Itô's Lemma**:

$$S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)T + \sigma\sqrt{T}Z\right)$$

Where:
- $S_0$ is the current spot price.
- $r$ is the risk-free interest rate.
- $\sigma$ is the annualized volatility.
- $Z \sim N(0,1)$ is a random variable from the standard normal distribution.

### The Pricing Logic
The fair value of a Call Option is the discounted expected payoff under the risk-neutral measure:

$$C = e^{-rT} E[\max(S_T - K, 0)]$$

---

## 🛠️ Implementation Details
- **Engine:** Pure Python with optional NumPy vectorization.
- **Validation:** Benchmarked against the **Black-Scholes-Merton** closed-form solution.