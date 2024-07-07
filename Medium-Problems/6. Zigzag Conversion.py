class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # The key for my thought process here was to keep it simple, at first I tried to do an overly complex
        # algorithm that ended up not working, stepping back and looking for patterns helped me to find this solution.

        # edge case:
        if numRows == 1:
            return s

        # Solution: create dictionary of letters and rows following this pattern:

        """
        Number of rows: 3
        PAYPALISHIRING
        12321232123212
        PAHNAPLSIIGYIR
        """

        """
        Number of rows: 4
        PAYPALISHIRING
        12343212343212
        PINALSIGYAHRPI
        """

        # then create new string row-by-row using this dictionary and return it

        # create dictionary:

        # need to create framework for rows:

        i = 1
        dict = {}
        while i <= numRows:
            dict[i] = []
            i += 1

        count = 1
        ascend = True
        for char in s:
            dict[count].append(char)

            # check if we should be ascending or descending in rows:
            if count == numRows and ascend:
                ascend = False
            if count == 1 and not ascend:
                ascend = True

            # increase or decrease row depending if we're ascending or not:
            if ascend:
                count += 1
            if not ascend:
                count -= 1

        # now that we have a dictionary of the rows, we need to create the new string:

        result = ""
        i = 1
        while i <= numRows:
            for char in dict[i]:
                result += char
            i += 1

        return result
