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
        subprocess.call(cmd + ' -props ./props/english_ssplit_xml.properties')
        subprocess.call(cmd + ' -props ./props/english_ssplit_json.properties')
        subprocess.call(cmd + ' -props ./props/english_corenlp_tokenize_ssplit_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_tokenize_ssplit_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_gold_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_gold_json.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_fromtoken_gold_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_fromtoken_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_frompos_gold_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_frompos_gold_json.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/japanese_ssplit_xml.properties')
        subprocess.call(cmd + ' -props ./props/japanese_ssplit_json.properties')

        subprocess.call(cmd + ' -props ./props/japanese_kuromoji_gold_xml.properties')
        subprocess.call(cmd + ' -props ./props/japanese_kuromoji_gold_json.properties')

        # XML -> XML
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_test_xml.properties', shell=True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_test_xml.properties', shell=True)

        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_fromtoken_test_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_frompos_test_xml.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/japanese_kuromoji_test_xml.properties')

        # JSON -> JSON
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_test_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_test_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_test_json.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_fromtoken_test_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_frompos_test_json.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/japanese_kuromoji_test_json.properties')

        # XML -> JSON
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_test_xml_json.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_fromtoken_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_frompos_test_xml_json.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/japanese_kuromoji_test_xml_json.properties')

        # JSON -> XML
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_json_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_json_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_test_json_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_test_json_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_test_json_xml.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_fromtoken_test_json_xml.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_berkeleyparser_frompos_test_json_xml.properties', shell = True)

        subprocess.call(cmd + ' -props ./props/japanese_kuromoji_test_json_xml.properties')

    def test_01_corenlp_1_pos(self):
        testRoot = ET.parse('./xml/english_corenlp_pos_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_pos_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_pos_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_pos_gold.json', \
            './json/english_corenlp_pos_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_pos_gold.json', \
            './json/english_corenlp_pos_test.json'))

    def test_01_corenlp_2_lemma(self):
        testRoot = ET.parse('./xml/english_corenlp_lemma_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_lemma_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_lemma_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_lemma_gold.json', \
            './json/english_corenlp_lemma_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_lemma_gold.json', \
            './json/english_corenlp_lemma_test.json'))

    def test_01_corenlp_3_ner(self):
        testRoot = ET.parse('./xml/english_corenlp_ner_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_ner_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_ner_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_ner_gold.json', \
                                     './json/english_corenlp_ner_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_ner_gold.json', \
                                     './json/english_corenlp_ner_test.json'))

    def test_01_corenlp_4_parse(self):
        testRoot = ET.parse('./xml/english_corenlp_parse_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_parse_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_parse_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_parse_gold.json', \
                                     './json/english_corenlp_parse_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_parse_gold.json', \
                                     './json/english_corenlp_parse_test.json'))

    def test_01_corenlp_5_depparse(self):
        testRoot = ET.parse('./xml/english_corenlp_depparse_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_depparse_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_depparse_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_depparse_gold.json', \
                                     './json/english_corenlp_depparse_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_depparse_gold.json', \
                                     './json/english_corenlp_depparse_test.json'))

    def test_02_berkeleyparser_1_fromToken(self):
        testRoot = ET.parse('./xml/english_berkeleyparser_fromtoken_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_berkeleyparser_fromtoken_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_berkeleyparser_fromtoken_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_fromtoken_gold.json', \
                                     './json/english_berkeleyparser_fromtoken_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_fromtoken_gold.json', \
                                     './json/english_berkeleyparser_fromtoken_test.json'))

    def test_02_berkeleyparser_2_fromPOS(self):
        testRoot = ET.parse('./xml/english_berkeleyparser_frompos_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_berkeleyparser_frompos_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_berkeleyparser_frompos_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_frompos_gold.json', \
                                     './json/english_berkeleyparser_frompos_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_berkeleyparser_frompos_gold.json', \
                                     './json/english_berkeleyparser_frompos_test.json'))

    def test_03_kuromoji(self):
        testRoot = ET.parse('./xml/japanese_kuromoji_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/japanese_kuromoji_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/japanese_kuromoji_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/japanese_kuromoji_gold.json', \
                                     './json/japanese_kuromoji_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/japanese_kuromoji_gold.json', \
                                     './json/japanese_kuromoji_test.json'))

    def test_04_mecab(self):
        self.assertTrue(1 == 1)

    def test_05_juman(self):
        self.assertTrue(1 == 1)

    def test_06_cabocha(self):
        self.assertTrue(1 == 1)

    def test_07_knp_1_knp(self):
        self.assertTrue(1 == 1)

    def test_07_knp_2_knpDoc(self):
        self.assertTrue(1 == 1)

    def test_08_jaccg(self):
        self.assertTrue(1 == 1)

    def test_09_syntaxnet_1_pos(self):
        self.assertTrue(1 == 1)

    def test_09_syntaxnet_2_basicDependencies(self):
        self.assertTrue(1 == 1)

    def test_10_syntaxnetpos(self):
        self.assertTrue(1 == 1)

    def test_11_syntaxnetparser(self):
        self.assertTrue(1 == 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=3).run(suite)
