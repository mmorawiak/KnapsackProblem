Algorytm Genetyczny dla Problemów Plecakowych

Opis projektu:

	Ten projekt implementuje algorytm genetyczny w celu rozwiązania problemu plecakowego (Knapsack Problem). 
	Algorytm genetyczny pozwala efektywnie przeszukiwać przestrzeń rozwiązań i znajdować wartości bliskie optymalnym, 
	nawet dla dużych i skomplikowanych zestawów danych.

Funkcjonalności:

	Rozwiązanie problemu plecakowego z ograniczeniem wagowym.
 
	Obsługa różnych metod selekcji: turniejowej i rankingowej.
 
	Wybór metody krzyżowania: jednopunktowego i dwupunktowego.
 
	Generowanie wykresów konwergencji algorytmu w czasie.
  
Struktura projektu:
Projekt składa się z następujących plików:

import_data.py:
    
	  Odpowiada za wczytywanie danych wejściowych (liczba przedmiotów, ich wartości, wagi oraz pojemność plecaka).
	  Tworzy obiekt Knapsack z informacjami o problemie.
    
genetic_algorithm.py:
  
	  Implementuje algorytm genetyczny.
	  Zawiera funkcje obsługujące populację, fitness, selekcję, krzyżowanie i mutację.

main.py:

	  Główna część programu.
	  Obsługuje wprowadzenie parametrów przez użytkownika.
	  Wywołuje algorytm genetyczny i generuje wyniki.

wyniki.txt:

	  Plik, w którym zapisywane są wyniki eksperymentów.


best_value_plot.png:

	  Wykres przedstawiający najlepszą wartość rozwiązania w kolejnych generacjach.

Wymagania:
  Do uruchomienia projektu potrzebne są:

	  Python 3.7+

	  Biblioteka matplotlib
  
  Aby zainstalować matplotlib, użyj polecenia:
  
    pip install matplotlib


Instrukcja uruchomienia:

1.Przygotuj dane wejściowe w pliku tekstowym, np. data.txt. Format pliku:

    liczba_przedmiotów pojemność_plecaka
    wartość_1 waga_1
    wartość_2 waga_2
    ...

2.Uruchom program:

    python main.py

3.Wprowadź wymagane parametry:

	  Ścieżka do pliku z danymi.
	 
	  Rozmiar populacji.
	 
	  Liczba pokoleń.
	 
	  Współczynnik mutacji.
	 
	  Metoda selekcji i krzyżowania.

4.Odczytaj wyniki:

	  Najlepsze rozwiązanie zostanie wyświetlone w konsoli.
	 
	  Wyniki zapisane zostaną w pliku wyniki.txt.
	 
	  Wygenerowany zostanie wykres best_value_plot.png.


Przykład użycia:
  Dla pliku example.txt o zawartości:

    5 50
    60 10
    100 20
    120 30

  Przykładowe parametry:
  
    Rozmiar populacji: 100
		
    Liczba pokoleń: 1000
		
    Współczynnik mutacji: 0.01
		
    Metoda selekcji: tournament
		
    Metoda krzyżowania: two-point

Uruchomienie programu zwróci najlepsze znalezione rozwiązanie oraz wykres przedstawiający proces konwergencji.



Autorzy:
	
  	Maciej Morawiak 51528
 	Alicja Żydek 49597






