from bug.Resources import Resources, TypeSpend, ResourceTable

resource = Resources()
data={"base_spend": TypeSpend("base_spend", 20, 3), "base_add": TypeSpend("base_add", 6, 2)}
resourceTable=ResourceTable()
resourceTable.set_init_data(data)
print(resource.money, resource.population)

resource.add_resources("base_add")
resource.add_resources("base_add")
resource.add_resources("base_add")
resource.add_resources("base_add")

print(resource.money, resource.population)

resource.spend("base_spend")
resource.spend("base_spend")
spends=resource.sum_apend()
print(spends.money,spends.population)
spends = resource.rest_resource()
resource.spend("base_spend")

print(spends.money,spends.population)

