import autode as ade
import os

ade.Config.n_cores = 8

print("n_cores:", ade.Config.n_cores)
print("get_lmethod:", ade.methods.get_lmethod())
print("get_hmethod:", ade.methods.get_hmethod())

rxn = ade.Reaction('C=CC=C.C=C>>C1=CCCCC1', name='DA')

rxn.calculate_reaction_profile()
