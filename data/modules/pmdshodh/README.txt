pmdshodh JSON run summaries, for the MultiQC pmdshodh module.

Each summary was written by pmdshodh (https://github.com/dpatel511/pmdshodh),
installed from PyPI, run in a directory holding the input BAM:

JK2067.pmdshodh.json                 pmdshodh 0.3.3, format_version 4
    pmdshodh filter --threshold 3 --summary JK2067.pmdshodh.json --quiet JK2067.bam -o JK2067.pmd3.bam
JK2067.score.pmdshodh.json           pmdshodh 0.3.3, format_version 4
    pmdshodh score --summary JK2067.score.pmdshodh.json --quiet JK2067.bam -o JK2067.scores.tsv
JK2067.damage.v0.1.0.pmdshodh.json   pmdshodh 0.1.0, format_version 1
    pmdshodh damage --quiet JK2067.bam -o JK2067.damage.v0.1.0.pmdshodh.json
UKY001.B0102.MT.pmdshodh.json        pmdshodh 0.3.3, format_version 4, single-stranded library
    pmdshodh filter --threshold 3 --library ss --summary UKY001.B0102.MT.pmdshodh.json --quiet UKY001.B0102.MT.bam -o UKY001.B0102.MT.pmd3.bam

Inputs:
- JK2067.bam: nf-core/test-datasets, branch eager, testdata/Human/bam/JK2067.bam
  (human, double-stranded; 125,285 reads).
- UKY001.B0102.MT.bam: ENA run ERR3991018 (project PRJEB37007), mtDNA BAM of a
  single-stranded library without UDG treatment (281,906 reads).

The three JK2067 summaries share one input, so they test how the module names
samples when two summaries come from the same BAM.
