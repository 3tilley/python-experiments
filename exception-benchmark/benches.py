import pyperf

INPUTS = [(4, 5), ("a", "b"), (4, "a")]
#INPUTS = [(4, 5), (2,2), (1,7)]
#INPUTS = [("4", 5), ("a", 2), ("4", 8)]
COUNT = 100000

def add_typesafe(a: str | int, b: str | int) -> str | int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return str(a) + str(b)

def add_exception(a: str | int, b: str | int) -> str | int:
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

def bench_typesafe():
    for i in range(COUNT):
        add_typesafe(*(INPUTS[i % 3]))
        
def bench_exceptions():
    for i in range(COUNT):
        add_exception(*(INPUTS[i % 3]))

runner = pyperf.Runner()
runner.bench_func(
    name="Type-checked addition",
    func=bench_typesafe,
    inner_loops=COUNT
) 

runner.bench_func(
    name="Exception-based addition",
    func=bench_exceptions,
    inner_loops=COUNT
)