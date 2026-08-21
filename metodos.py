def bisseccao(f, a, b, eps=1e-8, max_iter=200):
    fa = f(a)
    fb = f(b)

    for k in range(1, max_iter + 1):
        x = (a + b) / 2
        fx = f(x)

        if (b - a) / 2 < eps or abs(fx) < eps:
            return x

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    return x
