
## Varscan2 log file generated from `mpileup2cns` stderr so dont have a standard naming convention

```bash
samtools mpileup \
    --count-orphans \
    --max-depth 20000 \
    --min-BQ 0 \
    --fasta-ref GCF_009858895.2_ASM985889v3_genomic.200409.fna \
    sample1.trim.sorted.bam \
    > sample1.pileup

varscan mpileup2cns \
    sample1.pileup \
    --min-var-freq 0.02 \
    --p-value 0.99 \
    --variants \
    --output-vcf 1 \
    2> sample1.lowfreq.varscan2.mpileup2cns.log \
    | bgzip -c > sample1.lowfreq.vcf.gz
tabix -p vcf -f sample1.lowfreq.vcf.gz
bcftools stats sample1.lowfreq.vcf.gz > sample1.lowfreq.bcftools_stats.txt
```

### Test files added

`sample1.lowfreq.varscan2.mpileup2cns.log` (Varscan 2 v2.4.4 `mpileup2cns` mode)

## Varscan2 log file generated from `mpileup2snp` stderr so dont have a standard naming convention

```bash
samtools mpileup \
    --count-orphans \
    --max-depth 20000 \
    --min-BQ 0 \
    --fasta-ref GCF_009858895.2_ASM985889v3_genomic.200409.fna \
    SAMPLE1_PE.trim.sorted.bam \
    > SAMPLE1_PE.pileup

varscan mpileup2snp \
    SAMPLE1_PE.pileup \
    --min-var-freq 0.02 \
    --p-value 0.99 \
    --variants \
    --output-vcf 1 \
    2> SAMPLE1_PE.lowfreq.varscan2.mpileup2snp.log \
    | bgzip -c > SAMPLE1_PE.lowfreq.vcf.gz
tabix -p vcf -f SAMPLE1_PE.lowfreq.vcf.gz
bcftools stats SAMPLE1_PE.lowfreq.vcf.gz > SAMPLE1_PE.lowfreq.bcftools_stats.txt
```

### Test files added

`SAMPLE1_PE.lowfreq.varscan2.mpileup2snp.log` (Varscan 2 v2.4.4 `mpileup2snp` mode)

## Varscan2 log file generated from `mpileup2indel` stderr so dont have a standard naming convention

```bash
samtools mpileup \
    --count-orphans \
    --max-depth 20000 \
    --min-BQ 0 \
    --fasta-ref GCF_009858895.2_ASM985889v3_genomic.200409.fna \
    SRR11140750.sorted.bam \
    > SRR11140750.pileup

varscan mpileup2indel \
    SRR11140750.pileup \
    --min-var-freq 0.02 \
    --p-value 0.99 \
    --variants \
    --output-vcf 1 \
    2> SRR11140750.lowfreq.varscan2.mpileup2indel.log \
    | bgzip -c > SRR11140750.lowfreq.vcf.gz
tabix -p vcf -f SRR11140750.lowfreq.vcf.gz
bcftools stats SRR11140750.lowfreq.vcf.gz > SRR11140750.lowfreq.bcftools_stats.txt
```

### Test files added

`SRR11140750.lowfreq.varscan2.mpileup2indel.log` (Varscan 2 v2.4.4 `mpileup2cns` mode)
