# iVar Log Files

## `trim` log file

This has been generated from stdout so dont have a standard naming convention.

```bash
ivar trim \
    -i sample1.mapped.bam \
    -e \
    -b nCoV-2019.artic.V1.bed \
    -p sample1.trim > sample1.trim.ivar.log
```

### Test files added

`sample1.trim.ivar.log` (iVar v1.2)

## iVar `variants` file

Doesn't have a standard naming convention either.

```shell
samtools mpileup \
    -A \
    -d 6000000 \
    -B \
    -Q 0 \
    SAMPLE1_PE.trim.sorted.bam \
    | ivar variants -p SAMPLE1_PE -r GCF_009858895.2_ASM985889v3_genomic.200409.fna -g GCF_009858895.2_ASM985889v3_genomic.200409.gff
```

### Test files added

`sample1_pe_ivar_variants.tsv` (iVar v1.2.2) added.
