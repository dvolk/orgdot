# orgdot

## Description

Turn org-mode headers into a graph using networkx and graphviz

## Requirements

- python 3.6+
- graphviz
- python3-networkx
- python3-argh

## Installation example

    git clone https://github.com/dvolk/orgdot.git
    cd orgdot
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install networkx argh
    
## Use example

    python main.py stem.txt 

## Example

    * STEM
    ** Biology
    *** Zoology
    *** Microbiology
    *** Genetics
    *** Ecology
    ** Chemistry
    *** Analytical Chemistry
    *** Physical chemistry
    *** Biochemistry
    ** Physics
    *** Mechanics
    **** Orbital mechanics
    *** Thermodynamics
    *** Electrodynamics
    *** Materials science
    
->

![Example](https://raw.githubusercontent.com/dvolk/orgdot/master/stem.txt.png)
