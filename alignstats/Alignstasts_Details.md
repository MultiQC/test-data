### Alignstats Details

* Name of tool: alignstats
* Tool homepage: https://github.com/jfarek/alignstats
* Tool description: AlignStats produces various alignment, whole genome coverage, and capture coverage metrics for sequence alignment files in SAM, BAM, and CRAM format.
* Data suitable for MultiQC plot(s): In general I think the absolute values like read counts and base counts  are best for plotting (i.e. MappedReads, AlignedBases, Q20Bases, WgsCoverageBases20 etc.)
* Most interesting data for General Stats table: In general I think stats values like percent, mean, median are best for the stats table (i.e. MappedReadsPct, MismatchedBasesPct, WgsCoverageMean, WgsCoverageMedian, CapCoverageBases20Pct etc.)

### Alignstats output:

* Log filename pattern: The user names the output file or redirects to STDOUT, so the filename doesn't have a set pattern, although it's JSON, so should at least end in JSON and for our pipeline is always named *.alignstats.json.
* File contents:  I've given a head/tail snippet of the JSON output from alignstats below.  Output is very simple with JSON objects one level deep, so just a bunch of key/value pairs.  The full JSON output was uploaded along side this file as, `Sample.alignstats.json`.

```
{
    "InputFileName": "DS184660.bam",
    "InputFileSize": 55590928353,
    "TotalRecords": 999415788,
    "UnfilteredRecords": 999415788,
    "UnfilteredRecordsPct": 100.000000,
    "FilteredRecords": 0,
    "FilteredRecordsPct": 0.000000,
    "YieldReads": 999415788,
    "YieldBases": 134178052543,
...
    "CapTargetsHitPct": 100.000000,
    "CapTargetBuffersHit": 0,
    "CapTargetBuffersHitPct": 0.000000,
    "CapTotalTargets": 25,
    "CapHighCoverageNonTargetHits": 8205,
    "CapBasesOnTarget": 3095693981,
    "CapBasesOnBuffer": 0,
    "CapReadsOnTargetOrBuffer": 815701147,
    "CapReadsOnTargetOrBufferPct": 85.215900
}
```
