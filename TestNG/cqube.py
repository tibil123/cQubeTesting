import sys
#sys.path.append('/home/devraj/PycharmProjects/SemesterReport')


sys.path.append('/home/devraj/PycharmProjects/cQubeTesting')
from get_dir import pwd
import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner
from Test import cqube_login
class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name

             unittest.defaultTestLoader.loadTestsFromTestCase(cqube_login.CqubeLogin),

        ])
        p = pwd()
        outfile = open(p.get_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
             stream=outfile,
             title='Test Report',
             verbosity = 1,
             description='Smoke Tests'

        )

        runner1.run(smoke_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()
