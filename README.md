# Plot-Benchmark
This Python library plots the benchamark of a given procedure.

The main function to use in your project is `plot_benchmark` and here you can see its signature and documenation:

    def plot_benchmark(procedure, size_range, input_generator=lambda x:x, tries=1):
    
    
## @arg `procedure`: 
  The procedure to plot the benchmark of.

## @arg `size_range`:
  The range of values the size of the inputs should take.
      Can be any iterable.
      
## @arg `input_generator`: 
  `input_generator` is a function taking a number
      (let's call it `N`) as argument
      and returning a suitable input to the `procedure` of size = `N`.
      Deafault is identity function.
      
## @arg `tries`: 
  Times to run the procedure each time to reduce random noise if
      `input_generator is random`, defaults to 1.
 
# Examples

An example usage ready to be copy-pasted for you to start learning how to use this function:


    from plot_benchamrk import plot_benchmark
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
