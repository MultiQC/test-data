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

## Unassigned reasons

Pools run5 and run6 add the `--metrics-unassigned` file, which counts the unassigned reads of a pool by reason.
They come from the unmux release that added that flag, run on simulated reads that hold no real data. Each read
is an 8 bp round 1 barcode, a 12 bp linker, an 8 bp round 2 barcode, an 8 bp round 3 barcode and a random
insert. A set share of reads carries one fault each: a round 1, round 2 or round 3 barcode with 3 errors, a
linker with 4 errors, a second round 3 barcode, or the one round 1 barcode no sample claims. run6 has more
linker and round 2 faults than run5. The sample sheets give the round 1 barcodes bc01 to bc04 to well01 to
well04 in run5 and well05 to well08 in run6, leaving bc05 unclaimed.

```bash
for pool in run5 run6; do
  unmux $pool.fq --pool $pool \
    --group round1=round1.tsv --group round1::loc=0:0:8,dist=1,minFindsPerGroup=1,maxFindsPerGroup=1 \
    --group 'linker={L=GTGGCCGATGTT}' --group linker::loc=0:8:20,dist=2,minFindsPerGroup=1 \
    --group round2=round2.tsv --group round2::loc=0:20:28,dist=1,minFindsPerGroup=1,maxFindsPerGroup=1 \
    --group round3=round3.tsv --group round3::loc=0:28:44,dist=1,minFindsPerGroup=1,maxFindsPerGroup=1 \
    --extract insert=0:36:end --template insert \
    --sample-sheet samples.$pool.tsv \
    --out '%pool.%sample.fq' "${metrics[@]}" --metrics-unassigned %pool.unmux.unassigned.tsv
done
```
