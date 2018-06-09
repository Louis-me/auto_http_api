# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
import unittest
from TestCases.Api import ApiTest
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseGetExcel import write_excel
from Base.BaseInit import BaseInit


def runner_case():
    BaseInit().mk_file()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(ApiTest))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runner_case()
    write_excel()
