import unittest
import subprocess

props = './test.properties'
cmd = 'java -cp "$HOME/IdeaProjects/jigg/bin/*" jigg.pipeline.Pipeline'

if __name__ == '__main__':
    subprocess.call(cmd + ' -props %s' % props, shell=True)
