def sum_two_array(L1, L2):
    carry, total = 0, 0
    m, n = len(L1), len(L2)
    k   = max(m, n)
    
    result = [0] + [0] * k  # add +1 

    for i in range(1, k+1):
        a = L1[m-i] if m - i >= 0 else 0
        b = L2[n-i] if n - i >= 0 else 0
     
        total = a + b + carry
        result[k-i + 1] = total % 10
        carry = total // 10
    
    if carry > 0: result[0] = carry
    
    return result if result[0] != 0 else result[1:]

if __name__ == '__main__':
    L1 = [int(x) for x in input().split()]
    L2 = [int(x) for x in input().split()]

    print(sum_two_array(L1, L2))
