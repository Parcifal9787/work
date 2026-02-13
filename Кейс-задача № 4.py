def best_dragon_power(N):
    power = [0] * (N + 1)
    power[0] = 1
    
    for i in range(1, N + 1):
        for k in range(1, min(i, 7) + 1):
            power[i] = max(power[i], power[i - k] * k)
    
    return power[N]

N = int(input("Введите количество голов имеющихся в драконьей стае (число N): "))
print("Наиболее рациональное распределение голов для максимальной силы стаи:", best_dragon_power(N))
