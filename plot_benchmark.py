import matplotlib.pyplot as plt
import matplotlib
import time

def plot_points(points, size=5, title="", x_label="", y_label=""):
    # Adapted from StackOverflow and matplotlib documentation example.    
    fig = plt.figure()
    fig.suptitle(title, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title('x / y axes proportion is linear')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    plt.scatter(*zip(*points), s=size)
    plt.show()

def plot_benchmark(procedure, size_range, input_generator=lambda x:x, tries=1):
    """
    @arg procedure: The procedure to plot the benchmark of.
    @arg size_range: The range of values the size of the inputs should take.
      Can be any iterable.
    @arg input_generator: `input_generator` is a function taking a number
      (let's call it `N`) as argument
      and returning a suitable input to the `procedure` of size = `N`.
      Deafault is identity function.
    @ tries: Times to run the procedure each time to reduce random noise if
      `input_generator is random`, defaults to 1.
    """
    points = []
    for size in size_range:
        start = time.time()
        for _ in range(tries):
            result = procedure(input_generator(size))
        points.append((size, (time.time() - start) / tries))
    plot_points(points,
                size=0.1,
                title="Benchmark of {}".format(procedure.__name__),
                x_label="Input size",
                y_label="Time in seconds")
        
if __name__ == "__main__":
    import random

    def random_bool_list(size):
        return [random.randint(0, 1) for _ in range(size)]
    def count_ones(lst):
        return lst.count(1)
    plot_benchmark(count_ones,
                   range(1, 1000, 10),
                   input_generator=random_bool_list,
                   tries=10)
    def all_pairs(lst):
        return [(x, y) for x in lst for y in lst]
    plot_benchmark(all_pairs,
                   range(1, 500, 1),
                   input_generator=random_bool_list,
                   tries=2)

