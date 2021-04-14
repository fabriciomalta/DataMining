import pandas as pd
import matplotlib.pyplot as plt

input_file = 'Datasets/echocardiogramclear.data'  # Importação dos Dados
df = pd.read_csv(input_file, usecols=[
                 'AgeAtHeartAttack', 'Pericardial-Effusion', 'alive-at-1'])
idade = df['AgeAtHeartAttack'].tolist()
effusao = df['Pericardial-Effusion'].tolist()
vivo = df['alive-at-1'].value_counts(sort=True)
print(vivo)
labels = 'Morreu', 'Sobreviveu','?'

plt.title('Pacientes')
plt.xlabel('idade')
plt.ylabel('Quantidade')
plt.hist(idade, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title('Efusão')
plt.xlabel('effusao')
plt.ylabel('Quantidade')
plt.hist(effusao, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title("Resultado se está vivo ou não")
plt.pie(vivo, labels=labels, autopct='%1.1f%%')
plt.show()
