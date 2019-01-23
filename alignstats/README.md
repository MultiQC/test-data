### Alignstats Test Data

Test data for alignstats can be found in this folder.  The file is gzip compressed and named Sample.alignstats.json.gz.  It represents alignment stats for a single sample WGS BAM file.  Alignstats has some very nice depth/coverage summary stats and for this viwing this kind of data in tabular form in MutiQC I typically prefer relative values like percent rather than absolute values like read counds, where as values like read counts etc work well in the graphical (bee swarm etc) views.  Alignstats produces some values that are also reported by other tools like `samtools stats`, so while having those reported from the alignstats output would be fine there would be fine that would be redundant info for users who also run `samtools stats`, the values I would really love to see are things that I don't find in other tools that we run such as:

```
"DuplicateBasesPct": 9.780467,
"MappedBasesPct": 98.612693,
"AlignedBasesPct": 96.267198,
"MatchedBasesPct": 98.971407,
"MismatchedBasesPct": 0.802057,
"InsertedBasesPct": 0.226536,
"DeletedBasesPct": 0.044949,
"SoftClippedBasesPct": 2.378492,
"PerfectBasesPct": 66.520823,
"Q20BasesPct": 96.233052,
"UnpairedReadsPct": 0.104051,
"R1UnpairedReadsPct": 0.486684,
"R2UnpairedReadsPct": 8.833484,
"ChimericReadPairPct": 3.005516,
```

For WGS samples:

```
"WgsCoverageBases1Pct": 92.352244,
"WgsCoverageBases10Pct": 92.009921,
"WgsCoverageBases15Pct": 91.004414,
"WgsCoverageBases20Pct": 88.634897,
"WgsCoverageBases30Pct": 77.600943,
"WgsCoverageBases40Pct": 42.446312,
"WgsCoverageBases50Pct": 10.493153,
"WgsCoverageBases100Pct": 0.360472,
"WgsCoverageBases1000Pct": 0.034122,
```

For WES samples:

```
"CapCovDuplicateReadsPct": 9.257615,
"CapAlignedReadsPct": 95.777663,
"CapCoverageBases1Pct": 92.299802,
"CapCoverageBases10Pct": 92.036633,
"CapCoverageBases15Pct": 91.087238,
"CapCoverageBases20Pct": 88.790587,
"CapCoverageBases30Pct": 77.809853,
"CapCoverageBases40Pct": 42.372473,
"CapCoverageBases50Pct": 10.158809,
"CapCoverageBases100Pct": 0.149016,
"CapCoverageBases1000Pct": 0.007711,
"CapTargetAlignedReadsPct": 85.215900,
"CapTargetsHitPct": 100.000000,
"CapTargetBuffersHitPct": 0.000000,
```
