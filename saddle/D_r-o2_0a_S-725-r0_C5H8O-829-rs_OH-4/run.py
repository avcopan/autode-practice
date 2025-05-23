import autode as ade
import os

ade.Config.n_cores = 8

print("n_cores:", ade.Config.n_cores)
print("get_lmethod:", ade.methods.get_lmethod())
print("get_hmethod:", ade.methods.get_hmethod())

rxn = ade.Reaction('OO[C@H]1C[CH]CC1>>C1C[C@@H]2C[C@H]1O2.[OH]')

rxn.calculate_reaction_profile()
