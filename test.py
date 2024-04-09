import numpy as np

# Funkcja obliczająca wartość średnią dla rozkładu lognormalnego
def lognormal_mean(mu, sigma):
    return np.exp(mu + sigma**2 / 2)

# Parametry rozkładu lognormalnego
mu = 0.5  # średnia logarytmu
sigma = 0.3  # odchylenie standardowe logarytmu

# Wartość oczekiwana (średnia) dla rozkładu lognormalnego
mean_lognormal = lognormal_mean(mu, sigma)
print("Średnia dla rozkładu lognormalnego:", mean_lognormal)

# Liczba próbek w próbie
n = 10000

# Generowanie próby z rozkładu lognormalnego
lognormal_samples = np.random.lognormal(mu, sigma, n)

# Średnia z próby
sample_mean = np.mean(lognormal_samples)
print("Średnia z próby:", sample_mean)

# Sprawdzenie, czy średnia z próby jest nieobciążonym estymatorem parametru średniej
# Wykonujemy wielokrotnie symulację prób i obliczamy średnią z prób
num_simulations = 1000
sample_means = np.zeros(num_simulations)
for i in range(num_simulations):
    sample = np.random.lognormal(mu, sigma, n)
    sample_means[i] = np.mean(sample)

# Obliczamy odchylenie standardowe średnich z prób
std_sample_means = np.std(sample_means)

print("Średnia z prób:", np.mean(sample_means))
print("Odchylenie standardowe średnich z prób:", std_sample_means)