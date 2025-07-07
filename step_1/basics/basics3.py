class Solution:
    def whichWeekDay(self, day):
        print("Enter a number value ")
        value = int(input())

        if value >7 or value <1 :
            print("Invalid value")
            return
        
        # using a dictionary as switch 

        def day1():
            return "Monday"

        def day2():
            return "Tuesday"

        def day3():
            return "Wednesday"

        def day4():
            return "Thursday"

        def day5():
            return "Friday"

        def day6():
            return "Saturday"

        def day7():
            return "Sunday"
        
        day_dictionary = {
            1:day1,
            2:day2,
            3:day3,
            4:day4,
            5:day5,
            6:day6,
            7:day7
            
        }

        print("The day is:", day_dictionary[value]())
        
    # Use match statement (Structural Pattern Matching)
    # def grade(marks):
    #     match marks:
    #         case _ if marks >= 90:
    #             return "Grade A"
    #         case _ if marks >= 70:
    #             return "Grade B"
    #         case _ if marks >= 50:
    #             return "Grade C"
    #         case _:
    #             return "Fail"

    # print(grade(85))  # Output: Grade B

sol = Solution()
sol.whichWeekDay(0)
