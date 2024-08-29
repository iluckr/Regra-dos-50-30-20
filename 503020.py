user_wage = float(input("Para poder fazer a regra dos 50, 30 e 20, precisamos saber do seu salário. Quanto você recebe por mês? "))

#50%
a = 50 / 100
a *= user_wage
print(f"Você deve deixar R${a:.2f} para gastos essenciais, como, alimentação, saúde, transporte e moradia.")

#30%
b = 30 / 100
b *= user_wage
print(f"Você pode deixar R${b:.2f} para desejos pessoais, tipo, jogos, festas e etc.")

#20%
c = 20 / 100
c *= user_wage
print(f"Você deve deixar R${c:.2f} para investimentos, CDB Liquidez diária, Fundos imobiliários e talvez criptomoedas.")

print(f"Gastos essenciais - 50% = {a:.2f}")
print(f"Desejos pessoais - 30% = {b:.2f}")
print(f"Investimentos - 20% = {c:.2f}")

input("")
