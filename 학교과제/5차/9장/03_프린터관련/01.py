import random

def new_print_task(num):
    return num / 3600

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm                    # 분당 출력 페이지 수
        self.current_task = None                # 수행 대상 인쇄 과제
        self.time_remaining = 0                 # 수행 대상 인쇄 과제 수행 시간

    # 수행중인 인쇄 과제 남은 수행 시간동안 busy 상태 유지
    def tick(self):
        if self.current_task is not None:     
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):                              # 프린터 상태
        return self.current_task is not None

    def start_next(self, new_task, num):              # 다음 인쇄 과제 불러오기
        self.current_task = new_task
        self.time_remaining = new_task.get_pages(num) * 60 / self.page_rate # 지정된 인쇄 과제 인쇄 시간 계산. 초단위.

class Task:
    def __init__(self, time):
        self.timestamp = time                   # 생성 시간
        self.pages = random.randrange(1, 20)    # 페이지 수

    def get_stamp(self):                        # 생성 시간 확인
        return self.timestamp

    def get_pages(self, num):                        # 페이지 수 확인
        return self.pages

    def waiting_time(self, current_time):          # 대기 시간
        return current_time - self.timestamp
    
class Task:
    def __init__(self, time):
        self.timestamp = time                   # 생성 시간
        self.pages = random.randrange(1, 21)    # 페이지 수

    def get_stamp(self):                        # 생성 시간 확인
        return self.timestamp

    def get_pages(self):                        # 페이지 수 확인
        return self.pages

    def waiting_time(self, current_time):          # 대기 시간
        return current_time - self.timestamp
    
def simulation(num_seconds, pages_per_minute, num):
    
    lab_printer = Printer(pages_per_minute)     # 프린터 생성
    print_queue = Queue()                       # 인쇄 과제 큐 생성
    waiting_times = []                          # 과제들의 대기시간 리스트

    # 모의실험 단계: 초당 수행 내용
    for current_second in range(num_seconds):
        # 새 인쇄 과제 생성 여부 판단 
        if new_print_task(num):
            task = Task(current_second)
            print_queue.enqueue(task)

        # 프린터가 대기 상태인 경우: 다음 인쇄 과제 지정, 대기 시간 계산, 과제 수행
        if (not lab_printer.busy()) and (not print_queue.is_empty()): 
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.waiting_time(current_second))
            lab_printer.start_next(nexttask, num)

        # 수행중인 과제 남은 시간 확인 후 프린터 상태 지정: busy 및 대기
        lab_printer.tick()

    # 인쇄 과제 평균 대기 시간 반환
    average_wait = sum(waiting_times) / len(waiting_times)

    return average_wait