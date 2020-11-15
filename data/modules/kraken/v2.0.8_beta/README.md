
## Kraken2 report files generated using `--report` parameter

```bash
kraken2 \
    --db kraken2_human \
    --threads 12 \
    --unclassified-out sample1.viral#.fastq \
    --classified-out sample1.host#.fastq \
    --report sample1.kraken2.report.txt \
    --paired \
    --gzip-compressed \
    sample1_1.ptrim.fastq.gz sample1_2.ptrim.fastq.gz
pigz -p 12 *.fastq
```

### Test files added

`sample1.kraken2.report.txt` (Kraken2 v2.0.8_beta using [human database](https://zenodo.org/record/3738199/files/kraken2_human.tar.gz))
`sample1.kraken2.report` (Kraken2 v2.0.8_beta using [viral database](https://zenodo.org/record/3741444/files/kraken2_viral.tar.gz))
