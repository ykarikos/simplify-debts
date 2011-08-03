import subprocess

class MyKeywords(object):
    def run_cmd(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output = p.communicate()[0]
#        if p.wait() != 0:
#            print "*WARN* %s failed" %cmd
        return output


