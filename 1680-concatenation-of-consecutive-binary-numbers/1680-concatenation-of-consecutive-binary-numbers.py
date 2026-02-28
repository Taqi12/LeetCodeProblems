class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaryString = "" #our result in form of a string
        for i in range(1,n+1):
            #cast integer i into binary, and then to string, and remove the "0b" component in the front
            binaryString += str(bin(i))[2:]
        #cast from binary to integer
        decimal = int(binaryString, 2)

        return decimal % 1000000007