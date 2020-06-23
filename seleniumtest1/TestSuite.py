import unittest
from common import HTMLTestRunnerCN
from seleniumtest1.demo1 import unittest_demo1
from seleniumtest1.appiumDemo import appuium_demo
from seleniumtest1.fuxi import test

suite = unittest.TestSuite()
suite.addTest(unittest_demo1('test_loginsSuccess'))
# suite.addTest(unittest_demo1('test_nulluser'))
# suite.addTest(unittest_demo1('test_nullpwd'))
# suite.addTest(appuium_demo("test_click"))
# suite.addTest(test('test1'))

if __name__ == '__main__':
    # 执行测试

    runner = unittest.TestSuite()
    with open('HTMLReport.html', 'wb+') as f:
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f, title='测试报告', description='测试报告详情', verbosity=2, tester='姚希龙')
        runner.run(suite)  # 运行suite把报告写成HTML格式
        f.close()
