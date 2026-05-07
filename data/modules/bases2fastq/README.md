Real dataset generated from AVITI sequencing by Bases2fastq v1.4.0 (only files necessary for MultiQC included), plus template run layouts for run-level and project-level outputs.

This directory contains multiple bases2fastq output directories (run roots). Each subdirectory is a separate run root: it may contain run-level `RunStats.json`, optional `RunManifest.json`, and optionally `Samples/<ProjectName>/<ProjectName>_RunStats.json` for project-level data.

## How to run MultiQC

**Option 1 – run on the whole module directory** (all run roots at once):

```bash
multiqc test-data/data/modules/bases2fastq/ --filename bases2fastq --force
```

**Option 2 – run on a single run root** (typical for project-level: change into that directory or pass it):

```bash
# Run-level only (no project, no RunManifest)
multiqc test-data/data/modules/bases2fastq/PairedEndNoProject/ --filename PairedEndNoProject --force

# Run + DefaultProject (RunManifest at run root; project file in Samples/DefaultProject/)
multiqc test-data/data/modules/bases2fastq/PairedEndDefaultProject/ --filename PairedEndDefaultProject --force

# Multiple projects in one run
multiqc test-data/data/modules/bases2fastq/PairedEndProjects/ --filename PairedEndProjects --force
```

## Contents

* **WGS/** – Real AVITI/Bases2fastq run (run-level only).
* **WES/** – Real AVITI/Bases2fastq run (run-level only).
* **PairedEndNoProject/** – Template: run-level `RunStats.json` only.
* **SingleEndNoProject/** – Template: run-level `RunStats.json` only (single-end).
* **PairedEndDefaultProject/** – Template: run-level + `RunManifest.json` + `Samples/DefaultProject/DefaultProject_RunStats.json`.
* **PairedEndDefaultProjectAdapter/**, **PairedEndDefaultProjectTwoAdapter/**, **PairedEndDefaultProjectUltraQ/** – Variants with DefaultProject and RunManifest.
* **PairedEndProjects/** – Template: run-level + RunManifest + multiple projects (`Samples/Project1/`, `Project2/`, …).

Run-level data lives in `RunStats.json` at the run root. When project-level outputs exist, they live under `Samples/<ProjectName>/<ProjectName>_RunStats.json`, and `RunManifest.json` is at the run root (or next to the project file). Use option 2 when you want a report for one run root; use option 1 to aggregate all run roots in one report.
