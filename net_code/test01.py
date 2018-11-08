import subprocess

res = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(res.stdout.read().decode("gbk"))
print(res.stderr.read().decode("gbk"))

