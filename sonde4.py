import psutil

print("Memoire par utilisateur")
users = []
mem = []
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['username', 'memory_percent'])
        users.append(pinfo['username'])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

users2 = []
for user in users:
    if user not in users2:
        users2.append(user)
#print(users)
#print(users2)
for j in users2:
    mem.append(0)
k = 0
for j in users2:
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['username', 'memory_percent'])
            if (pinfo['username'] == j):
                mem[k] = mem[k] + pinfo['memory_percent']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(j, "utilise", mem[k], "% de la mémoire")
    k = k + 1
print("Fin")
