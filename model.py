import utils
import os


class model():
    def __init__(self):
        # gpu_info      [[gpu.id, gpu_memoryTotal, gpu.memoryUsed, gpu_memoryUtil, gpu_util]]
        self.gpu_list = utils.get_gpu_info()
        # cpu_info
        self.cpu_freq, self.cpu_util = utils.get_cpu_info()
        # memory_info
        self.used_memory, self.total_memory, self.free_memory, self.memory_percent = utils.get_memory_info()
        # disk info [[disk_name, total_size, free_disk_size]
        self.disk_list = utils.get_disk_info()

    def update(self):
        self.gpu_list = utils.get_gpu_info()
        self.cpu_freq, self.cpu_util = utils.get_cpu_info()
        self.used_memory, self.total_memory, self.free_memory, self.memory_percent = utils.get_memory_info()
        self.disk_list = utils.get_disk_info()

    def print_object(self):
        self.update()
        print('\n'.join(['%s:%s' % item for item in self.__dict__.items()]))
        print("-------------")

    def get_gpu_info(self):
        if self.gpu_list is None or len(self.gpu_list) == 0:
            return "No GPU detected!"
        info = ""
        for index, gpu in enumerate(self.gpu_list):
            info += f"{gpu[0]}   {gpu[1]}%  {gpu[2]}℃\n显存 {gpu[3]}/{gpu[4]}GB {gpu[5]}%"
            if index != len(self.gpu_list):
                info += "\n"
        return info

    def get_cpu_info(self):
        return f"CPU \n{self.cpu_util}% {self.cpu_freq.current/1000:.3}MHz"

    def get_memory_info(self):
        return f"内存 \n{self.used_memory}/{self.total_memory}GB({self.memory_percent}%)"

    def get_disk_info(self):
        info = ""
        for index, disk in enumerate(self.disk_list):
            info += f"{disk[0]}盘：{disk[2]}GB可用， 共{disk[1]}GB"
            if index != len(self.disk_list):
                info += "\n"
        return info


if __name__ == "__main__":
    m = model()
    os.system("cls")
    m.print_object()
