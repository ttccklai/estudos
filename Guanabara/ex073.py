times_brasileirao_vencedores = (
    "Palmeiras",      # 12 títulos
    "Santos",         # 8 títulos
    "Corinthians",    # 7 títulos
    "Flamengo",       # 7 títulos
    "São Paulo",      # 6 títulos
    "Cruzeiro",       # 4 títulos
    "Vasco da Gama",  # 4 títulos
    "Fluminense",     # 4 títulos
    "Internacional",  # 3 títulos
    "Grêmio",         # 2 títulos
    "Atlético-MG",    # 2 títulos
    "Bahia",          # 2 títulos
    "Botafogo",       # 2 títulos
    "Athletico-PR",   # 1 título
    "Guarani",        # 1 título
    "Coritiba",       # 1 título
    "Sport",          # 1 título
    "Atlético-PR",    # 1 título
)

print(f"Os 5 primeiros colocados do Brasileirão são: {times_brasileirao_vencedores[:5]}")
print(f"Os 4 últimos colocados do Brasileirão são: {times_brasileirao_vencedores[-4:]}")
print(f" Os times em ordem alfabetica são: {sorted(times_brasileirao_vencedores)}")
print(f"O fluminense está na {times_brasileirao_vencedores.index('Fluminense') + 1}ª posição.")