# jigg-pipeline-test
Repository for integrating test of the `-inputFormat` option of [`jigg`](https://github.com/tomeken-yoshinaga/jigg/tree/intermediateInput).

## Test Result

| | | XML |XML |JSON |JSON | 
|:----------|:------|:--|:--|:--|:--|
| | | -> | -> | -> | -> | 
| annotator | | XML |JSON |JSON |XML | 
| | | | | | | 
|corenlp | pos | Ok |Ok |Ok |Ok |
|corenlp | lemma | Ok |Ok |Ok |Ok |
|corenlp | ner | Ok |Ok |Ok |Ok |
|corenlp | parse | Ok |Ok |Ok |Ok |
|corenlp | depparse | Ok |Ok |Ok |Ok |
| | | | | | | 
|berkeleyparser | fromtoken | Ok |Ok |Ok |Ok |
|berkeleyparser | frompos | Ok |Ok |Ok |Ok |
| | | | | | | 
|syntaxnet | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|syntaxnetpos | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|syntaxnetparse | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|macab | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|cabocha | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|juman | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|knp | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|knpDoc | - | Ok |Ok |Ok |Ok |
| | | | | | | 
|jaccg | - | Ok |Ok |Ok |Ok |

## Integration test script

### Requirement
* python 2.7
* JDK 1.8
* juman
* knp/knpDoc
* mecab
* cabocha
* syntaxnet

### Workflow
1. If you don't have `stanford-english-corenlp-2016-01-10-models.jar` and 
`eng_sm6.gr`, run a following script.
```sh
$ ./scripts/download-models.sh
```
If you have them, 
```sh
$ mkdir models
$ ln -s STANFORD_CORENLP_EDU_DIR ./edu
$ ln -s ENG_GR ./models/
```

1. Install the required tools.
```sh
$ ./scripts/install-tools.sh
```

1. Installing and compiling `syntaxnet`. And adding a soft link to the syntaxnet directory, which contain the files of `bazel-bin`, `bazel-syntaxnet`, etc.
```sh
$ ln -s /SYNTAXNET/DIRECTORY ./syntaxnet
```

1. Run `run_test.py`. After run all test patterns, the following message will be displayed.

Result: 
```sh
Writing to ./xml/japanese_jaccg_test_json.xml... done [0.1 sec]
test_01_corenlp_1_pos (__main__.TestSequenceFunctions) ... ok
test_01_corenlp_2_lemma (__main__.TestSequenceFunctions) ... ok
test_01_corenlp_3_ner (__main__.TestSequenceFunctions) ... ok
test_01_corenlp_4_parse (__main__.TestSequenceFunctions) ... ok
test_01_corenlp_5_depparse (__main__.TestSequenceFunctions) ... ok
test_02_berkeleyparser_1_fromToken (__main__.TestSequenceFunctions) ... ok
test_02_berkeleyparser_2_fromPOS (__main__.TestSequenceFunctions) ... ok
test_03_kuromoji (__main__.TestSequenceFunctions) ... ok
test_04_mecab (__main__.TestSequenceFunctions) ... ok
test_05_juman (__main__.TestSequenceFunctions) ... ok
test_06_cabocha (__main__.TestSequenceFunctions) ... ok
test_07_knp_1_knp (__main__.TestSequenceFunctions) ... ok
test_07_knp_2_knpDoc (__main__.TestSequenceFunctions) ... ok
test_08_jaccg (__main__.TestSequenceFunctions) ... ok
test_09_syntaxnet_1_pos (__main__.TestSequenceFunctions) ... ok
test_09_syntaxnet_2_basicDependencies (__main__.TestSequenceFunctions) ... ok
test_10_syntaxnetpos (__main__.TestSequenceFunctions) ... ok
test_11_syntaxnetparser (__main__.TestSequenceFunctions) ... ok

----------------------------------------------------------------------
Ran 18 tests in 1495.368s

OK
```