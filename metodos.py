def adicionar_historico(historico, k, x, fx, erro):
    historico.append({"k": k, "x": x, "fx": fx, "erro": erro})


def bisseccao(f, a, b, eps=1e-8, max_iter=200):
    fa = f(a)
    fb = f(b)
    historico = []

    for k in range(1, max_iter + 1):
        x = (a + b) / 2
        fx = f(x)
        erro = (b - a) / 2

        adicionar_historico(historico, k, x, fx, erro)

        if erro < eps or abs(fx) < eps:
            return x, historico

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    return x, historico


def newton(f, df, x0, eps=1e-8, max_iter=200):
    x = x0
    historico = []

    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("derivada nula")

        x_novo = x - fx / dfx
        fx_novo = f(x_novo)
        erro = abs(x_novo - x)

        adicionar_historico(historico, k, x_novo, fx_novo, erro)

        if erro < eps or abs(fx_novo) < eps:
            return x_novo, historico

        x = x_novo

    return x, historico
