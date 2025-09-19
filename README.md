
1.	Program overview
   
	This program is regarding requisition system by which staff can request products, and the program will determine whether they will be approved, pending, or not approved. I have provided comments in the code to demonstrate how various software design principles are applied and here I would summarize them.

3.	Staff counter
   
	The program begins with a variable known as staff counter that gives every staff requisition a number. This is in line with the Kiss (Keep It Simple, Stupid) since the reason is straightforward and simple to understand. The number is higher by one, so it is easy to follow individual requisitions.

5.	Initialization
   
	The __init method within RequisitionSystem class would take care of establishing the simple variables date, staff ID, staff name, requisition ID, cost and approval reference number. This is founded on the Single Responsibility Principle because the method only deals with the declaration of variables. It also follows the Clean Code principles because the names of the variables are short and simple to read.

7.	Staff Information Method
   
	The staff information method gathers the information of the staff including the date, staff ID, and name of staff. It is in line with the KISS principle one more time because it only collects the information and does not introduce any additional processes. It also uses the DRY (Don’t Repeat Yourself) concept since all the staff information is processed in a single location rather than the duplication of code with other processes.

9.	Requisition Details Method
    
	The requisitions details method enables to input the quantity of products and product prices. It then divides the sum of price. This is simple and once again demonstrates the DRY principle since the calculation of the costs is all within a single method.

11.	Requisition Approval Procedure
    
     The requisition approval procedure determines approval, pending or not approval of the request based on the overall cost. The approval is less than $500, pending approval between $500 and $1000, and not approved more than $1000. This once again applies to KISS because the rules are straightforward and plain.

13.	Respond to Requisitions Method
    
	The respond to requisitions method is used to deal with outstanding requests. It enables a manager to make final decision. This is according to the Separation of Concerns principle since the only aspect it is concerned with the decision-making and does not concern itself with the calculation of costs or the details of its staff.

15.	Display Requisitions Procedure
    
	The display requisitions procedure displays all the information of the requisition in a tabular manner. It follows to the DRY and Clean Code as the output is organized and readable.

17.	Requisition statistics Method
    
	Lastly, the requisition statistics method displays the number of requisitions submitted, approved, pending and not approved. This is in accordance with the Single Responsibility principle because it is the only one that shows statistics. It is also using the YAGNI (You Aren’t Gonna Need It) principle since it does not add any features to the product unless needed.

19.	Refactoring and Future Improvements
    
	All in all, the program can be refined and tested in future, which is also aligned with Refactor principle. This makes the code more adaptable and less difficult to keep.


