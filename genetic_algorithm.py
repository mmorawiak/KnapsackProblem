import random

class GeneticAlgorithm:
    def __init__(self, knapsack, population_size=100, mutation_rate=0.01, generations=1000,
                 selection_method="tournament", crossover_method="two-point"):
        self.knapsack = knapsack
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population = self.initialize_population()
        self.fitness_cache = {}
        self.selection_method = selection_method
        self.crossover_method = crossover_method

    def initialize_population(self):
        return [[random.randint(0, 1) for _ in range(self.knapsack.size)] for _ in range(self.population_size)]

    def fitness(self, individual):
        individual_tuple = tuple(individual)
        if individual_tuple in self.fitness_cache:
            return self.fitness_cache[individual_tuple]

        total_value = sum(item[0] for i, item in enumerate(self.knapsack.items) if individual[i] == 1)
        total_weight = sum(item[1] for i, item in enumerate(self.knapsack.items) if individual[i] == 1)

        if total_weight > self.knapsack.capacity:
            penalty = (total_weight - self.knapsack.capacity) ** 2
            fitness_value = total_value - penalty
        else:
            fitness_value = total_value

        self.fitness_cache[individual_tuple] = fitness_value
        return fitness_value

    def select_tournament(self, tournament_size=5):
        tournament = random.sample(self.population, tournament_size)
        return max(tournament, key=self.fitness)

    def select_rank(self):
        sorted_population = sorted(self.population, key=self.fitness)
        ranks = list(range(1, len(sorted_population) + 1))
        total_rank = sum(ranks)
        selected = random.choices(sorted_population, weights=ranks, k=1)[0]
        return selected

    def crossover_one_point(self, parent1, parent2):
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:]

    def crossover_two_point(self, parent1, parent2):
        length = len(parent1)
        point1 = random.randint(1, length - 2)
        point2 = random.randint(point1, length - 1)
        return parent1[:point1] + parent2[point1:point2] + parent1[point2:]

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def run(self):
        best_values = []
        generations_list = []

        for generation in range(self.generations):
            new_population = []

            for _ in range(self.population_size // 2):
                if self.selection_method == "rank":
                    parent1 = self.select_rank()
                    parent2 = self.select_rank()
                else:
                    parent1 = self.select_tournament()
                    parent2 = self.select_tournament()

                if self.crossover_method == "two-point":
                    child1 = self.crossover_two_point(parent1, parent2)
                    child2 = self.crossover_two_point(parent2, parent1)
                else:
                    child1 = self.crossover_one_point(parent1, parent2)
                    child2 = self.crossover_one_point(parent2, parent1)

                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))

            self.population = new_population

            if (generation + 1) % 10 == 0:
                best_individual = max(self.population, key=self.fitness)
                best_value = self.fitness(best_individual)
                if best_value >= 0:
                    best_values.append(best_value)
                    generations_list.append(generation + 1)
                    print(f"Generation {generation + 1}/{self.generations} - Best Value: {best_value}")

        best_individual = max(self.population, key=self.fitness)
        best_value = self.fitness(best_individual)
        if best_value >= 0:
            best_values.append(best_value)
            generations_list.append(self.generations)

        return best_individual, best_value, generations_list, best_values
