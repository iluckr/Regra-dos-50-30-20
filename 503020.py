user_wage = float(input("Para poder fazer a regra dos 50, 30 e 20, precisamos saber do seu salário. Quanto você recebe por mês? "))

#50%
a = 50 / 100
a *= user_wage
print("Você deve deixar R$",a,"para gastos essenciais, como, alimentação, saúde, transporte e moradia.")

#30%
b = 30 / 100
b *= user_wage
print("Você pode deixar R$",b,"para desejos pessoais, tipo, jogos, festas e etc.")

#20%
c = 20 / 100
c *= user_wage
print("Você deve deixar R$",c,"para investimentos, CDB Liquidez diária, Fundos imobiliários e talvez criptomoedas.")

print("Gastos essenciais - 50% =",a)
print("Desejos pessoais - 30% =",b)
print("Investimentos - 20% =",c)

input("")