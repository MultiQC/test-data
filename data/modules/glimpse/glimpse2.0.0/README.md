## Results from GLIMPSE2_concordance

The files presented here are generated using the nf-core/phaseimpute pipeline.
The pipeline was run on the data from the 1000 Genomes Project, which is publicly available.
The pipeline was run using the default settings and the validate step.

This can be easily reproduce using the following command:

```bash
nextflow run nf-core/phaseimpute -profile test_validate,singularity --outdir results
```

The validation files are stored in the `results/validation/glimpse2` directory.

They are obtained by comparing two sets of vcf files:
- the "truth" variants called with `bcftools mpileup` and `bcftools call` from high depth data
- the imputed variants from downsampled data

The validation is performed using the `GLIMPSE2_concordance` tool from the [GLIMPSE2 software](https://odelaneau.github.io/GLIMPSE/).

```bash
wget https://raw.githubusercontent.com/nf-core/test-datasets/phaseimpute/data/individuals/NA12878/NA12878.s.bcf -O truthNA12878.bcf
wget https://raw.githubusercontent.com/nf-core/test-datasets/phaseimpute/data/individuals/NA12878/NA12878.s_imputed.bcf -O imputedNA12878.bcf
wget https://raw.githubusercontent.com/nf-core/test-datasets/phaseimpute/data/individuals/NA20359/NA20359.s.bcf -O truthNA20359.bcf
wget https://raw.githubusercontent.com/nf-core/test-datasets/phaseimpute/data/individuals/NA20359/NA20359.s_imputed.bcf -O imputedNA20359.bcf
wget https://raw.githubusercontent.com/nf-core/test-datasets/phaseimpute/data/panel/21_22/1000GP.chr21_22.s.norel.sites.bcf -O freq.bcf

bcftools merge truthNA12878.bcf truthNA20359.bcf -O b -o truth.bcf
bcftools merge imputedNA12878.bcf imputedNA20359.bcf -O b -o imputed.bcf

echo 'chr21 freq.bcf truth.bcf imputed.bcf' > input.txt
echo 'chr22 freq.bcf truth.bcf imputed.bcf' >> input.txt

GLIMPSE2_concordance \
    --out-r2-per-site \
    --input input.txt --min-val-gl 0.9 --min-val-dp 5 --bins 0 0.01 0.05 0.1 0.2 0.5 \
    --output validation
```

For the moment the files are in a compressed format and this not supported by MultiQC.
The files are uncompressed using the following command:

```bash
gunzip validation*
```