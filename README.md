# jigg-pipeline-test
Repository for integrating test of the `-inputFormat` option of [`jigg`](https://github.com/tomeken-yoshinaga/jigg/tree/develop).

## Test result

|| annotator | XML -> XML |XML -> JSON |JSON -> JSON |JSON -> XML | 
|:----------|:------|:--|:--|:--|:--|
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
|| **annotator** | **XML -> XML** |**XML -> JSON** |**JSON -> JSON** |**JSON -> XML** | 

## Example

### Command
```sh
$ java -cp "./jigg/bin/*" jigg.pipeline.Pipeline -annotators "berkeleyparser" \
-berkeleyparser.grFileName ./models/eng_sm6.gr -checkRequirement false \
-inputFormat xml -outputFormat xml -file ./xml/english_corenlp_tokenize_ssplit.xml \
-output ./xml/english_berkrleyparser_fromtoken_test.xml
```

### Input file
```xml
<?xml version='1.0' encoding='UTF-8'?>
<root>
  <document id="d0">
    <sentences>
      <sentence characterOffsetEnd="38" characterOffsetBegin="0" id="s0">
        Alice asked her mother to cook a cake.
        <tokens annotators="corenlp">
          <token form="Alice" id="t0" characterOffsetBegin="0" characterOffsetEnd="5"/>
          <token form="asked" id="t1" characterOffsetBegin="6" characterOffsetEnd="11"/>
          <token form="her" id="t2" characterOffsetBegin="12" characterOffsetEnd="15"/>
          <token form="mother" id="t3" characterOffsetBegin="16" characterOffsetEnd="22"/>
          <token form="to" id="t4" characterOffsetBegin="23" characterOffsetEnd="25"/>
          <token form="cook" id="t5" characterOffsetBegin="26" characterOffsetEnd="30"/>
          <token form="a" id="t6" characterOffsetBegin="31" characterOffsetEnd="32"/>
          <token form="cake" id="t7" characterOffsetBegin="33" characterOffsetEnd="37"/>
          <token form="." id="t8" characterOffsetBegin="37" characterOffsetEnd="38"/>
        </tokens>
      </sentence>
      <sentence characterOffsetEnd="85" characterOffsetBegin="39" id="s1">
        Bob saw a girl in the garden with a telescope.
        <tokens annotators="corenlp">
          <token form="Bob" id="t9" characterOffsetBegin="0" characterOffsetEnd="3"/>
          <token form="saw" id="t10" characterOffsetBegin="4" characterOffsetEnd="7"/>
          <token form="a" id="t11" characterOffsetBegin="8" characterOffsetEnd="9"/>
          <token form="girl" id="t12" characterOffsetBegin="10" characterOffsetEnd="14"/>
          <token form="in" id="t13" characterOffsetBegin="15" characterOffsetEnd="17"/>
          <token form="the" id="t14" characterOffsetBegin="18" characterOffsetEnd="21"/>
          <token form="garden" id="t15" characterOffsetBegin="22" characterOffsetEnd="28"/>
          <token form="with" id="t16" characterOffsetBegin="29" characterOffsetEnd="33"/>
          <token form="a" id="t17" characterOffsetBegin="34" characterOffsetEnd="35"/>
          <token form="telescope" id="t18" characterOffsetBegin="36" characterOffsetEnd="45"/>
          <token form="." id="t19" characterOffsetBegin="45" characterOffsetEnd="46"/>
        </tokens>
      </sentence>
    </sentences>
  </document>
</root>
```

### Output file
```xml
<?xml version='1.0' encoding='UTF-8'?>
<root>
  <document id="d0">
    <sentences>
      <sentence characterOffsetEnd="38" characterOffsetBegin="0" id="s0">
        Alice asked her mother to cook a cake.
        <tokens annotators="corenlp berkeleyparser">
          <token form="Alice" id="t0" characterOffsetBegin="0" characterOffsetEnd="5" pos="NNP"/>
          <token form="asked" id="t1" characterOffsetBegin="6" characterOffsetEnd="11" pos="VBD"/>
          <token form="her" id="t2" characterOffsetBegin="12" characterOffsetEnd="15" pos="PRP$"/>
          <token form="mother" id="t3" characterOffsetBegin="16" characterOffsetEnd="22" pos="NN"/>
          <token form="to" id="t4" characterOffsetBegin="23" characterOffsetEnd="25" pos="TO"/>
          <token form="cook" id="t5" characterOffsetBegin="26" characterOffsetEnd="30" pos="VB"/>
          <token form="a" id="t6" characterOffsetBegin="31" characterOffsetEnd="32" pos="DT"/>
          <token form="cake" id="t7" characterOffsetBegin="33" characterOffsetEnd="37" pos="NN"/>
          <token form="." id="t8" characterOffsetBegin="37" characterOffsetEnd="38" pos="."/>
        </tokens>
        <parse root="s0_berksp0" annotators="berkeleyparser">
          <span children="s0_berksp1 s0_berksp2 t8" symbol="S" id="s0_berksp0"/>
          <span children="t0" symbol="NP" id="s0_berksp1"/>
          <span children="t1 s0_berksp3 s0_berksp4" symbol="VP" id="s0_berksp2"/>
          <span children="t2 t3" symbol="NP" id="s0_berksp3"/>
          <span children="s0_berksp5" symbol="S" id="s0_berksp4"/>
          <span children="t4 s0_berksp6" symbol="VP" id="s0_berksp5"/>
          <span children="t5 s0_berksp7" symbol="VP" id="s0_berksp6"/>
          <span children="t6 t7" symbol="NP" id="s0_berksp7"/>
        </parse>
      </sentence>
      <sentence characterOffsetEnd="85" characterOffsetBegin="39" id="s1">
        Bob saw a girl in the garden with a telescope.
        <tokens annotators="corenlp berkeleyparser">
          <token form="Bob" id="t9" characterOffsetBegin="0" characterOffsetEnd="3" pos="NNP"/>
          <token form="saw" id="t10" characterOffsetBegin="4" characterOffsetEnd="7" pos="VBD"/>
          <token form="a" id="t11" characterOffsetBegin="8" characterOffsetEnd="9" pos="DT"/>
          <token form="girl" id="t12" characterOffsetBegin="10" characterOffsetEnd="14" pos="NN"/>
          <token form="in" id="t13" characterOffsetBegin="15" characterOffsetEnd="17" pos="IN"/>
          <token form="the" id="t14" characterOffsetBegin="18" characterOffsetEnd="21" pos="DT"/>
          <token form="garden" id="t15" characterOffsetBegin="22" characterOffsetEnd="28" pos="NN"/>
          <token form="with" id="t16" characterOffsetBegin="29" characterOffsetEnd="33" pos="IN"/>
          <token form="a" id="t17" characterOffsetBegin="34" characterOffsetEnd="35" pos="DT"/>
          <token form="telescope" id="t18" characterOffsetBegin="36" characterOffsetEnd="45" pos="NN"/>
          <token form="." id="t19" characterOffsetBegin="45" characterOffsetEnd="46" pos="."/>
        </tokens>
        <parse root="s1_berksp0" annotators="berkeleyparser">
          <span children="s1_berksp1 s1_berksp2 t19" symbol="S" id="s1_berksp0"/>
          <span children="t9" symbol="NP" id="s1_berksp1"/>
          <span children="t10 s1_berksp3" symbol="VP" id="s1_berksp2"/>
          <span children="s1_berksp4 s1_berksp5 s1_berksp7" symbol="NP" id="s1_berksp3"/>
          <span children="t11 t12" symbol="NP" id="s1_berksp4"/>
          <span children="t13 s1_berksp6" symbol="PP" id="s1_berksp5"/>
          <span children="t14 t15" symbol="NP" id="s1_berksp6"/>
          <span children="t16 s1_berksp8" symbol="PP" id="s1_berksp7"/>
          <span children="t17 t18" symbol="NP" id="s1_berksp8"/>
        </parse>
      </sentence>
    </sentences>
  </document>
</root>
```

## Integration test script

### Requirement
* python 2.7
* JDK 1.8
* syntaxnet
* mecab
* cabocha
* juman
* knp

### Running the test
1. If you don't have `stanford-english-corenlp-2016-01-10-models.jar` and 
`eng_sm6.gr`, run a following script.
```sh
$ ./scripts/download-models.sh
```
If you have them, add a soft link.
```sh
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
test_09_syntaxnet (__main__.TestSequenceFunctions) ... ok
test_10_syntaxnetpos (__main__.TestSequenceFunctions) ... ok
test_11_syntaxnetparser (__main__.TestSequenceFunctions) ... ok

----------------------------------------------------------------------
Ran 17 tests in 1616.272s

OK
```