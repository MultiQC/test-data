Test data for the FastDup module

These metrics files support the module in MultiQC/MultiQC#3707.

issue-3621.stats.txt
- Original FastDup metrics attachment to MultiQC/MultiQC#3621:
  https://github.com/MultiQC/MultiQC/issues/3621
  https://github.com/user-attachments/files/30896575/stats.txt
- Line endings and the final newline are normalized in the existing module test fixture.
- SHA-256: c17043951f0afed0877b9f06c717050c7bb36fe9454f2bc811624ef1c314da08

NA12878.fastdup.metrics.txt
- Generated with native FastDup from commit 7b3f62587283a257fd38c5c20ceeda0364c285ef:
  https://github.com/zzhofict/FastDup/tree/7b3f62587283a257fd38c5c20ceeda0364c285ef
- Input is the public GATK NA12878.chr17_69k_70k.dictFix.bam regional test file:
  https://github.com/broadinstitute/gatk/blob/master/src/test/resources/NA12878.chr17_69k_70k.dictFix.bam
- Input SHA-256: afff2396bb69b112f687ccff7158df1a0afeb659c13918f59818caf0a538928b
- FastDup ran with --num-threads 2 on 4 October 2026. Output is preserved as emitted.
- Metrics SHA-256: 83259cb394c97e09fdf20f149b7d7e953e4d6709dfe8f28ad8c56afc6b5181ad
- The BAM contains 493 alignment records, including 15 mapped paired records with absent mates.
  FastDup floors the paired-record counter, so the reported categories account for 492 records.
  Its library-size and yield predictions do not characterize the original complete library.

Both files contain one metrics row and 100 predicted-yield histogram points.
