from app import Solution

def test_can_complete_circuit_basic():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    assert solution.canCompleteCircuit(gas, cost) == 3

def test_no_possible_start():
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    solution = Solution()
    assert solution.canCompleteCircuit(gas, cost) == -1

def test_single_station():
    gas = [5]
    cost = [4]
    solution = Solution()
    assert solution.canCompleteCircuit(gas, cost) == 0

def test_exact_match():
    gas = [2, 2, 2]
    cost = [1, 2, 3]
    solution = Solution()
    assert solution.canCompleteCircuit(gas, cost) == 2
