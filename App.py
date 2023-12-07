
user_input = int(input("Input numbers from 1 to 13: "))

if 1 <= user_input <= 13:
    if user_input == 1:
        print("1. Phonebook")
        phone_book = int(input("Input numbers from 1 to 10: "))
        if 1 <= phone_book <= 10:
            if phone_book == 1:
                print("1. Search")
            elif phone_book == 2:
                print("2. Service Nos.")
            elif phone_book == 3:
                print("3. Add name")
            elif phone_book == 4:
                print("4. Erase")
            elif phone_book == 5:
                print("5. Edit")
            elif phone_book == 6:
                print("6. Assign tone")
            elif phone_book == 7:
                print("7. Send b'card")
            elif phone_book == 8:
                print("8. Options")
                options = int(input("Input numbers from 1 to 2: "))
                if 1 <= options <= 2:
                    if options == 1:
                        print("1. Type of view")
                    elif options == 2:
                        print("2. Memory status")
            elif phone_book == 9:
                print("9. Speed dials")
            elif phone_book == 10:
                print("10. Voice tags")

    elif user_input == 2:
        print("2. Messages")
        message = int(input("Input numbers from 1 to 10: "))
        if 1 <= message <= 10:
            if message == 1:
                print("1. Write messages")
            elif message == 2:
                print("2. Inbox")
            elif message == 3:
                print("3. Outbox")
            elif message == 4:
                print("4. Picture messages")
            elif message == 5:
                print("5. Templates")
            elif message == 6:
                print("6. Smileys")
            elif message == 7:
                print("7. Message settings")
                message_settings = int(input("Input numbers from 1 to 2: "))
                if 1 <= message_settings <= 2:
                    if message_settings == 1:
                        print("1. Set1")
                        set1 = int(input("Input numbers from 1 to 3: "))
                        if 1 <= set1 <= 3:
                            if set1 == 1:
                                print("1. Message centre number")
                            elif set1 == 2:
                                print("2. Message sent as")
                            elif set1 == 3:
                                print("3. Message validity")
                    elif message_settings == 2:
                        print("2. Set2")
                        set2 = int(input("Input numbers from 1 to 3: "))
                        if 1 <= set2 <= 3:
                            if set2 == 1:
                                print("1. Delivery reports")
                            elif set2 == 2:
                                print("2. Reply via same center")
                            elif set2 == 3:
                                print("3. Character support")

            elif message == 8:
                print("8. Info service")
            elif message == 9:
                print("9. Voice mailbox number")
            elif message == 10:
                print("10. Service command editor")

    elif user_input == 3:
        print("3. Chat")

    elif user_input == 4:
        print("4. Call Register")
        call_register = int(input("Input numbers from 1 to 8: "))
        if 1 <= call_register <= 8:
            if call_register == 1:
                print("1. Missed calls")
            elif call_register == 2:
                print("2. Received calls")
            elif call_register == 3:
                print("3. Dialled numbers")
            elif call_register == 4:
                print("4. Erase recent call lists")
            elif call_register == 5:
                print("5. Show call duration")
                show_call_duration = int(input("Input numbers from 1 to 5: "))
                if 1 <= show_call_duration <= 5:
                    if show_call_duration == 1:
                        print("1. Last call duration")
                    elif show_call_duration == 2:
                        print("2. All calls' duration")
                    elif show_call_duration == 3:
                        print("3. Received calls' duration")
                    elif show_call_duration == 4:
                        print("4. Dialled calls' duration")
                    elif show_call_duration == 5:
                        print("5. Clear timers")

            elif call_register == 6:
                print("6. Show call costs")
                show_call_cost = int(input("Input numbers from 1 to 3: "))
                if 1 <= show_call_cost <= 3:
                    if show_call_cost == 1:
                        print("1. Last call cost")
                    elif show_call_cost == 2:
                        print("2. All calls' cost")
                    elif show_call_cost == 3:
                        print("3. Clear counter3")

            elif call_register == 7:
                print("7. Call cost settings")
                call_cost_settings = int(input("Input numbers from 1 to 2: "))
                if 1 <= call_cost_settings <= 2:
                    if call_cost_settings == 1:
                        print("1. Call cost limit")
                    elif call_cost_settings == 2:
                        print("2. Show costs in")

            elif call_register == 8:
                print("8. Prepaid credit")

    elif user_input == 5:
        print("5. Tones")
        tones = int(input("Input numbers from 1 to 9: "))
        if 1 <= tones <= 9:
            if tones == 1:
                print("1. Ringing tone")
            elif tones == 2:
                print("2. Ringing volume")
            elif tones == 3:
                print("3. Incoming call alert")
            elif tones == 4:
                print("4. Composer")
            elif tones == 5:
                print("5. Message alert tones")
            elif tones == 6:
                print("6. Keypad tones")
            elif tones == 7:
                print("7. Warning and game tones")
            elif tones == 8:
                print("8. Vibrating alert")
            elif tones == 9:
                print("9. Screen saver")

    elif user_input == 6:
        print("6. Settings")
        settings = int(input("Input numbers from 1 to 4: "))
        if 1 <= settings <= 4:
            if settings == 1:
                print("1. Call settings")
                call_settings = int(input("Input numbers from 1 to 6: "))
                if 1 <= call_settings <= 6:
                    if call_settings == 1:
                        print("1. Automatic redial")
                    elif call_settings == 2:
                        print("2. Speed dialing")
                    elif call_settings == 3:
                        print("3. Call waiting options")
                    elif call_settings == 4:
                        print("4. Own number sending")
                    elif call_settings == 5:
                        print("5. Phone line in use")
                    elif call_settings == 6:
                        print("6. Automatic answer")

            elif settings == 2:
                print("2. Phone settings")
                phone_settings = int(input("Input numbers from 1 to 6: "))
                if 1 <= phone_settings <= 6:
                    if phone_settings == 1:
                        print("1. Language")
                    elif phone_settings == 2:
                        print("2. Cell info display")
                    elif phone_settings == 3:
                        print("3. Welcome")
                    elif phone_settings == 4:
                        print("4. Network selection")
                    elif phone_settings == 5:
                        print("5. Lights")
                    elif phone_settings == 6:
                        print("6. Confirm SIM service actions")

            elif settings == 3:
                print("3. Security settings")
                security_settings = int(input("Input numbers from 1 to 6: "))
                if 1 <= security_settings <= 6:
                    if security_settings == 1:
                        print("1. PIN code request")
                    elif security_settings == 2:
                        print("2. Call barring service")
                    elif security_settings == 3:
                        print("3. Fixed dialing")
                    elif security_settings == 4:
                        print("4. Closed user group")
                    elif security_settings == 5:
                        print("5. Phone security")
                    elif security_settings == 6:
                        print("6. Change access codes")

            elif settings == 4:
                print("4. Restore factory settings")

    elif user_input == 7:
        print("7. Call Divert")

    elif user_input == 8:
        print("8. Games")

    elif user_input == 9:
        print("9. Calculator")

    elif user_input == 10:
        print("10. Reminders")

    elif user_input == 11:
        print("11. Clock")
        clock = int(input("Input numbers from 1 to 6: "))
        if 1 <= clock <= 6:
            if clock == 1:
                print("1. Alarm clock")
            elif clock == 2:
                print("2. Clock settings")
            elif clock == 3:
                print("3. Date setting")
            elif clock == 4:
                print("4. Stopwatch")
            elif clock == 5:
                print("5. Countdown timer")
            elif clock == 6:
                print("6. Auto update of date and time")

    elif user_input == 12:
        print("12. Profiles")

    elif user_input == 13:
        print("13. SIM services")

else:
    print("Invalid input. Please enter a number between 1 and 13.")
