from import_data import Knapsack
from genetic_algorithm import GeneticAlgorithm
import time
import matplotlib.pyplot as plt

def plot_best_value(generations, best_values, knapsack, population_size, generations_count, mutation_rate, best_value):
    plt.figure(figsize=(10, 5))
    plt.plot(generations, best_values, marker='o', color='b')
    plt.title('Najlepsza wartość rozwiązania w czasie')
    plt.xlabel('Pokolenie')
    plt.ylabel('Najlepsza wartość')
    plt.grid(True)

    params = (
        f"Pojemność plecaka: {knapsack.capacity}, Populacja: {population_size}, "
        f"Generacje: {generations_count}, Mutacja: {mutation_rate}, Najlepsza wartość: {best_value}"
    )
    plt.figtext(0.5, 0.01, params, wrap=True, horizontalalignment='center', fontsize=10)
    plt.savefig('best_value_plot.png')
    plt.show()

def main():
    file_path = input("Podaj ścieżkę do pliku z danymi: ")
    population_size = int(input("Podaj rozmiar populacji (domyślnie 100): ") or 100)
    generations = int(input("Podaj liczbę pokoleń (domyślnie 1000): ") or 1000)
    mutation_rate = float(input("Podaj współczynnik mutacji (domyślnie 0.01): ") or 0.01)
    selection_method = input("Wybierz metodę selekcji (tournament/rank): ").strip().lower() or "tournament"
    crossover_method = input("Wybierz metodę krzyżowania (one-point/two-point): ").strip().lower() or "two-point"

    try:
        knapsack = Knapsack(file_path)
        knapsack.display_data()

        ga = GeneticAlgorithm(
            knapsack,
            population_size=population_size,
            mutation_rate=mutation_rate,
            generations=generations,
            selection_method=selection_method,
            crossover_method=crossover_method
        )

        start_time = time.time()
        best_solution, best_value, generations_list, best_values = ga.run()
        elapsed_time = time.time() - start_time

        print(f'Najlepsze rozwiązanie: {best_solution} z wartością: {best_value}')
        print(f'Czas wykonania: {elapsed_time:.2f} sekund')

        with open('wyniki.txt', 'a') as results_file:
            results_file.write(f'Pojemnosc plecaka: {knapsack.capacity},')
            results_file.write(f'Wielkosc problemu: {len(knapsack.items)},')
            results_file.write(f'Rozmiar populacji: {population_size},')
            results_file.write(f'Liczba pokolen: {generations},')
            results_file.write(f'Wspolczynnik mutacji: {mutation_rate},')
            results_file.write(f'Selekcja: {selection_method}, Krzyzowanie: {crossover_method}, ')
            results_file.write(f'Wartosc najlepszego rozwiazania: {best_value},\n---\n')

        plot_best_value(generations_list, best_values, knapsack, population_size, generations, mutation_rate, best_value)

    except FileNotFoundError:
        print("Nie znaleziono pliku. Sprawdź, czy ścieżka jest poprawna.")
    except ValueError as e:
        print(f"Wystąpił błąd przy wczytywaniu danych: {e}")

if __name__ == "__main__":
    main()
