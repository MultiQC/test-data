Data from <https://github.com/ewels/MultiQC/issues/737>

Description:

For completeness below the code used to run the TIN module, and the results have been attached. (the txt file `*out.summary.txt` contains the summary of the sample (i.e. median + SD), the xls [actually, also a tab delim txt] file `*out.tin.xls` the TIN score per transcript).

```console
[guidoh@localhost P15-1-6h]$ tin.py -i P15-1-6h_Aligned.sortedByCoord.out.bam -r /mnt/files/guido/INDEX/STAR/Housekeeping_TranscriptsHuman2158.bed
@ 2021-06-10 11:44:04: Get BAM file(s) ...
Total 1 BAM file(s):
        P15-1-6h_Aligned.sortedByCoord.out.bam
@ 2021-06-10 11:44:04: Processing P15-1-6h_Aligned.sortedByCoord.out.bam
[guidoh@localhost P15-1-6h]$
```
