# <img src="MultiQC_logo.png" width="300" title="MultiQC">

**MultiQC is a tool to aggregate bioinformatics results across many
samples into a single report.**

This repository contains files to test MultiQC with. These are used in the
automated [Travis CI build tests](https://travis-ci.org/ewels/MultiQC)
and can be used whilst developing for MultiQC.

To add new files to this repository, please follow the following procedure:

1. Fork the repository to your own account
2. Clone the repository locally
3. Copy your log files to `MultiQC_TestData/data/modules/<module_name>`
4. Commit and push your changes (`git add .` / `git commit -m "<message describing change>"` / `git push`)
5. Create a Pull Request to bring your changes back into this repository.
6. Delete your fork once the PR is accepted _(optional)_

For information about MultiQC, please see [http://multiqc.info](http://multiqc.info)
or the [main MultiQC GitHub repository](https://github.com/ewels/MultiQC).