import numpy as np

# Liczba iteracji eksperymentu
n_iterations = 100

# Liczba danych w próbce
n_data = 2 * n_iterations + 1

# Pusta lista do przechowywania błędów średniokwadratowych dla próbkowej średniej
mse_mean_estimate = []

# Pusta lista do przechowywania błędów średniokwadratowych dla próbkowej mediany
mse_median_estimate = []

# Powtórz eksperyment n_iterations razy
for _ in range(n_iterations):
    # Wygeneruj próbkę z rozkładu normalnego
    sample = np.random.normal(loc=0, scale=1, size=n_data)
    
    # Oblicz estymator próbkowej średniej
    mean_estimate = np.mean(sample)
    
    # Oblicz estymator próbkowej mediany
    median_estimate = np.median(sample)
    
    # Oblicz błąd średniokwadratowy dla próbkowej średniej
    mse_mean = (mean_estimate - 0)**2
    
    # Oblicz błąd średniokwadratowy dla próbkowej mediany
    mse_median = (median_estimate - 0)**2
    
    # Dodaj błędy średniokwadratowe do list
    mse_mean_estimate.append(mse_mean)
    mse_median_estimate.append(mse_median)

# Oblicz średnią z błędów średniokwadratowych dla próbkowej średniej
mean_mse_mean_estimate = np.mean(mse_mean_estimate)

# Oblicz średnią z błędów średniokwadratowych dla próbkowej mediany
mean_mse_median_estimate = np.mean(mse_median_estimate)

# Wyświetl wyniki
print("Średni błąd średniokwadratowy dla próbkowej średniej:", mean_mse_mean_estimate)
print("Średni błąd średniokwadratowy dla próbkowej mediany:", mean_mse_median_estimate)