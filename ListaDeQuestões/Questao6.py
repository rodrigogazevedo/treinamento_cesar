populationGrowthA = int(
    input("Digite a ordem de habitantes da população do país A: "))
populationGrowthB = int(
    input("Digite a ordem de habitantes da população do país B: "))

annualGrowthRateA = float(
    input("Informe a taxa anual de crescimento da população do país A: "))
annualGrowthRateA = annualGrowthRateA / 100
annualGrowthRateB = float(
    input("Informe a taxa anual de crescimento da população do país B: "))
annualGrowthRateB = annualGrowthRateB / 100

countYearPopulationGrowthA = 0
countYearPopulationGrowthB = 0

analysisPeriod = 100

while(populationGrowthB >= populationGrowthA):
    populationGrowthA = populationGrowthA + \
        (populationGrowthA * annualGrowthRateA)
    populationGrowthB = populationGrowthB + \
        (populationGrowthB * annualGrowthRateB)
    countYearPopulationGrowthA += 1
    countYearPopulationGrowthB += 1

print("A partir de {} ano(s) a população A é maior ou igual que a população B".format(
    countYearPopulationGrowthA))
