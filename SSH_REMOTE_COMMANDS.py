# import libraries

import paramiko

# Vars

Distribution = "IP"
USER = "user"
OpenSRC = "ibm i open source path"
ScriptName = "prueba.py"
PathSRC = "path python py"
Execute = PathSRC + ScriptName
Remote_cmd = 'cd %s' % OpenSRC
Remote_py = 'python3 %s' % Execute
Pass = "pass"

# Execute SSH, Set Path and Extract Log User for SBS.

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(Distribution, username=USER, password=Pass)

stdin, stdout, stderr = client.exec_command("%s " % Remote_cmd + "\n %s " % Remote_py, get_pty=True)
print(stdout.read())
client.close()
