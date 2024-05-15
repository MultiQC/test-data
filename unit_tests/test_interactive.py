import multiqc


def test_parse_logs_fn_clean_exts():
    multiqc.parse_logs(
        "data/modules/fastp/SAMPLE.json",
        "data/modules/fastp/single_end",
        extra_fn_clean_exts=["_1", "_S10_R1_001"],
    )
    assert multiqc.list_samples() == ["SRR5442949", "smalltest"]
    assert multiqc.list_modules() == ["fastp"]


def test_parse_logs_ignore_samples():
    multiqc.parse_logs(
        "data/modules/quast/full_metaquast_run",
        ignore_samples=["meta_contigs_2"],
    )

    assert multiqc.list_samples() == ["SRR5442949", "meta_contigs_1", "smalltest"]
    assert multiqc.list_modules() == ["fastp", "QUAST"]
