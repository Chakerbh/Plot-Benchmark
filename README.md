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
      
## @arg `tries`: Times to run the procedure each time to reduce random noise if
      `input_generator is random`, defaults to 1.
 
