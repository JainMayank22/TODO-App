def minSwaps(self, data):
        counts_ones = 0
        steps = 0
        for i in data:
            if i == 1:
                counts_ones += 1
            if i == 0:
                steps += counts_ones
        counts_zeros = len(data) - counts_ones
        steps_reverse = counts_ones*counts_zeros - steps
        print(steps)
        print(steps_reverse)
        return min([steps,steps_reverse])