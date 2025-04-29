import numpy as np

def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

def fuzzy_difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in A}

def cartesian_product(A, B):
    return {(a, b): min(A[a], B[b]) for a in A for b in B}

def max_min_composition(R, S):
    result = {}
    for (x, y) in R:
        for (y2, z) in S:
            if y == y2:
                result[(x, z)] = max(result.get((x, z), 0), min(R[(x, y)], S[(y2, z)]))
    return result

def print_fuzzy_set(title, fuzzy_set):
    print(f"\n{title}:")
    for key, value in fuzzy_set.items():
        print(f"  {key}: {value:.2f}")

# Example fuzzy sets
A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.7}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.8}
C = {'y1': 0.3, 'y2': 0.9}

# Performing operations
union_result = fuzzy_union(A, B)
intersection_result = fuzzy_intersection(A, B)
complement_result = fuzzy_complement(A)
difference_result = fuzzy_difference(A, B)

# Fuzzy relations
R = cartesian_product(A, C)
S = cartesian_product(C, B)
composition_result = max_min_composition(R, S)

# Display results neatly
print_fuzzy_set("Union", union_result)
print_fuzzy_set("Intersection", intersection_result)
print_fuzzy_set("Complement", complement_result)
print_fuzzy_set("Difference", difference_result)
print_fuzzy_set("Cartesian Product (Relation R)", R)
print_fuzzy_set("Cartesian Product (Relation S)", S)
print_fuzzy_set("Max-Min Composition (R ∘ S)", composition_result)
