def lcsRec(s1, s2, m, n):
    # Base case: if either string is empty
    if m == 0 or n == 0:
        return 0, ""

    # If last characters match
    if s1[m - 1] == s2[n - 1]:
        length, subseq = lcsRec(s1, s2, m - 1, n - 1)
        return length + 1, subseq + s1[m - 1]

    # If last characters don't match, check both possibilities
    len1, subseq1 = lcsRec(s1, s2, m, n - 1)
    len2, subseq2 = lcsRec(s1, s2, m - 1, n)

    if len1 > len2:
        return len1, subseq1
    else:
        return len2, subseq2

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    return lcsRec(s1, s2, m, n)

if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    length, subsequence = lcs(s1, s2)
    print("Length of LCS:", length)
    print("Longest Common Subsequence:", subsequence)
