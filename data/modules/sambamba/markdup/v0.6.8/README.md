Test output files for sambamba markdup (version `v0.6.8`) were generated from snakemake, but basic commands would be:

```bash
sambamba markdup -r -t {threads} --tmpdir=data/markd --io-buffer-size=512 {input} {output} > {log} 2>&1
```
