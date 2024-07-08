class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        """
        Solution: We can isolate out specific digits by using modulo 10 and shifting x down by diving by 10 each digit
                  that we get. We do the inverse to our result (as we are reversing x) by shifting the last digit added
                  up by multiplying by 10 and then adding the digit we isolated from x. Note that the digit should be 
                  removed from x when it is isolated so that we dont get it as a decimal in the next digit
                  
        Time Complexity: O(Log(X))
        
        """

        negative = False

        # check for sign:
        if str(x)[0] == "-":
            negative = True
            x = int(str(x)[1:])

        size = len(str(x))
        i = 1
        result = 0
        while i < size + 1:
            # get the current digit of x we want:
            num = x%(10)

            # push last digit up
            result = result*10

            # add current digit
            result += num

            # remove current digit from x
            x -= x%(10)

            # shift x down 1 place
            x //= 10
            i += 1

        # apply sign if necessary
        if negative:
            result = -1 * result

        # edge cases: result is less/greater than -2^31 or 2^31 - 1
        if result < (-2**31) or result > (2**31) - 1:
            return 0

        else:
            return result