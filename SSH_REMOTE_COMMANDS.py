# import libraries

import paramiko
import os

# Vars

Distribution = "IP"
USER = "user"
Connect = USER + "@" + Distribution
OpenSRC = "ibm i open source path"
ScriptName = "prueba.py"
PathSRC = "path python py"
Execute = PathSRC + ScriptName
Remote_cmd = 'cd %s' % OpenSRC
Remote_py = 'python3 %s' % Execute
LogPath = os.environ.get("USERPROFILE")
LogPath = LogPath + "\\Desktop"
NameLog = "Prueba.txt"
AllPathLog = LogPath + "\\" + NameLog
Pass = "pass"

# Execute SSH, Set Path and Extract Log User for SBS.

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(Distribution, username=USER, password=Pass)

stdin, stdout, stderr = client.exec_command("%s " % Remote_cmd + "\n %s " % Remote_py, get_pty=True)
print(stdout.read())
client.close()
