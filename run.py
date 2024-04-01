from booking import Booking

try:
    
    with Booking() as bot: #Creates a new instance of the chrome driver. Starts the service and then creates new instance of chrome driver.
        
        bot.land_first_page()
        print('Exiting...')
        bot.change_currency(currency='USD')
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2021-06-16',
                     check_out_date='2021-06-23')
        bot.select_adults(1)
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh() #A workaround to let our bot to grab the data properly
        bot.report_results()

except Exception as e:
    
    if 'in PATH' in str(e):

        print(

            'You are trying to run the bot from command line \n'
            'Please add to Path your Selenium Drivers \n'
            'Windows: \n'
            '       set PATH = %PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            'PATH = $PATH:/path/toyour/folder/ \n'      
        )

    else:

        raise 