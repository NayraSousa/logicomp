"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from formula import *


def length(formula: Formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula: Formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    conjunto = set()

    if isinstance(formula, Atom):
        conjunto.add(formula)
    if isinstance(formula, Not):
        conjunto.update(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        conjunto.update(subformulas(formula.left))
        conjunto.update(subformulas(formula.right))

    return conjunto

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula: Formula):
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """

    conjunto = set()

    if isinstance(formula, Atom):
        conjunto.add(formula.name)

    if isinstance(formula, Not):
        conjunto.update(atoms(formula.inner))

    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        conjunto.update(atoms(formula.left))
        conjunto.update(atoms(formula.right))

    return conjunto


def number_of_atoms(formula: Formula):
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """
    
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_atoms(formula.left) + number_of_atoms(formula.right)

def number_of_connectives(formula: Formula):
    """Returns the number of connectives occurring in a formula."""

    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return 1 + number_of_connectives(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return 1 + number_of_connectives(formula.left) + number_of_connectives(formula.right)


def is_literal(formula: Formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def substitution(formula: Formula, old_subformula: Formula, new_subformula: Formula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_clause(formula: Formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_negation_normal_form(formula: Formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_cnf(formula: Formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_term(formula: Formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula: Formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula: Formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
