#
#
import os
from autotest.client                        import test, utils

class ubuntu_futex(test.test):
    version = 1

    def initialize(self):
        self.job.require_gcc()

    # setup
    #
    #    Automatically run when there is no autotest/client/tmp/<test-suite> directory
    #
    def setup(self):
        os.chdir(self.srcdir)
        cmd = 'git clone git://git.kernel.org/pub/scm/linux/kernel/git/dvhart/futextest.git'
        self.results = utils.system_output(cmd, retain_output=True)

        os.chdir(os.path.join(self.srcdir, 'futextest', 'functional'))
        cmd = 'sed -i s/lpthread/pthread/ Makefile'
        self.results = utils.system_output(cmd, retain_output=True)

        cmd = 'make'
        self.results = utils.system_output(cmd, retain_output=True)

    # run_once
    #
    #    Driven by the control file for each individual test.
    #
    def run_once(self, test_name):
        cmd = './run.sh'
        self.results = utils.system_output(cmd, retain_output=True)

# vi:set ts=4 sw=4 expandtab syntax=python: