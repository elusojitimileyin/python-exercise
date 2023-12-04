print("NOKIA PHONE MENU")
userinput = int(input("input numbers from 1 to 13:"))

if userinput>=1 and userinput<=13:

		if (userinput == 1):
			print("1. PhoneBook" )
	

			phoneBook = int(input("input numbers from 1 to 10:"))

			if (phoneBook>=1 and phoneBook<=10):
				if (phoneBook == 1 ):
					print("1. Search")
	
				if (phoneBook == 2 ):
					print("2.Service Nos.")
	

				if (phoneBook == 3 ):
					print("3. Add name")
	

				if (phoneBook == 4 ):
					print("4. Erase")
	
				if (phoneBook == 5 ):
					print("5. Edit")
	
				if (phoneBook == 6 ):
					print("6. Assign tone")
	
				if (phoneBook == 7 ):
					print("7. Send b'card")
	
				if (phoneBook == 8 ):
					print("8. Options")
					Options= int(input("input numbers from 1 to 2:"))

					if (Options>=1 and Options<=2):
						if (Options == 1 ):
							print("1. Type of view")
			
						if (Options == 2 ):
							print("2. Memory status")
				
		
				if (phoneBook == 9 ):
					print("9. Speed dials")
	
				if (phoneBook == 10 ):
					print("10. Voice tags")
	


	
		elif userinput == 2:
			print("2. Message" )

			Message = int(input("input numbers from 1 to 10:"))

			if (Message>=1 and Message<=10):
				if (Message == 1  ):
					print("1. Write messages")
		
				if (Message == 2 ):
					print("2. Inbox ")
		
				if (Message == 3  ):
					print("3. Outbox ")
		
				if (Message == 4  ):
					print("4. Picture messages ")
		
				if (Message == 5  ):
					print("5. Templates ")
		
				if (Message == 6  ):
					print("6. Smileys ")
		
				if (Message == 7 ):
					print("7. Message settings ")
		
					Message_settings = int(input("input numbers from 1 to 2:"))
					if ( Message_settings>=1 and Message_settings <=2):

						if (Message_settings == 1 ):
							print("1. Set1")
					
							Set1 = int(input("input numbers from 1 to 3:"))
							if (Set1>=1 and Set1 <=3):
								if (Set1 == 1 ):
									print("1. Message centre number")
						
								if (Set1 == 2 ):
									print("2. Message sent as")
						
								if (Set1 == 3 ):
									print("3. Message validity")
						
					
				
				
						if (Message_settings == 2 ):
							print("2. Set2")
					
							Set2 = int(input("input numbers from 1 to 3:"))
							if (Set2>=1 and Set2 <=3):
								if (Set2 == 1 ):
									print("1. Delivery reports")
						
								if (Set2 == 2 ):
									print("2. Reply via same center ")
						
								if (Set2 == 3 ):
									print("3. Character support")
							


			if (Message == 8 ):
				print("8. Info service")
	
			if (Message == 9 ):
				print("9. Voice mailbox number")
	
			if (Message ==  10 ):
				print("10. Service command editor ")


		elif (userinput == 3):
          		print("3. Chat")

		elif (userinput == 4):
            		print("4. Call Register")
            		call_register = int(input("Input numbers from 1 to 8: "))
            		if 1 <= callregister <= 8:
                		if call_register == 1:
                   			print("1. Missed calls")
                		if call_register == 2:
                    			print("2. Received calls")
                		if call_register == 3:
                    			print("3. Dialled numbers")
                		if call_register == 4:
                   			print("4. Erase recent call lists")
                		if call_register == 5:
                  			print("5. Show call duration")
                				show_call_duration = int(input("Input numbers from 1 to 5: "))
                    			if 1 <= show_call_duration <= 5:
                        			if show_call_duration == 1:
                            				print("1. Last call duration")
                        			if show_call_duration == 2:
                           				print("2. All calls' duration")
                        			if show_call_duration == 3:
                            				print("3. Received calls' duration")
                        			if show_call_duration == 4:
                            				print("4. Dialled calls' duration")
                        			if show_call_duration == 5:
                            				print("5. Clear timers")

                		if call_register == 6:
                   			print("6. Show call costs")
                    			show_call_cost = int(input("Input numbers from 1 to 3: "))
                    			if 1 <= show_call_cost <= 3:
                        			if show_call_cost == 1:
                           		 		print("1. Last call cost")
                        			if show_call_cost == 2:
                            				print("2. All calls' cost")
                        			if show_call_cost == 3:
                            				print("3. Clear counter3")

                		if call_register == 7:
                    			print("7. Call cost settings")
                    			call_cost_settings = int(input("Input numbers from 1 to 2: "))
                    			if 1 <= call_cost_settings <= 2:
                        			if call_cost_settings == 1:
                            				print("1. Call cost limit")
                        			if call_cost_settings == 2:
                            				print("2. Show costs in")

               		 	if call_register == 8:
                    			print("8. Prepaid credit")



	


