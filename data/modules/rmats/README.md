# rMATS test data

Real outputs from [rMATS-turbo](https://github.com/Xinglab/rmats-turbo), from four 75 bp paired-end
human RNA-seq samples (chromosome X subset, GBR and YRI populations) in the nf-core/rnasplice test
dataset. The reads were trimmed with Trim Galore and aligned with STAR.

## `nf-core_rnasplice`

From the nf-core/rnasplice `test` profile (rMATS v4.3.0, run with `--variable-read-length --allow-clipping`).

- `<sample>_read_outcomes_by_bam.txt`: one `rmats.py --task prep` per BAM, with
  `[datetime]_read_outcomes_by_bam.txt` copied out of `--tmp`.
- `<contrast>.rmats_summary.txt`: `summary.txt` from `rmats.py --task post` (with `--paired-stats`)
  for each contrast, renamed per contrast as the pipeline publishes it for MultiQC.

## `rmats_default_flags`

A plain rMATS v4.3.0 run on the same BAMs (renamed `GBR_rep1.bam` and so on), with rMATS defaults,
so without `--variable-read-length` or `--allow-clipping`:

```bash
rmats.py --b1 GBR_bamlist.txt --b2 YRI_bamlist.txt --gtf genes_chrX.gtf --readLength 75 \
    -t paired --libType fr-unstranded --nthread 4 --od GBR_vs_YRI --tmp GBR_vs_YRI_tmp
python rMATS_P/summary.py GBR_vs_YRI --summary-prefix GBR_vs_YRI/summary \
    --p-cutoff 0.1 --inc-level-diff-cutoff 0.05
```

- `GBR_vs_YRI_tmp/[datetime]_read_outcomes_by_bam.txt`: one file covering all four BAMs. Trimmed
  reads and STAR soft clipping make rMATS discard about 40% of the reads.
- `GBR_vs_YRI/summary.txt`: the default summary (FDR <= 0.05).
- `GBR_vs_YRI/summary_FDR_0.1_IncLevelDifference_0.05.txt`: a summary rewritten with other cutoffs.
