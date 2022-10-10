# Schellman-loop-Search
Search and analyse Schellman loops datamined from PDB

## Usage

database
```
Schellman loop Finder
  The database can be found:
    https://www.dropbox.com/s/8donclg9uwzjl0k/Schellman%20loop%20Finder%20Database.csv?dl=0
  what it includes:
    include all Schellman loops in PDB till Nov. 2020
    search Schellman loops in any interesting csyrtal by typing in its PDB code
    get extra structural information, such as sequence, dihedrals, secondary structures and at interface or not
nonredundant Schellman loops
  Schellman loops obtained from unique chains
  Most useful for statistical analyses
hot Schellman loops
  interface Schellman loops that are important to binding
hydrophobic patterns of Schellman loops
  includes hydrophobic patterns of common α-helical Schellman loops, wide α-helical and π-helical Schellman loops
```



Scripts
```
Schellman_informatics.ipynb can do basic statistical analyses of any Schellman loop databases, providing structural and statistical information
sasa_Schellman.py can calculate solvent-accessible surface areas of any given Schellman loop and help decide if it is a hot loop or not
count_hydrophobic_common and _wide.py can calculate hydrophobic patterns based on closest distance between sidechains
```

## Citation

to be published
