import time

class Timing:
    def __init__(self, func):
        self.num_runs = 100
        self.func = func

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func.__name__
        print("[Timing] Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, self.num_runs, avg))
        return self.func(*args, **kwargs)
@Timing
def foo(*args):
    for _ in range(*args):
        pass

def main():
    foo(int(input("Введите количество циклов работы функции за 1 запуск: ")))

if __name__ == "__main__":
    main()