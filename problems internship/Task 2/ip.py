#ip adress
class Solution:
    def defangIPaddr(self, address: str) -> str:
        w = address.replace(".", "[.]")
        return w

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    address = "192.188.0.1"
    print(sol.defangIPaddr(address))
