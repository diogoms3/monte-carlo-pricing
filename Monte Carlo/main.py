import math
import random

# 1. Parâmetros (Input manual)
S0 = 100.0    # Preço inicial do ativo
K = 105.0     # Strike
T = 1.0       # Tempo (1 ano)
r = 0.12      # Taxa (12%)
sigma = 0.30  # Volatilidade (30%)
n = 100000    # Número de simulações (O quanto seu PC aguentar)

soma_payoffs = 0

# Função para a Distribuição Normal Acumulada (N(x))
def norm_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

# --- Cálculo de Black-Scholes ---
d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
d2 = d1 - sigma * math.sqrt(T)

bs_price = S0 * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)

# 2. Loop de Simulação (Força Bruta)
for _ in range(n):
    # Gera um número aleatório da Normal Padrão Z ~ N(0,1)
    Z = random.gauss(0, 1)
    
    # Fórmula do Movimento Browniano Geométrico (GBM)
    ST = S0 * math.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z)
    
    # Payoff da Call: max(ST - K, 0)
    payoff = max(ST - K, 0)
    soma_payoffs += payoff

# 3. Média e Desconto a Valor Presente
preco_opcao = (soma_payoffs / n) * math.exp(-r * T)

# --- Comparação Final ---
print(f"Preço Monte Carlo: {preco_opcao:.4f}")
print(f"Preço Black-Scholes: {bs_price:.4f}")
print(f"Erro Absoluto: {abs(preco_opcao - bs_price):.6f}")