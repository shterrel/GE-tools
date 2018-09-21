#Just a simple script to do math for calculating percentage from
#capacity email that is generated weekly for GE
#built by Squirrel

print ("What is memory_mb_used and memory_mb?")
memory_mb_used = float(input("memory_mb_used: "))
memory_mb = float(input("memory_mb: "))
answer_memory = ((memory_mb_used / memory_mb) * 100)
Memory = ("%.2f" % answer_memory)
print "Memory Percentage: " + "%.2f" % answer_memory + "%"

print ("What is vcpus_used and vcpus?")
vcpus_used = float(input('vcpus_used: '))
vcpus = float(input('vcpus: ') * 4)
answer_vcpu = ((vcpus_used / vcpus) * 100)
VCPU = ("%.2f" % answer_vcpu)
print "VCPUs Percentage: " + "%.2f" % answer_vcpu + "%"

print ("What is disk_avalable_least and local_gb?")
disk_available_least = float(input("disk_available_least: "))
local_gb = float(input("local_gb: "))
answer_disk = ((disk_available_least / local_gb) * 100)
Disk = ("%.2f" % answer_disk)
print "Disk Percentage: " + "%.2f" % answer_disk + "%"

print "RECAP: "
print "RAM Utlization : " + Memory + "%"
print "VCPU Utlization: " + VCPU + "%"
print "DISK Utlization: " + Disk + "%"
