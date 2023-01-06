import random
import statistics
from dataclasses import dataclass


@dataclass
class OutputResults:
    l1: int
    l2: int
    mean_1: float
    mean_2: float
    difference: float  # mean_2 - mean_1
    p_value: float  # if less than 0.05, we reject H0 that mean_1 == mean_2
    numer: int
    denom: int

    def __str__(self) -> str:
        return f"""
        {self.mean_1=} (n={self.l1})
        {self.mean_2=} (n={self.l2})
        {self.difference=}
        {self.p_value=} ({self.numer}/{self.denom})
        """


def get_pv(s1: list[float], s2: list[float]) -> OutputResults:
    """Get the p-value of uhhh"""
    reps = 50000

    m1 = statistics.mean(s1)  # control
    m2 = statistics.mean(s2)  # treatment

    l1 = len(s1)  # size of the control
    l2 = len(s2)  # size of the treatment

    diff_actual = m2 - m1
    combined = s1 + s2

    diff_means_collected = []

    for _ in range(0, reps):
        random.shuffle(combined)

        control_null = combined[:l1]
        treatment_null = combined[l1:]

        d1 = statistics.mean(treatment_null) - statistics.mean(control_null)
        diff_means_collected.append(d1)

    accum_counter = 0
    for item in diff_means_collected:
        # simulated diff greater than actual diff
        if abs(item) >= abs(diff_actual):
            accum_counter += 1

    p_value = accum_counter / len(diff_means_collected)

    return OutputResults(l1, l2, m1, m2, diff_actual, p_value,
                         accum_counter, len(diff_means_collected))


def str_seq_to_num_list(text: str) -> list[float]:
    splitted = [float(x.strip()) for x in text.strip().split('\n')]
    return splitted


def open_file(fp: str) -> str:
    with open(fp, 'r', encoding='UTF-8') as f:
        text = f.read()
    return text


def main() -> None:
    i1 = open_file('1control.txt')
    i2 = open_file('2treatment.txt')
    d = get_pv(str_seq_to_num_list(i1), str_seq_to_num_list(i2))
    print(d)


if __name__ == '__main__':
    main()
