Real dataset generated from NovaSeq sequencing by BclConvert 3.6.3 (only files neccessay for MultiQC included)

This directory contains multiple bclconvert output directories _all coming from the same sequencing run_ (bclconvert multiqc module should not process multiple bclconvert output directories coming from different sequencing runs, and in fact will exit with an error if it detects such a thing is being attempted by checking RunInfo.xml for multiple run ids).

Running multiqc in this directory should produce a single MultiQC report, merging all the data and recalculating undetermined stats.
