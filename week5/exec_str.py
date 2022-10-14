import coverage
import unittest

cov = coverage.coverage(branch=True, source=['mystr'])
cov.start()
suite = unittest.defaultTestLoader.discover("E:/4GitHub/pyHelloWorld/week5/", "week5_homework.py")
unittest.TextTestRunner().run(suite)
cov.stop()
cov.save()
cov.report()
cov.html_report(directory='E:/4GitHub/pyHelloWorld/testreport/strunitest')
