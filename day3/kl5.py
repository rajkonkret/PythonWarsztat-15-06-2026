# longest_key() - ma wyszukac najdłuższy klucz

class LongestKeyDict(dict):

    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 14
art['zen'] = 9

print(art.longest_key())  # abraham


class LongestKeyDictMax(dict):
    def longest_key(self):
        return max(self.keys(), key=len, default=None)


art = LongestKeyDictMax()
art['tomasz'] = 12
art['abraham'] = 14
art['zen'] = 9

print(art.longest_key())  # abraham
