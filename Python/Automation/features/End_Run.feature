Feature: End running instance of Tender Spider
	@endSpiderRun
	Scenario: Send email if needed and close driver completely
		Given there is an email log, send the message 
		  And there is an email tally list, send the list
		  And end the spider instance