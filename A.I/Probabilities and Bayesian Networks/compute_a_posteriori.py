
import sys

value = sys.argv[1]
length_input = len(value)

H_P_ = []
for i in range(0, length_input + 1):
    block = {}
    for j in range(1, 6):
        block[j] = 0
    H_P_.append(block)

# Initial probability for five possible hypotheses for our bag are (h1, h2, h3, h4, h5):
H_P_[0][1] = 0.1 #h1
H_P_[0][2] = 0.2 #h2
H_P_[0][3] = 0.4 #h3
H_P_[0][4] = 0.2 #h4
H_P_[0][5] = 0.1 #h5

# Initial probability of Q (C or L)
C_P_givenQ = {}
L_P_GivenQ = {}

# Initial probability of Cherry given hypotheses (h1, h2, h3, h4, h5)
C_P_ = {}
C_P_[1] = 1
C_P_[2] = 0.75
C_P_[3] = 0.5
C_P_[4] = 0.25
C_P_[5] = 0

# Initial probability of Lime given hypotheses (h1, h2, h3, h4, h5)
L_P_ = {}
L_P_[1] = 0
L_P_[2] = 0.25
L_P_[3] = 0.5
L_P_[4] = 0.75
L_P_[5] = 1



# This will open a txt file by the name result.txt to store output
f = open('result.txt', 'w')
f.write ("Observation sequence Q: " + value + "\n")
f.write ("Length of Q: " + str(length_input) + "\n\n")

C_P_givenQ[0] = H_P_[0][1] * C_P_[1] + H_P_[0][2] * C_P_[2] + H_P_[0][3] * C_P_[3] + H_P_[0][4] * C_P_[4] + H_P_[0][5] * C_P_[5]
L_P_GivenQ[0] = H_P_[0][1] * L_P_[1] + H_P_[0][2] * L_P_[2] + H_P_[0][3] * L_P_[3] + H_P_[0][4] * L_P_[4] + H_P_[0][5] * L_P_[5]

i = 1
for letter in value:
    f.write ("After Observation " + str(i) + " = " + letter + ":\n\n")
    if letter == "C":
        C_P_givenQ[i] = 0
        for j in range(1, 6):
            H_P_[i][j] = (C_P_[j] * H_P_[i-1][j]) / C_P_givenQ[i-1]
            C_P_givenQ[i] = C_P_givenQ[i] + (H_P_[i][j] * C_P_[j])
            f.write ("P(h" + str(j) + " | Q) = " + str(round(H_P_[i][j], 5)) + "\n")
        L_P_GivenQ[i] = 1-C_P_givenQ[i]
        f.write ("\nProbability that the next candy we pick will be C, given Q: " + str(round(C_P_givenQ[i], 5)) + "\n")
        f.write ("Probability that the next candy we pick will be L, given Q: " + str(round(L_P_GivenQ[i], 5)) + "\n\n")

    elif letter == "L":
        L_P_GivenQ[i] = 0
        for j in range(1, 6):
            H_P_[i][j] = (L_P_[j] * H_P_[i-1][j]) / L_P_GivenQ[i-1]
            L_P_GivenQ[i] = L_P_GivenQ[i] + (H_P_[i][j] * L_P_[j])
            f.write ("P(h" + str(j) + " | Q) = " + str(round(H_P_[i][j], 5)) + "\n")
        C_P_givenQ[i] = 1 - L_P_GivenQ[i]
        f.write ("\nProbability that the next candy we pick will be C, given Q: " + str(round(C_P_givenQ[i], 5)) + "\n")
        f.write ("Probability that the next candy we pick will be L, given Q: " + str(round(L_P_GivenQ[i], 5)) + "\n\n")
    i = i + 1
f.close()
# End of Program
