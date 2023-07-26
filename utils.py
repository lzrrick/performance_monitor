import platform
import os
from distutils import spawn
from subprocess import Popen, PIPE, STARTUPINFO, STARTF_USESHOWWINDOW, SW_HIDE
import psutil


class GPU:
    def __init__(self, ID, uuid, load, memoryTotal, memoryUsed, memoryFree, driver, gpu_name, serial, display_mode, display_active, temp_gpu):
        self.id = ID
        self.uuid = uuid
        self.load = load
        self.memoryUtil = float(memoryUsed)/float(memoryTotal)
        self.memoryTotal = memoryTotal
        self.memoryUsed = memoryUsed
        self.memoryFree = memoryFree
        self.driver = driver
        self.name = gpu_name
        self.serial = serial
        self.display_mode = display_mode
        self.display_active = display_active
        self.temperature = temp_gpu


def safeFloatCast(strNumber):
    try:
        number = float(strNumber)
    except ValueError:
        number = float('nan')
    return number


def getGPUs():
    if platform.system() == "Windows":
        nvidia_smi = spawn.find_executable('nvidia-smi')
        if nvidia_smi is None:
            nvidia_smi = "%s\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" % os.environ['systemdrive']
    else:
        nvidia_smi = "nvidia-smi"
    # hide window
    st = STARTUPINFO()
    st.dwFlags = STARTF_USESHOWWINDOW
    st.wShowWindow = SW_HIDE
    try:
        p = Popen([nvidia_smi, "--query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature.gpu",
                  "--format=csv,noheader,nounits"],  stdin=PIPE, stdout=PIPE, stderr=PIPE, startupinfo=st)
        stdout, stderror = p.communicate()
    except:
        return []
    output = stdout.decode('UTF-8')
    lines = output.split(os.linesep)
    numDevices = len(lines)-1
    GPUs = []
    for g in range(numDevices):
        line = lines[g]
        vals = line.split(', ')
        for i in range(12):
            if (i == 0):
                deviceIds = int(vals[i])
            elif (i == 1):
                uuid = vals[i]
            elif (i == 2):
                gpuUtil = safeFloatCast(vals[i])/100
            elif (i == 3):
                memTotal = safeFloatCast(vals[i])
            elif (i == 4):
                memUsed = safeFloatCast(vals[i])
            elif (i == 5):
                memFree = safeFloatCast(vals[i])
            elif (i == 6):
                driver = vals[i]
            elif (i == 7):
                gpu_name = vals[i]
            elif (i == 8):
                serial = vals[i]
            elif (i == 9):
                display_active = vals[i]
            elif (i == 10):
                display_mode = vals[i]
            elif (i == 11):
                temp_gpu = safeFloatCast(vals[i])
        GPUs.append(GPU(deviceIds, uuid, gpuUtil, memTotal, memUsed, memFree,
                    driver, gpu_name, serial, display_mode, display_active, temp_gpu))
    return GPUs  # (deviceIds, gpuUtil, memUtil)


def get_gpu_info():
    gpulist = []

    for gpu in getGPUs():
        gpu_util = round(gpu.load * 100, 2)
        gpu_memory_total = round((gpu.memoryTotal) / 1024, 2)
        gpu_memory_used = round((gpu.memoryUsed) / 1024, 2)
        gpu_memory_util = round((gpu.memoryUtil) * 100, 2)
        gpulist.append(
            [gpu.id, gpu_util,  gpu_memory_used, gpu_memory_total, gpu_memory_util])
        # print(
        #     f"GPU:{gpu.id} {gpu_memory_total}G {gpu_memory_used}G {gpu_memory_util}%")
    return gpulist


def get_cpu_info():
    cpu_freq = psutil.cpu_freq()
    cpu_util = psutil.cpu_percent()
    # print(f"cpu_freq:{cpu_freq}")
    # print(f"cpu_percent:{cpu_percent}%")
    return cpu_freq, cpu_util


def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    used_memory = round(virtual_memory.used / (1024 * 1024 * 1024), 2)
    total_memory = round(virtual_memory.total / (1024 * 1024*1024), 2)
    free_memory = round(total_memory - used_memory, 2)
    memory_percent = round(virtual_memory.percent, 2)
    # print(f"total_memory:{total_memory} ")
    # print(f"used_memory:{used_memory } ")
    # print(f"free_memory:{free_memory}")
    # print(f"memory_percent:{memory_percent}%")
    return used_memory, total_memory, free_memory, memory_percent


def get_disk_info():
    disks = []
    for disk in psutil.disk_partitions():
        # 读写方式 光盘 or 有效磁盘类型
        if 'cdrom' in disk.opts or disk.fstype == '':
            continue
        disk_name_arr = disk.device.split(':')
        disk_name = disk_name_arr[0]
        disk_info = psutil.disk_usage(disk.mountpoint)
        total_size = round(disk_info.total / (1024 * 1024 * 1024))
        free_disk_size = round(disk_info.free / (1024 * 1024 * 1024))
        disks.append([disk_name, total_size, free_disk_size])
        # print(f"{disk_name}: total_size:{total_size}G free:{free_disk_size}G")

    return disks


if __name__ == "__main__":
    while True:
        get_cpu_info()
        print("---------------")
        get_memory_info()
        print("---------------")
        get_gpu_info()
        print("---------------")
        get_disk_info()
        print("---------------")
        break
