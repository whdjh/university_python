import numpy as np
import random

for _ in range(5):
    print(random.randrange(1, 121))


def new_casher_task():
    num = random.randrange(1, 121)

    return num == 120


class Casher:
    def __init__(self, cpm):
        self.catalogue_rate = cpm  # 분당 계산 횟수
        self.current_task = None  # 수행 대상 계산할것
        self.time_remaining = 0  # 수행 대상 계산 수행 시간

    # 수행중인 계산 남은 수행 시간동안 busy 상태 유지
    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):  # 계산기 상태
        return self.current_task is not None

    def start_next(self, new_task):  # 다음 계산할것 불러오기
        self.current_task = new_task
        # 지정된 계산할 것들 계산 시간 계산. 초단위.
        self.time_remaining = new_task.get_catalogue() * 60 / self.catalogue_rate


class Task:
    def __init__(self, time):
        self.timestamp = time  # 생성 시간
        self.catalogues = random.randrange(1, 31)  # 계산할것들 개수

    def get_stamp(self):  # 생성 시간 확인
        return self.timestamp

    def get_catalogue(self):  # 계산할것들의 수 확인
        return self.catalogues

    def waiting_time(self, current_time):  # 대기 시간
        return current_time - self.timestamp


def simulation(num_seconds, casher_per_minute):

    comunity_Casher = Casher(casher_per_minute)  # 계산기 생성
    casher_queue = Queue()  # 계산할것 큐 생성
    waiting_times = []  # 계산할것들의 대기시간 리스트

    # 모의실험 단계: 초당 수행 내용
    for current_second in range(num_seconds):
        # 새 계산 생성 여부 판단
        if new_casher_task():
            task = Task(current_second)
            casher_queue.enqueue(task)

        # 계산기가 대기 상태인 경우: 다음 계산 지정, 대기 시간 계산, 과제 수행
        if (not comunity_Casher.busy()) and (not casher_queue.is_empty()):
            nexttask = casher_queue.dequeue()
            waiting_times.append(nexttask.waiting_time(current_second))
            comunity_Casher.start_next(nexttask)

        # 수행중인 계산 남은 시간 확인 후 프린터 상태 지정: busy 및 대기
        comunity_Casher.tick()

    # 계산 평균 대기 시간 반환
    average_wait = sum(waiting_times) / len(waiting_times)

    return average_wait


average_wait_list = []
# 분당 5개를 계산하는 계산기를 1시간동안 모의실험 100번 돌림
for i in range(100):
    average_wait_list.append(simulation(3600, 5))

print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


average_wait_list = []
# 분당 10개를 계산하는 계산기를 1시간동안 모의실험 100번 돌림
for i in range(100):
    average_wait_list.append(simulation(3600, 10))

print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


average_wait_list = []
# 분당 20개를 계산하는 계산기를 1시간동안 모의실험 100번 돌림
for i in range(100):
    average_wait_list.append(simulation(3600, 20))

print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


average_wait_list = []
# 분당 30개를 계산하는 계산기를 1시간동안 모의실험 100번 돌림
for i in range(100):
    average_wait_list.append(simulation(3600, 30))

print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")
