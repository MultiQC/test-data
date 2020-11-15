---
Name: odgi
URL: https://github.com/vgteam/odgi
Description: >
    is an optimized dynamic graph/genome implementation.
---

The [odgi stats](https://pangenome.github.io/odgi/odgi_docs.html#_odgi_stats1) reports were generated with default run parameters.

```bash
odgi stats \
    -i  
```

All reports must adhere to the following structure (as automatically done by [odgi stats](https://pangenome.github.io/odgi/odgi_docs.html#_odgi_stats1)):

```ts
length    nodes    edges    paths
8778    168    243    35
#mean_links_length
path    in_node_space    in_nucleotide_space    num_links_considered
all_paths    9.75053    497.321    942
#sum_of_path_node_distances
path    in_node_space    in_nucleotide_space    nodes    nucleotides    num_penalties    num_penalties_different_orientation
all_paths    20.0686     19.5609    977     51365     90    0
```

### Test files added

`*.consensus@[100-1000000].gfa.stats` (odgi stats v0.4.1 using []())
`*.seqwish.og.stats` (odgi stats v0.4.1 using []())
`*.smooth.og.stats` (odgi stats v0.4.1 using []())
