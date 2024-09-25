from chapter_02.linked_list import LinkedList


def kth_to_last(ll, k):
    leader = follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    return follower


# O(N) space
def kth_last_recursive(ll, k):
    head = ll.head
    counter = 0

    def helper(head, k):
        nonlocal counter
        if not head:
            return None
        helper_node = helper(head.next, k)
        counter = counter + 1
        if counter == k:
            return head
        return helper_node

    return helper(head, k)


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  #sort the position of existing dinners
  S.sort()
  
  #calculate gaps and possibility for first dinners
  additional_dinners = 0
  
  
  if S[0] > K+1:
    additional_dinners += (S[0] - 1) // (K+1)

  #check gap between dinners 
  for i in range(1, M):
    gap = S[i] - S [i -1] -1 
    if gap > 2* K:
      additional_dinners +=( gap -2 * K) // ( K+1)
      
    #last gap
    
    
    if N - S[-1] > K :
      additional_dinners+= (N - S[-1]) // (K+1)
  
      
      
  return additional_dinners