def poly_acc(t_coefs, g_coefs):
    coefs_acc = [(1 - abs(t_coefs[i] - g_coefs[i]) / max(abs(t_coefs[i]), abs(g_coefs[i]), 1))
                 for i in range(len(t_coefs))]
    acc = sum(coefs_acc) / len(t_coefs)
    return round(acc * 100, 2)
