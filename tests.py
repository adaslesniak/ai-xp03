from linearity_check import linearity_check
from test_data import described_test_data


def test_data(to_be_tested, test_name):
    result = linearity_check(to_be_tested)
    print(f'score for {test_name} is {result}')


print("------- testing linearity check -------")
test_cases = described_test_data()
for case in test_cases:
    test_data(test_cases[case], case)