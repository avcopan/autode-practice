import autode as ade
import os

ade.Config.n_cores = 1

print("n_cores:", ade.Config.n_cores)
print("get_lmethod:", ade.methods.get_lmethod())
print("get_hmethod:", ade.methods.get_hmethod())

h2 = ade.Molecule(smiles='[H][H]')

h2.optimise(method=ade.methods.get_lmethod())

h2.optimise(method=ade.methods.get_hmethod())

print(h2.energy)
