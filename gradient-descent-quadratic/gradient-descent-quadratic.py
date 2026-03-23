def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    x = x0
    
    for _ in range(steps):
        grad = 2*a*x + b   # derivative
        x = x - lr * grad  # update rule
    
    return float(x)