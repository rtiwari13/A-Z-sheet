class Solution:
    def studentGrade(self, marks):
        print("Enter marks")
        marks = int(input())
        if marks >= 90:
            print("Grade A")
        elif marks >=70 :
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        elif marks >= 34:
            print("Grade D")
        else:
            print("Fail")

sol = Solution()
sol.studentGrade(0)  # The argument is not used, input is taken inside the method
