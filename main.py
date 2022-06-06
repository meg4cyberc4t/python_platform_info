import platform
import cpuinfo
import shutil
import psutil
from pprint import pprint

print('About processor:')
print(platform.platform())
print(platform.processor())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_implementation())
print(platform.python_version())
print(platform.release())
pprint(cpuinfo.get_cpu_info())

print()

print('About disk:')
total, used, free = shutil.disk_usage("/")
print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

print()

print("About RAM:")
print(psutil.virtual_memory())