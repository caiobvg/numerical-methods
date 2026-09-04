from metodos import bisseccao

# D1

fluxo = [-1000, 300, 350, 400, 450]

def vpl(i):
    soma = 0
    for k, c in enumerate(fluxo):
        soma += c / (1 + i)**k
    return soma

tir, hist = bisseccao(vpl, 0.15, 0.20, eps=1e-6)

print("TIR = %.2f%% ao ano" % (tir * 100))