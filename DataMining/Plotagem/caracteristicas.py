import pandas as pd
import statistics
import matplotlib.pyplot as plt

input_file = 'Datasets/echocardiogramclear.data'
df = pd.read_csv(input_file)
columns = list(df.columns)

idade = df['AgeAtHeartAttack'].tolist()
idadeordenada = sorted(df['AgeAtHeartAttack'].tolist())

idadeMedia = df['AgeAtHeartAttack'].mean()
idadeModa = df['AgeAtHeartAttack'].mode()
idadeMediana = statistics.median(idade)
idadePontoMedio = (
    idadeordenada[0] + idadeordenada[len(idadeordenada)-1])/2

print("Média de pessoas que sofreram de ataques cardíacos no estudo")
print("Média = " + str(idadeMedia))
print("Moda = " + str(idadeModa[0]))
print("Mediana = " + str(idadeMediana))
print("Ponto Médio = " + str(idadePontoMedio))

idadeAmplitude = idadeordenada[len(
    idadeordenada)-1] - idadeordenada[0]
idadeDesvioPadrao = statistics.pstdev(idade)
idadeVariancia = statistics.pvariance(idade)
idadeCoeficienteVariacao = (idadeDesvioPadrao/idadeMedia)*100

print("\nMedidas de dispersão da idade dos pacientes registrados")
print("Amplitude = " + str(idadeAmplitude))
print("Desvio Padrão = " + str(idadeDesvioPadrao))
print("Variância = " + str(idadeVariancia))
print("Coeficiente de Variação = " +
      str(round(idadeCoeficienteVariacao, 2)) + "%\n")

idade = df['AgeAtHeartAttack']
idade_descri = idade.describe()

q1 = idade_descri['25%']
mediana = idade_descri['50%']
q2 = idade_descri['75%']

s_q1 = "{0:.2f}".format(q1)
s_mediana = "{0:.2f}".format(mediana)
s_q2 = "{0:.2f}".format(q2)

font_1 = {'family': 'serif', 'color': 'darkred', 'size': '14'}

plt.figure(figsize=(6, 7))
plt.boxplot(idade)
plt.title('Boxplot Batimentos Cardíacos')
plt.text(1, q1, s_q1, fontdict=font_1)
plt.text(1, mediana, s_mediana, fontdict=font_1)
plt.text(1, q2, s_q2, fontdict=font_1)
plt.ylabel('Idade')
plt.show()
