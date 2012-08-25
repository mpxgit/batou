from batou import UpdateNeeded
from batou.component import Component
from batou.lib.file import Directory
import os.path


class Subversion(Component):

    namevar = 'url'
    target = '.'

    def configure(self):
        self += Directory(self.target)

    def verify(self):
        raise UpdateNeeded()

    def update(self):
        with self.chdir(self.target):
            if not os.path.exists('.svn'):
                self.cmd(self.expand(
                    'svn co {{component.url}} .'))
            else:
                self.cmd(self.expand('svn revert -R .'))
                self.cmd(self.expand('svn switch {{component.url}}'))
                self.cmd(self.expand('svn up'))