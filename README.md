# <img src="MultiQC_logo.png" width="300" title="MultiQC">

**MultiQC is a tool to aggregate bioinformatics results across many
samples into a single report.**

This repository contains files to test MultiQC with. These are used in the
automated [Travis CI build tests](https://travis-ci.org/ewels/MultiQC)
and can be used whilst developing for MultiQC.

## Contributing

To add new files to this repository, please follow the following procedure:

After forking the repository to your own GitHub account:

```
git clone https://github.com/<your github username>/MultiQC_TestData.git
cd MultiQC_TestData
cp /your/files/. ./data/modules/<module_name> 
git add .
git commit -m "<message describing change>"
git push
```

Create a Pull Request to bring your changes back into this repository.

Delete your fork once the PR is accepted _(optional)_ 

For information about MultiQC, please see [http://multiqc.info](http://multiqc.info)
or the [main MultiQC GitHub repository](https://github.com/ewels/MultiQC).
