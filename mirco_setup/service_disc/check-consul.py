import consul
cons = consul.Consul(host='localhost', port=8500)
print(cons.status.leader())