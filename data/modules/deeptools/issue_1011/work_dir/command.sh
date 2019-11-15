#!/bin/bash -euo pipefail

multiqc . -f --config multiqc_config.yaml -m deeptools
