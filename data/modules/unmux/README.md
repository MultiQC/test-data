# unmux

Metrics files written by [unmux](https://github.com/clintval/unmux) 0.4.0 from simulated reads. They hold no
real data. Each read is an 8 bp sample barcode, a 6 bp library barcode (run1 only) and a random 60 bp insert.
The barcodes are random, with a poly-T spike-in barcode that `--remove` drops.

- run1: samples with sub-samples from a sample sheet, plus removed reads.
- run2.fq: no sample sheet and no `--pool`, so samples are named by barcode sequence and the pool by the
  input file name.
- run3: no samples, so reads pass through; its per-sample file is empty, as unmux writes it.
- run4: ten samples of uneven depth, two of them nearly empty.

The commands, with `barcodes.tsv` holding `id` and `seq` columns for bc01 to bc10 and spike:

```bash
metrics=(--metrics-per-sample %pool.unmux.per_sample.tsv --metrics-summary %pool.unmux.summary.tsv)

unmux run1.fq --pool run1 --group bc=barcodes.tsv --group bc::loc=0:0:8 \
  --group 'lib={lib01=CAGTCA,lib02=GTCAGT}' --group lib::loc=0:8:14 \
  --extract insert=0:14:end --template insert --sample-sheet samples.run1.tsv --remove bc::spike \
  --out '%pool.%sample.%sub_sample.fq' "${metrics[@]}"

unmux run2.fq --group 'bc={TAGGCTTC,CGAATCGT,AGTCGGTA}' --group bc::loc=0:0:8 \
  --extract insert=0:8:end --template insert --sample-from-group bc \
  --out '%pool.%sample.fq' "${metrics[@]}"

unmux run3.fq --pool run3 --group bc=barcodes.tsv --group bc::loc=0:0:8 \
  --extract insert=0:8:end --template insert --remove bc::spike \
  --out '%pool.fq' "${metrics[@]}"

unmux run4.fq --pool run4 --group bc=barcodes.tsv --group bc::loc=0:0:8 \
  --extract insert=0:8:end --template insert --sample-sheet samples.run4.tsv \
  --out '%pool.%sample.fq' "${metrics[@]}"
```

The run1 sample sheet pairs tumor and normal with bc01 and bc02 and with lib01 and lib02. The run4 sheet
names bc01 to bc10 as sampleA to sampleJ.
