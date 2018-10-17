from unittest import TextTestRunner, TestLoader

if __name__ == "__main__":

    loader = TestLoader()
    # loading tests like this until we need to make specific suites
    tests = loader.discover('../', 'reliq*')

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(tests)
