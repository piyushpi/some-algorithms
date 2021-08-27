# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    # pass
    found = True

    while True:
        if found == True and len(S)>1:

            # print(len(S))
            for i in range(0, len(S)-1):
                # if S[i] == 'A' and S[i+1] == 'B':
                # if (S[i] == 'B' and S[i+1] == 'A'):

                # print("running loop")

                # print(S)

                if (S[i] == 'B' and S[i+1] == 'A') or (S[i] == 'C' and S[i+1] == 'D') or (S[i] == 'D' and S[i+1] == 'C') or (S[i] == 'A' and S[i+1] == 'B'):
                # if (S[i] == 'B' and S[i+1] == 'A') or (S[i] == 'A' and S[i+1] == 'B'):
                    
                    print(S)
                    
                    if (i+2 < len(S)):
                        S = S[:i] + S[i+2:]
                    else:
                        print("edge")
                        S = S[:i]
                        # if len(S) <= 2:
                        #     S = ""
                    
                    found = True
                    break
                else:
                    found = False
            # found = False
        else:
            break
    return S

# print(solution("CDCDA"))

print("Solution is:", solution("ACBDACBDABABABBABABADCDCBDCBDCCDCDAAABBAACDBABC"))
print("Solution is:", solution("ABABABCABABABCDBCDA"))
print("Solution is:", solution("APPLE"))
print("complete")