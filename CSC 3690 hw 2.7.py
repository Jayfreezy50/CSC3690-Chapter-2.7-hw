import random


def genetic_algorithm(population, fitness, generations=100, mutation_prob=0.05):
    for _ in range(generations):
        weights = [fitness(ind) for ind in population]
        population2 = []
        for _ in range(len(population)):
            parent1, parent2 = random.choices(population, weights, k=2)
            child = reproduce(parent1, parent2)
            if random.random() < mutation_prob:
                child = mutate(child)
            population2.append(child)
        population = population2
    return max(population, key=fitness)


def reproduce(parent1, parent2):
    c = random.randint(1, len(parent1))
    return parent1[:c] + parent2[c:]


def mutate(individual):
    i = random.randrange(len(individual))
    return individual[:i] + [1 - individual[i]] + individual[i + 1:]


if __name__ == "__main__":
    population = [[random.randint(0, 1) for _ in range(30)] for _ in range(50)]
    best = genetic_algorithm(population, sum)
    print(best, sum(best))