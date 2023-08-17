Real dataset generated from AVITI sequencing by Bases2fastq v1.4.0 (only files neccessay for MultiQC included)

This directory contains multiple bases2fastq output directories.

Running multiqc on any of the sub-directories single MultiQC report, spanning multiple runs and multiple samples.

multiqc Cloudbreak-DVT-ecoli-wgs-2x150/ --filename Cloudbreak-DVT-ecoli-wgs-2x150 --force
multiqc Cloudbreak-DVT-human-wgs-2x150/ --filename Cloudbreak-DVT-human-wgs-2x150 --force
multiqc Cloudbreak-DVT-human-rnaseq-2x75/ --filename Cloudbreak-DVT-human-rnaseq-2x75 --force

 Cloudbreak-DVT-ecoli-wgs-2x150/ - contains a 96plex of Ecoli WGS lirbaries, sequenced on a single AVITI run, 1 run total.
 Cloudbreak-DVT-human-wgs-2x150/ - contains a 2plex of Human WGS lirbaries, sequenced on a single AVITI run, 10 runs total.
 Cloudbreak-DVT-human-rnaseq-2x75/ - contains a 16plex of Human RNASEQ lirbaries, sequenced on a single AVITI run, 10 runs total.
