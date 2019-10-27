import networkx
import sys
import os
import argh
import pathlib

def count_char_from_left(xs, c):
    result = 0
    for x in xs:
        if x != c:
            return result
        else:
            result = result + 1
    return result

def go(org_filepath):
    labels = list()
    max_level = 0
    for line in open(org_filepath).readlines():
        line2 = line.strip()
        if line2 and line2[0] == '*':
            label = line2.replace('*', '').strip()
            level = count_char_from_left(line2, '*')
            labels.append([level, label])
            if level > max_level:
                max_level = level
    
    edges = list()
    prev_label = None
    for prev_level in range(1, max_level + 1):
        for [level, label] in labels:
            if not prev_label:
                prev_label = label
            else:
                if level == prev_level + 1:
                    edges.append([prev_label, label])
                if level == prev_level:
                    prev_label = label

    G = networkx.Graph()
    G.add_edges_from(edges)

    basename = pathlib.Path(org_filepath).name
    networkx.drawing.nx_pydot.write_dot(G, f'{basename}.dot')

    os.system(f"sfdp -Tpng {basename}.dot -o {basename}.png")
    try:
        os.system(f"feh {basename}.png")
    except:
        sys.stderr.write("Couldn't open image with feh")

if __name__ == '__main__':
    argh.dispatch_command(go)
