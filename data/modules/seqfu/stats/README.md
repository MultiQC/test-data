# seqfu stats testdata

Testdata from nf-core/test-datasets (seqinspector, commit 46faf74)

```
git clone https://github.com/nf-core/test-datasets.git -b seqinspector nfcore-test-datasets-seqinspector --depth 1
```

Seqfu commands

```
NF_TESTDATA="path/to/nfcore-test-datasets-seqinspector"

docker run --rm -v $NF_TESTDATA/full_tests/MiSeq_PairedEnd/Fastq:/data 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "seqfu stats data/*fastq.gz" > paired_end.tsv

docker run --rm -v $NF_TESTDATA/full_tests/MiSeq_SingleEnd/Fastq:/data 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "seqfu stats data/*fastq.gz" > single_end.tsv

docker run --rm -v $NF_TESTDATA/full_tests/MiSeq_SingleEnd/Fastq:/data 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "seqfu stats --gc data/*fastq.gz" > single_end_gc.tsv

docker run --rm -v $NF_TESTDATA/testdata/PromethION/20230505_1857_1B_PAO99309_94e07fab/fastq_pass:/data 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "seqfu stats data/*fastq.gz" > promethion_pass.tsv

docker run --rm -v $NF_TESTDATA/testdata/PromethION/20230505_1857_1B_PAO99309_94e07fab/fastq_fail:/data 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "seqfu stats data/*fastq.gz" > promethion_fail.tsv

# From stdin
docker run --rm -v $NF_TESTDATA/testdata/PromethION/20230505_1857_1B_PAO99309_94e07fab/fastq_pass:/data 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "zcat data/*.fastq.gz | seqfu stats" > promethion_pass_stdin.tsv

# Empty
docker run --rm 'quay.io/biocontainers/seqfu:1.20.3--h1eb128b_0' /bin/bash -c "seqfu stats" > empty.tsv
```

