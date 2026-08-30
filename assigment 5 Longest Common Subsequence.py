def build_lcs_table(seq1, seq2):
    """Fills the (m+1) x (n+1) DP grid using tabulation."""
    m, n = len(seq1), len(seq2)
    # Create a grid initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp

def reconstruct_lcs(dp, seq1, seq2):
    """Backtracks through the table to find the actual LCS sequence/string."""
    i, j = len(seq1), len(seq2)
    lcs_chars = []
    
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_chars.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    # Reverse because we backtracked from bottom-right to top-left
    if isinstance(seq1, str):
        return "".join(reversed(lcs_chars))
    else:
        return list(reversed(lcs_chars))

def lcs(seq1, seq2):
    """Main entry point returning length, subsequence, and the full dp table."""
    dp = build_lcs_table(seq1, seq2)
    length = dp[len(seq1)][len(seq2)]
    subsequence = reconstruct_lcs(dp, seq1, seq2)
    return length, subsequence, dp

def print_dp_table(dp, seq1, seq2):
    """Pretty-prints the DP grid with sequence headers."""
    print("\nDP Table:")
    header = [" ", " "] + list(seq2)
    print(" ".join(f"{c:>3}" for c in header))
    
    for i, row_char in enumerate([" "] + list(seq1)):
        row_vals = [str(val) for val in dp[i]]
        print(f"{row_char:>3} " + " ".join(f"{val:>3}" for val in row_vals))
    print()

def memoized_lcs(seq1, seq2):
    """Top-down DP approach using memoization for comparison."""
    memo = {}
    
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if seq1[i - 1] == seq2[j - 1]:
            memo[(i, j)] = 1 + helper(i - 1, j - 1)
        else:
            memo[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))
        return memo[(i, j)]

    return helper(len(seq1), len(seq2))

def brute_force_lcs(seq1, seq2):
    """Naive recursive approach (exponential time - use only for tiny inputs)."""
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if seq1[i - 1] == seq2[j - 1]:
            return 1 + helper(i - 1, j - 1)
        return max(helper(i - 1, j), helper(i, j - 1))
        
    return helper(len(seq1), len(seq2))

if __name__ == "__main__":
    # Classic example from lab presentation
    seq1 = "ABCBDAB"
    seq2 = "BDCABA"
    
    print(f"Comparing Sequence 1: {seq1}")
    print(f"Comparing Sequence 2: {seq2}")
    
    # 1. Tabulation Solution
    length, subsequence, dp_grid = lcs(seq1, seq2)
    print_dp_table(dp_grid, seq1, seq2)
    print(f"LCS Length: {length}")
    print(f"LCS Subsequence: {subsequence}")
    
    # 2. Verification using Memoization
    memo_len = memoized_lcs(seq1, seq2)
    print(f"Memoized Length (Verification): {memo_len}")
    
    # 3. Example using lists of words (Playlist analogy)
    playlist1 = ["walk", "to", "store", "buy", "milk"]
    playlist2 = ["drive", "to", "store", "buy", "some", "milk"]
    
    p_len, p_sub = lcs(playlist1, playlist2)
    print(f"\nPlaylist LCS Length: {p_len}")
    print(f"Playlist LCS Subsequence: {p_sub}")