"""You can test your functions in this module as in the following code: """

from formula import *
from functions import *


formula1 = Atom('p')  # p
formula2 = Atom('q')  # q
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = And(Atom('p'), Atom('s'))  # (p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Not(Atom('q')), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(And(Not(Atom('p')), Atom('s')), And(Atom('q'), And(Not(Atom('p')), Atom('s'))))
formula9 = Not(Atom('p'))
# ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))

print(formula1 == formula3)
print(formula1 == formula2)
print(formula3 == And(Atom('p'), Atom('q')))

print('formula1:', formula1)
print('formula2:', formula2)
print('formula3:', formula3)
print('formula4:', formula4)
print('formula5:', formula5)
print('formula6:', formula6)
print('formula7:', formula7)
print('formula8:', formula8)
print('formula9:', formula9)
print('length of formula1:', length(formula1))
print('length of formula3:', length(formula3))

print('length of formula7:', length(formula7))

print('subformulas of formula7:')
print(formula7)

print('length of formula8:', length(formula8))
print('subformulas of formula8:')
print(formula8)


#  we have shown in class that for all formula A, len(subformulas(A)) <= length(A):
# for example, for formula8:
print('number of subformulas of formula8:', len(subformulas(formula8)))
print('len(subformulas(formula8)) <= length(formula8):', len(subformulas(formula8)) <= length(formula8))

print(atoms(formula8))
print(number_of_atoms(formula8))
print(number_of_connectives(formula8))

print('formula6:', formula9)
print(is_negation_normal_form(formula9))
print(substitution(Implies(And(Atom('p'), Not(Atom('q'))), Atom('r')), Not(Atom('q')), Or(Atom('r'), Atom('t'))))
print(formula8)
print(substitution(formula8, And(Not(Atom('p')), Atom('s')), Atom('h')))