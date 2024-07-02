# Challenge 1

def longest_common_subsequence(X, Y, Z):
    results = {}
    
    
    def lcs_recursive(i, j, k):
        # if sequence is 0 - return ""
        if i == 0 or j == 0 or k == 0:
            return ""
        # if this case is already solve, return what we have in results.
        if (i, j, k) in results:
            return results[(i, j, k)]
        # if the current character is the same..
        if X[i - 1] == Y[j - 1] == Z[k - 1]:
            # we include that char in the result list.
            results[(i, j, k)] = lcs_recursive(i - 1, j - 1, k - 1) + X[i - 1]
        else:
            # We recalculate by excluding the last character of each sequence.
            lcs1 = lcs_recursive(i - 1, j, k)
            lcs2 = lcs_recursive(i, j - 1, k)
            lcs3 = lcs_recursive(i, j, k - 1)
            results[(i, j, k)] = max(lcs1, lcs2, lcs3, key=len)
        
        return results[(i, j, k)]
    # We call the recursive function
    return lcs_recursive(len(X), len(Y), len(Z))






# First test . OK 
X1 = "ADDB"
Y1 = "CDDE"
Z1 = "EDDF"
print(longest_common_subsequence(X1, Y1, Z1))  # Expected output: "DD" , Real output: "DD"

# Second test . KO 
X2 = "UIBAZDBSIAHFB"
Y2 = "PQACIZDBIBDLAG"
Z2 = "QIDBCZDBKSHDVF"
print(longest_common_subsequence(X2, Y2, Z2))  # Expected output: "ZDB" , Real output: "IZDB"