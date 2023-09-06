#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""psutil

psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and
system utilization (CPU, memory, disks, network, sensors) in Python.
It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes.
"""

import psutil

# 获取CPU使用率
cpu_percent = psutil.cpu_percent(interval=1)

# 获取内存使用率
memory_percent = psutil.virtual_memory().percent

# 获取磁盘使用率（根目录）
disk_percent = psutil.disk_usage('/').percent

print('CPU使用率：{0:.2f}%'.format(cpu_percent))
print('内存使用率：{0}%'.format(memory_percent))
print('磁盘使用率：{0}%'.format(disk_percent))

# 获取网络使用情况
net_counter = psutil.net_io_counters()

print('网络使用情况：')
print(net_counter)
