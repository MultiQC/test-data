&nbsp;
![MultiQC](multiqc-logo.png#gh-light-mode-only)
![MultiQC](multiqc-logo-darkbg.png#gh-dark-mode-only)
&nbsp;

### Aggregate bioinformatics results across many samples into a single report

This repository contains files to test MultiQC with. These are used in the
automated continous-integration tests and can be used whilst developing for MultiQC.

## Contributing

To add new files to this repository, please follow the following procedure:

After forking the repository to your own GitHub account:

```bash
git clone <forked-repo-address>
cd <repo-directory>
cp /your/files/. ./data/modules/<module_name>
git add .
git commit -m "<message describing change>"
git push
```

Create a Pull Request to bring your changes back into this repository.

Delete your fork once the PR is accepted _(optional)_

For information about MultiQC, please see [http://multiqc.info](http://multiqc.info)
or the [main MultiQC GitHub repository](https://github.com/MultiQC/MultiQC).
