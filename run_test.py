#!/usr/bin/python

import unittest
import subprocess
import sys
import xml.etree.ElementTree as ET

import comp_modules as cm

cmd = 'java -cp "./jigg/bin/*" jigg.pipeline.Pipeline'

class TestSequenceFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.reporter = True

        # Gold data
        subprocess.call(cmd + ' -props ./props/english_ssplit_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_ssplit_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_tokenize_ssplit_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_tokenize_ssplit_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_pos_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_pos_gold_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_lemma_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_lemma_gold_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_ner_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_ner_gold_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_parse_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_parse_gold_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_depparse_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_depparse_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_fromtoken_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_fromtoken_gold_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_frompos_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_frompos_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnet/english_syntaxnet_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/syntaxnet/english_syntaxnet_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetpos/english_syntaxnetpos_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/syntaxnetpos/english_syntaxnetpos_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetparse/english_syntaxnetparse_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/syntaxnetparse/english_syntaxnetparse_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/japanese_ssplit_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/japanese_ssplit_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/kuromoji/japanese_kuromoji_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/kuromoji/japanese_kuromoji_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/mecab/japanese_mecab_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/mecab/japanese_mecab_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/juman/japanese_juman_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/juman/japanese_juman_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/cabocha/japanese_cabocha_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/cabocha/japanese_cabocha_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knp/japanese_knp_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/knp/japanese_knp_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knpdoc/japanese_knpdoc_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/knpdoc/japanese_knpdoc_gold_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/jaccg/japanese_jaccg_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/jaccg/japanese_jaccg_gold_json.properties', shell=True)

        # XML -> XML
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_pos_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_lemma_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_ner_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_parse_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_depparse_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_fromtoken_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_frompos_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnet/english_syntaxnet_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetpos/english_syntaxnetpos_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetparse/english_syntaxnetparse_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/kuromoji/japanese_kuromoji_test_xml.properties', # shell=True)

        subprocess.call(cmd + ' -props ./props/mecab/japanese_mecab_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/juman/japanese_juman_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/cabocha/japanese_cabocha_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knp/japanese_knp_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knpdoc/japanese_knpdoc_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/jaccg/japanese_jaccg_test_xml.properties', shell=True)

        # JSON -> JSON
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_pos_test_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_lemma_test_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_ner_test_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_parse_test_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_depparse_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_fromtoken_test_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_frompos_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnet/english_syntaxnet_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetpos/english_syntaxnetpos_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetparse/english_syntaxnetparse_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/kuromoji/japanese_kuromoji_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/mecab/japanese_mecab_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/juman/japanese_juman_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/cabocha/japanese_cabocha_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knp/japanese_knp_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knpdoc/japanese_knpdoc_test_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/jaccg/japanese_jaccg_test_json.properties', shell=True)

        # XML -> JSON
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_pos_test_xml_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_lemma_test_xml_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_ner_test_xml_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_parse_test_xml_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_depparse_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_fromtoken_test_xml_json.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_frompos_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnet/english_syntaxnet_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetpos/english_syntaxnetpos_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetparse/english_syntaxnetparse_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/kuromoji/japanese_kuromoji_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/mecab/japanese_mecab_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/juman/japanese_juman_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/cabocha/japanese_cabocha_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knp/japanese_knp_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knpdoc/japanese_knpdoc_test_xml_json.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/jaccg/japanese_jaccg_test_xml_json.properties', shell=True)

        # JSON -> XML
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_pos_test_json_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_lemma_test_json_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_ner_test_json_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_parse_test_json_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/corenlp/english_corenlp_depparse_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_fromtoken_test_json_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/berkeleyparser/english_berkeleyparser_frompos_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnet/english_syntaxnet_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetpos/english_syntaxnetpos_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/syntaxnetparse/english_syntaxnetparse_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/kuromoji/japanese_kuromoji_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/mecab/japanese_mecab_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/juman/japanese_juman_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/cabocha/japanese_cabocha_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knp/japanese_knp_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/knpdoc/japanese_knpdoc_test_json_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/jaccg/japanese_jaccg_test_json_xml.properties', shell=True)

    def test_01_corenlp_1_pos(self):
        goldRoot     = ET.parse('./xml/english_corenlp_pos_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_corenlp_pos_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_pos_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_pos_gold.json', \
            './json/english_corenlp_pos_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_pos_gold.json', \
            './json/english_corenlp_pos_test.json'))

    def test_01_corenlp_2_lemma(self):
        goldRoot     = ET.parse('./xml/english_corenlp_lemma_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_corenlp_lemma_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_lemma_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_lemma_gold.json', \
            './json/english_corenlp_lemma_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_lemma_gold.json', \
            './json/english_corenlp_lemma_test.json'))

    def test_01_corenlp_3_ner(self):
        goldRoot     = ET.parse('./xml/english_corenlp_ner_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_corenlp_ner_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_ner_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_ner_gold.json', \
                                     './json/english_corenlp_ner_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_ner_gold.json', \
                                     './json/english_corenlp_ner_test.json'))

    def test_01_corenlp_4_parse(self):
        goldRoot     = ET.parse('./xml/english_corenlp_parse_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_corenlp_parse_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_parse_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_parse_gold.json', \
                                     './json/english_corenlp_parse_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_parse_gold.json', \
                                     './json/english_corenlp_parse_test.json'))

    def test_01_corenlp_5_depparse(self):
        goldRoot     = ET.parse('./xml/english_corenlp_depparse_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_corenlp_depparse_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_depparse_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_depparse_gold.json', \
                                     './json/english_corenlp_depparse_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_depparse_gold.json', \
                                     './json/english_corenlp_depparse_test.json'))

    def test_02_berkeleyparser_1_fromToken(self):
        goldRoot     = ET.parse('./xml/english_berkeleyparser_fromtoken_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_berkeleyparser_fromtoken_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_berkeleyparser_fromtoken_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_fromtoken_gold.json', \
                                     './json/english_berkeleyparser_fromtoken_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_fromtoken_gold.json', \
                                     './json/english_berkeleyparser_fromtoken_test.json'))

    def test_02_berkeleyparser_2_fromPOS(self):
        goldRoot     = ET.parse('./xml/english_berkeleyparser_frompos_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_berkeleyparser_frompos_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_berkeleyparser_frompos_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_frompos_gold.json', \
                                     './json/english_berkeleyparser_frompos_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_frompos_gold.json', \
                                     './json/english_berkeleyparser_frompos_test.json'))

    def test_03_kuromoji(self):
        goldRoot     = ET.parse('./xml/japanese_kuromoji_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_kuromoji_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_kuromoji_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_kuromoji_gold.json', \
                                     './json/japanese_kuromoji_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_kuromoji_gold.json', \
                                     './json/japanese_kuromoji_test.json'))

    def test_04_mecab(self):
        goldRoot     = ET.parse('./xml/japanese_mecab_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_mecab_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_mecab_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_mecab_gold.json', \
                                     './json/japanese_mecab_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_mecab_gold.json', \
                                     './json/japanese_mecab_test.json'))

    def test_05_juman(self):
        goldRoot     = ET.parse('./xml/japanese_juman_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_juman_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_juman_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_juman_gold.json', \
                                     './json/japanese_juman_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_juman_gold.json', \
                                     './json/japanese_juman_test.json'))

    def test_06_cabocha(self):
        goldRoot     = ET.parse('./xml/japanese_cabocha_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_cabocha_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_cabocha_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_cabocha_gold.json', \
                                     './json/japanese_cabocha_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_cabocha_gold.json', \
                                     './json/japanese_cabocha_test.json'))

    def test_07_knp_1_knp(self):
        goldRoot     = ET.parse('./xml/japanese_knp_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_knp_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_knp_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_knp_gold.json', \
                                     './json/japanese_knp_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_knp_gold.json', \
                                     './json/japanese_knp_test.json'))

    def test_07_knp_2_knpDoc(self):
        goldRoot     = ET.parse('./xml/japanese_knpdoc_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_knpdoc_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_knpdoc_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_knpdoc_gold.json', \
                                     './json/japanese_knpdoc_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_knpdoc_gold.json', \
                                     './json/japanese_knpdoc_test.json'))

    def test_08_jaccg(self):
        goldRoot     = ET.parse('./xml/japanese_jaccg_gold.xml').getroot()
        testRoot     = ET.parse('./xml/japanese_jaccg_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_jaccg_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_jaccg_gold.json', \
                                     './json/japanese_jaccg_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_jaccg_gold.json', \
                                     './json/japanese_jaccg_test.json'))

    def test_09_syntaxnet(self):
        goldRoot     = ET.parse('./xml/english_syntaxnet_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_syntaxnet_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_syntaxnet_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_syntaxnet_gold.json', \
                                     './json/english_syntaxnet_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_syntaxnet_gold.json', \
                                     './json/english_syntaxnet_test.json'))

    def test_10_syntaxnetpos(self):
        goldRoot     = ET.parse('./xml/english_syntaxnetpos_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_syntaxnetpos_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_syntaxnetpos_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_syntaxnetpos_gold.json', \
                                     './json/english_syntaxnetpos_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_syntaxnetpos_gold.json', \
                                     './json/english_syntaxnetpos_test.json'))

    def test_11_syntaxnetparser(self):
        goldRoot     = ET.parse('./xml/english_syntaxnetparse_gold.xml').getroot()
        testRoot     = ET.parse('./xml/english_syntaxnetparse_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_syntaxnetparse_test_json.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_syntaxnetparse_gold.json', \
                                     './json/english_syntaxnetparse_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_syntaxnetparse_gold.json', \
                                     './json/english_syntaxnetparse_test.json'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=3).run(suite)
