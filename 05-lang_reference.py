
# Ternary Operator in Python
# <result_if_true> if <condition> else <result_if_false>
print(True if True else False)

# Lambdas are anonymous (undefined) functions
# Note no return value. The expression is returned immediately.
sqrt = lambda num: num ** 2
print(sqrt(3)) # 9

# Lambdas are sometimes stored in variables
sqrt_3 = lambda: 3 ** 2
print(sqrt_3()) # 9

# Lambdas are expressions (evaluate to a value), not statements.
# You can store a lambda in a list, unlike a "def" function
list = ['string', 99, lambda x: x * 2]
print(list[2](5)) # 10

# Lambdas are often used as callbacks
def invoker(callback):
    print callback(2)
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

# Lambdas can be returned by defined functions
def incrementor(num):
    return lambda x: num + x
print(incrementor(5)(3)) # 8