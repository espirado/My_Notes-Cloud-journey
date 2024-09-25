# Tool

uptime - Load averages to identify if load is increasing or decreasing (compare 1-, 5-, and 15-minute averages).

dmesg -T | tail - Kernel errors including OOM events.

vmstat -SM 1 - System-wide statistics: run queue length, swapping, overall CPU usage.

mpstat -P ALL 1 - Per-CPU balance: a single busy CPU can indicate poor thread scaling.

pidstat 1 - Per-process CPU usage: identify unexpected CPU consumers, and user/system CPU time for each process.

iostat -sxz 1 - Disk I/O statistics: IOPS and throughput, average wait time, percent busy.

free -m - Memory usage including the file system cache.

sar -n DEV 1 - Network device I/O: packets and throughput.

sar -n TCP,ETCP 1 TCP statistics: connection rates, retransmits.

top - Check overview.