        #This variable is used to give each staff request a number. 
        #The Kiss (Keep It Simple, Stupid) concept is followed because the reasoning is simple and straightforward

staff_counter = 1000

class RequisitionSystem:
    def __init__(self):
        #This method inserts data of requisition  such as the date, staff ID, staff name, status, requisition ID, overall cost and approval reference
        #It follows the principle of Single Responsibility because it simply declares the existence of those variables
        #It follows the principle of the Clean Code because the names of these variables are short and easy to read

        date = "date"
        staff_id="staff_id"
        staff_name="staff_name"
        status = 0
        requisition_id = 0
        total_cost = 0
        approval_reference_number = 0
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.status = status
        self.requisition_id = requisition_id
        self.total_cost = total_cost
        self.approval_reference_number = approval_reference_number

    def staff_info(self):

        #This process gathers information about the staff including date, staff id and staff name.

        global staff_counter
        print("Printing Requisitions:")
        self.date = input("Enter a date: ")

        self.staff_id = input("Enter a staff ID: ")
        self.staff_name = input("Enter a staff name: ")
        staff_counter += 1
        self.requisition_id = staff_counter
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")

        #It follows  the Kiss principle as it is simple and just collects the staff information. 
        # It also follows the Dry principle as it does not repeat the same code and they have the information all in one method.
        

    def requisitions_details(self):
        #This process is done by asking the employees to indicate the number of products they  want to purchase.
        #The products name and price will then be determined and added up to create the total price.

        self.staff_info()
        self.total_cost = 0
        number = int(input("Enter the number of products: "))
        for i in range(number):
            product = input("Enter the name of products: ")
            cost = float(input("please enter the cost of products: $"))
            self.total_cost += cost
            print(f" Total = ${self.total_cost}")

        #It follows the dry principle as all the cost calculations are performed in this section because the logic is straightforward 
        # all i have to do is loop through the products and sum up the costs.


    def requisition_approval(self):

        #This process determines the requisition that is approved, pending or not approved based on the overall cost. 
        #When it is less than 500, Approved; When 500 to 1000, Pending; When it is greater than 1000, Not Approved.

        self.requisitions_details()
        if self.total_cost < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.requisition_id)[2:5]
        elif 500 <= self.total_cost <= 1000:
            self.status = "pending"
        else:
            self.status = "Not Approved"
            print(f"status: {self.status}")
        if self.status == "Approved":
            print(f"Approval Reference Number: {self.approval_ref}")

        #This is with the principle of Kiss as the rule is brief, concise and simple.

    def respond_requisitions(self):
        #This  is applied in the case of a Pending requisition
        #It gives the manager to give a final decision which can be Approved, Not Approved, or Pending

        
        if self.status == "Pending":
            decision = input(f"decision for requisition {self.requisition_id} (Approved /Not Approved/Pending): ")
            if decision.lower() == "approved":
                self.status = "Approved"
                self.approval_ref = self.staff_id + str(self.requisition_id)[2:5]
                RequisitionSystem.approved += 1
                RequisitionSystem.pending-= 1
            elif decision.lower() == "not approved":
                self.status = "Not approved"
                RequisitionSystem.not_approved += 1
                RequisitionSystem.pending -= 1
            else:
                print("Pending.")

        #It is based on the principle of Separation of Concerns because this approach does not address  other activities such as input or cost calculations
        #It only deals with the decision-making  process


    def display_requisitions(self):
        
        # all the details of a requisition displays  on a screen
        # It  follows the Dry principle since i don't need to repeat the print statements in the various functions
        #  It also follows to the Clean Code since the output is fully arranged and is suitable to read by any person
        
        print("printing Requisitions: ")
        print(f"date:{self.date}")
        print(f"requisition_id:{self.requisition_id}")
        print(f"staff_id:{self.staff_id}")
        print(f" Total cost = ${self.total_cost}")
        print(f"status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref}")

    def requisition_statistics(self):
        #the total statistics of all requisitions; the number of those submitted, approved, pending, or not approved will be seen. 
        # It follows to the Single Responsibility principle since it only works with displaying statistics and nothing more.
        #  It is also based on the YAGNI (You Aren't Gonna Need It) principle since it only includes the statistics which are actually needed at the moment but not the additional features
    
        print("\n Requisition Statistics")
        print(f"Total Requisitions Submitted: {RequisitionSystem.total_requisitions}")
        print(f"Approved: {RequisitionSystem.approved}")
        print(f"Pending: {RequisitionSystem.pending}")
        print(f"Not Approved: {RequisitionSystem.not_approved}")



        # It gathers the information of the staff first
        # asks the information about the product then verifies the requisition is approved or not and finally presents the statistics

student = RequisitionSystem()
student.staff_info()
student.requisitions_details()   
student.requisition_approval()
student.respond_requisitions()
student.display_requisitions()
student.requisition_statistics()

        # follows the Refactor principle because i can later test and make improvements to the program, without making any changes



    