#import_data.py
class Knapsack:
    def __init__(self, file_path):
        """
        Inicjalizuje obiekt Knapsack, wczytując dane z pliku.

        :param file_path: Ścieżka do pliku z danymi
        """
        self.capacity = 0
        self.items = []
        self.size = 0
        self.load_data(file_path)

    def load_data(self, file_path):
        """
        Wczytuje dane z pliku i przypisuje je do atrybutów.

        :param file_path: Ścieżka do pliku z danymi
        """
        with open(file_path, 'r') as file:
            # Wczytaj wielkość problemu i pojemność
            first_line = file.readline().strip()
            self.size, self.capacity = map(int, first_line.split())

            # Wczytaj wartości i wagi przedmiotów
            for line in file:
                value, weight = map(int, line.strip().split())
                self.items.append((value, weight))

    def display_data(self):
        """
        Wyświetla wszystkie dane dotyczące plecaka.
        """
        print(f'Pojemność plecaka: {self.capacity}')
        print(f'Wielkość problemu: {self.size}')
        print('Przedmioty:')
        for idx, (value, weight) in enumerate(self.items, start=1):
            print(f'  Przedmiot {idx}: Wartość = {value}, Waga = {weight}')
