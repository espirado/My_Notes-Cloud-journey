def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: list) -> int:
    # Step 1: Sort the positions of the existing diners
    S.sort()
    
    # Step 2: Calculate gaps and possible new diners
    additional_diners = 0
    
    # Step 3: Check the gap before the first diner
    if S[0] - K > 1:
        additional_diners += (S[0] - K - 1) // (K + 1)
    
    # Step 4: Check gaps between diners
    for i in range(M - 1):
        left = S[i] + K + 1
        right = S[i + 1] - K - 1
        if left <= right:
            additional_diners += (right - left + 1) // (K + 1)
    
    # Step 5: Check the gap after the last diner
    if S[-1] + K < N:
        additional_diners += (N - (S[-1] + K)) // (K + 1)
    
    return additional_diners

# Test cases
def test_getMaxAdditionalDinersCount():
    assert getMaxAdditionalDinersCount(10, 1, 2, [2, 6]) == 3
    assert getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]) == 1
    print("All tests passed!")

if __name__ == "__main__":
    test_getMaxAdditionalDinersCount()
