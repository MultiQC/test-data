SAMStat example output for the MultiQC samstat module
=====================================================

Written by SAMStat 2.4.0 (https://github.com/TimoLassmann/samstat, tag v2.4.0) with

    samstat -t 2 --json <input files>

The JSON report (format_version 2) is the file the module reads; the HTML reports were
deleted. The inputs are small synthetic test fixtures from SAMStat's repository (tests/data):

    small.sam.samstat.json          small.sam: 20 aligned single-end short reads
    paired_small.sam.samstat.json   paired_small.sam: paired-end reads (read 1 and read 2)
    ont_like.bam.samstat.json       longread/ont_like.bam: aligned ONT-like long reads
    hifi_like.sam.samstat.json      longread/hifi_like.sam: aligned PacBio HiFi-like long reads
    long.fq.samstat.json            longread/long.fq: unaligned long reads (FASTQ)
    reads.fa.gz.samstat.json        reads.fa.gz: unaligned reads (gzipped FASTA, no qualities)

Together they cover aligned and unaligned input, single and paired reads, short and long
reads, and input with and without base qualities.

They can be regenerated with packaging/multiqc/make_test_data.sh in the SAMStat repository.
