Running the UDP protocol:

   * Extract the zip file and find 'udp_client.py' and 'udp_server.py'
   * Navigate to the file directory and run the file using the command "python udp_server.py" on the terminal
   * First run the file udp_server.py and if the file successfully runs it would display "The server is ready to receive"
   * After getting that message run "udp_client.py" on the terminal using "python udp_client.py"
   * This would prompt the user to enter the length followed by numbers (separated by comma)
   * While entering the numbers make sure you don't add spaces in between
   * Enter the length and the numbers separated by comma and hit enter after done
   * The output would be displayed with Max, Min, Mean, and Sum in the order.
  
Running the TCP Protocol:

   * Extract the zip file and find 'tcp_client.py' and 'tcp_server.py'
   * Navigate to the file directory and run the file using the command "python tcp_server.py" on the terminal
   * First run the file tcp_server.py and if the file successfully runs it would display "The server is ready to receive"
   * After getting that message run "tcp_client.py" on the terminal using "python tcp_client.py"
   * This would prompt the user to enter the length followed by numbers (separated by comma)
   * While entering the numbers make sure you don't add spaces in between
   * Enter the length and the numbers separated by comma and hit enter after done
   * The output would be displayed with Max, Min, Mean, and Sum in the order.
   
Test Cases for UDP:
    
    Enter the numbers: "1,3,8,12,9"
    Output: Invalid Length
    Expected Output: Invalid Length
    
    Enter the numbers: "4,-1,-4,-8,13455"
    Output: ('Max: ', 13455, 'Min: ', -8, 'Mean: ', 3360.5, 'Total: ', 13442)
    Expected Output: ('Max: ', 13455, 'Min: ', -8, 'Mean: ', 3360.5, 'Total: ', 13442)
    
    Enter the numbers: "dfsd,fsdfsdf,fsdfsd"
    Output: Invalid
    Expected Output: Invalid
    
    Enter the numbers: "5,2,4,7,5666,afdf"
    Output: Invalid
    Expected Output: Invalid
    
    Enter the numbers:  "3, 4 , 5 , 6"
    Output: Invalid
    Expected Output: Invalid
    
Test Cases for TCP:    
    
    Enter the numbers: "1,3,8,12,9"
    Output: "From Server:  Invalid Length"
    Expected Output: "From Server:  Invalid Length"
    
    Enter the numbers: "4,-1,-4,-8,13455"
    Output: From Server:  ('Max: ', 13455, 'Min: ', -8, 'Mean: ', 3360.5, 'Total: ', 13442)
    Expected Output: From Server:  ('Max: ', 13455, 'Min: ', -8, 'Mean: ', 3360.5, 'Total: ', 13442)
    
    Enter the numbers: "dfsd,fsdfsdf,fsdfsd"
    Output: From Server:  Invalid
    Expected Output: From Server:  Invalid
    
    Enter the numbers: "5,2,4,7,5666,afdf"
    Output: From Server:  Invalid
    Expected Output: From Server:  Invalid
    
    Enter the numbers:  "3, 4 , 5 , 6"
    Output: From Server:  Invalid
    Expected Output: From Server:  Invalid
    