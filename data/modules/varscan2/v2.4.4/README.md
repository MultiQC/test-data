
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
    2> sample1.lowfreq.varscan2.log \
    | bgzip -c > sample1.lowfreq.vcf.gz
tabix -p vcf -f sample1.lowfreq.vcf.gz
bcftools stats sample1.lowfreq.vcf.gz > sample1.lowfreq.bcftools_stats.txt
```

### Test files added

`sample1.lowfreq.varscan2.log` (Varscan 2 v2.4.4)

