# jigg-pipeline-test
Repository for integrating test using by intermediate input option of jigg.

# Requirement
* python 2.7
* JDK 1.8
* git
* automake1.4
* gcc
* g++
* libtool
* make
* maven

# Workflow
1. If you don't have `stanford-english-corenlp-2016-01-10-models.jar` and 
`eng_sm6.gr`, run a following script.
```bash
$ ./scripts/download-models.sh
```
If you have them, 
```bash
$ mkdir models
$ ln -s STANFORD_CORENLP_EDU_DIR ./edu
$ ln -s ENG_GR ./models/
```

1. Install the required tools.
```bash
$ ./scripts/install-tools.sh
```
1. Run `run_test.py`,

Result: 
```bash
test_1_corenlp_1_pos (__main__.TestSequenceFunctions) ... ok
test_1_corenlp_2_lemma (__main__.TestSequenceFunctions) ... ok
test_1_corenlp_3_ner (__main__.TestSequenceFunctions) ... ok
test_1_corenlp_4_parse (__main__.TestSequenceFunctions) ... ok
test_1_corenlp_5_depparse (__main__.TestSequenceFunctions) ... ok

----------------------------------------------------------------------
Ran 5 tests in 31.746s

OK
```

# Test Result

| annotator | Check |
|:----------|:------|
|corenlp[pos]| Ok|