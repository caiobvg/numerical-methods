import warnings


def contador(f):
    def wrapper(x):
        wrapper.n += 1
        return f(x)
    wrapper.n = 0
    return wrapper


def adicionar_historico(historico, k, x, fx, erro):
    historico.append({"k": k, "x": x, "fx": fx, "erro": erro})


def bisseccao(f, a, b, eps=1e-8, max_iter=200):
    fa = f(a)
    fb = f(b)

    # verifica mudanca de sinal no intervalo
    if fa * fb >= 0:
        raise ValueError("O intervalo não contém mudança de sinal: f(a) * f(b) >= 0.")

    historico = []
    x = (a + b) / 2

    for k in range(1, max_iter + 1):
        x = (a + b) / 2
        fx = f(x)
        erro = (b - a) / 2

        adicionar_historico(historico, k, x, fx, erro)

        # criterio de parada combinado
        if erro < eps or abs(fx) < eps:
            return x, historico

        #atualiza o intervalo evitando underflow numerico
        if (fa > 0) != (fx > 0):
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    warnings.warn(f"Bissecção atingiu {max_iter} iterações sem convergir.")
    return x, historico


def newton(f, df, x0, eps=1e-8, max_iter=200):
    x = x0
    fx = f(x)
    historico = []

    for k in range(1, max_iter + 1):
        dfx = df(x)

        #evita divisao por zero
        if dfx == 0:
            raise ValueError("Derivada nula encontrada na iteração.")

        x_novo = x - fx / dfx
        fx_novo = f(x_novo)
        erro = abs(x_novo - x)

        adicionar_historico(historico, k, x_novo, fx_novo, erro)

        # Criterio de parada combinado
        if erro < eps or abs(fx_novo) < eps:
            return x_novo, historico

        x = x_novo
        fx = fx_novo

    warnings.warn(f"Newton atingiu {max_iter} iterações sem convergir.")
    return x, historico


def secante(f, x0, x1, eps=1e-8, max_iter=200):
    fx0 = f(x0)
    fx1 = f(x1)
    historico = []

    for k in range(1, max_iter + 1):
        delta_f = fx1 - fx0

        #evita divisao por zero
        if delta_f == 0:
            raise ValueError("Denominador nulo na iteração da secante.")

        x_novo = x1 - fx1 * (x1 - x0) / delta_f
        fx_novo = f(x_novo)
        erro = abs(x_novo - x1)

        adicionar_historico(historico, k, x_novo, fx_novo, erro)

        # criterio de parada combinado
        if erro < eps or abs(fx_novo) < eps:
            return x_novo, historico

        #avanca os pontos para a proxima iteracao
        x0, x1 = x1, x_novo
        fx0, fx1 = fx1, fx_novo

    warnings.warn(f"Secante atingiu {max_iter} iterações sem convergir.")
    return x1, historico
