import platform
import cpuinfo
from pprint import pprint

print(platform.platform())
print(platform.processor())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_implementation())
print(platform.python_version())
print(platform.release())
pprint(cpuinfo.get_cpu_info())

# macOS-12.4-arm64-arm-64bit
# arm
# ('default', 'May 17 2022 12:55:41')
# Clang 13.1.6 (clang-1316.0.21.2.5)
# CPython
# 3.8.9
# 21.5.0
# {'arch': 'ARM_8',
#  'arch_string_raw': 'arm64',
#  'bits': 64,
#  'brand_raw': 'Apple M1',
#  'count': 8,
#  'cpuinfo_version': [8, 0, 0],
#  'cpuinfo_version_string': '8.0.0',
#  'python_version': '3.8.9.final.0 (64 bit)'}