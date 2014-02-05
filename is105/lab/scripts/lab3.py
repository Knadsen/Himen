import subprocess



def lab3_scripts():
	subprocess.call(["python", "test1.py"])
	subprocess.call(["bash", "test1.sh"])
	subprocess.call(["perl", "test1.pl"])

lab3_scripts()
