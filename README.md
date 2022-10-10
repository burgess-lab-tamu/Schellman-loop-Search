# Schellman-loop-Search
Search and analyse Schellman loops datamined from PDB

## Usage

database

Schellman loop Finder Database<br />
  The database can be found:<br />
    [Schellman loop Finder Database](https://www.dropbox.com/s/8donclg9uwzjl0k/Schellman%20loop%20Finder%20Database.csv?dl=0)<br />
  what it includes:<br />
    include all Schellman loops in PDB till Nov. 2020<br />
    search Schellman loops in any interesting csyrtal by typing in its PDB code<br />
    get extra structural information, such as sequence, dihedrals, secondary structures and at interface or not<br />
nonredundant Schellman loops<br />
  Schellman loops obtained from unique chains<br />
  Most useful for statistical analyses<br />
hot Schellman loops<br />
  interface Schellman loops that are important to binding<br />
hydrophobic patterns of Schellman loops<br />
  includes hydrophobic patterns of common α-helical Schellman loops, wide α-helical and π-helical Schellman loops<br />




Scripts
Schellman_informatics.ipynb can do basic statistical analyses of any Schellman loop databases, providing structural and statistical information
sasa_Schellman.py can calculate solvent-accessible surface areas of any given Schellman loop and help decide if it is a hot loop or not
count_hydrophobic_common and _wide.py can calculate hydrophobic patterns based on closest distance between sidechains


## Citation

to be published
