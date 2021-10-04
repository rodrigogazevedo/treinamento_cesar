populationGrowthA = 80000
populationGrowthB = 200000

countYearPopulationGrowthA = 0
countYearPopulationGrowthB = 0

analysisPeriod = 100
#countYearPopulationGrowthA < analysisPeriod
while(populationGrowthB >= populationGrowthA):
    populationGrowthA = populationGrowthA + (populationGrowthA * 0.3)
    populationGrowthB = populationGrowthB + (populationGrowthB * 0.015)
    countYearPopulationGrowthA += 1
    countYearPopulationGrowthB += 1

print("A partir de {} ano(s) a população A é maior ou igual que a população B".format(
    countYearPopulationGrowthA))
