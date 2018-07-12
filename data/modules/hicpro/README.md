# Results from HiC-Pro test-op

```bash
wget https://zerkalo.curie.fr/partage/HiC-Pro/HiCPro_testdata.tar.gz && tar -zxvf HiCPro_testdata.tar.gz
/bin/rm -f HiCPro_testdata.tar.gz

RES_PREFIX=HiC_Pro_test-op
CONFIG=config_test_latest.txt

## standalone complete pipeline
cmd="time HiC-Pro -i test_data/ -o ${RES_PREFIX} -c ${CONFIG}"
echo $cmd
eval $cmd
if [[ $? != 0 ]]; then echo -e "Error in test-op - Exit 1"; exit 1; fi
```
