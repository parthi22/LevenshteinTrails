from fuzzywuzzy import fuzz
from fuzzywuzzy import process

string1 = input("Enter String1 to compare:\t")
string2 = input("Enter String2 to compare:\t")
editDistance =  fuzz.ratio(string1, string2)
bestPartial = fuzz.partial_ratio(string1, string2)
tokenSortRatio = fuzz.token_sort_ratio(string1, string2)
tokenSetRatio = fuzz.token_set_ratio(string1, string2)
print("\nEdit Distance:\t" + str(editDistance))
print("\nBest Partial:\t" + str(bestPartial))
print("\nToken Sort Ratio:\t" + str(tokenSortRatio))
print("\nToken Set Ratio:\t" + str(tokenSetRatio))