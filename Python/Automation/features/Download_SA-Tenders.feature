Feature: Download tenders from SA Tenders site using keywords
	@downloadSAtenders
	Scenario Outline: Testing windows automation
		Given this machine opens the "SA-Tenders" page
		  And this machine confirms that the webpage has the "page div" element
		  And this machine confirms that the "SA-Tenders Home" webpage is running and has a code "200"
		  And this machine waits until the webpage with title "SA-Tenders.co.za | Your free South African tender website" is done loading
		 When this machine enters "<Keywords>" into the "key word" input field
		  And this machine clicks on the "apply" button
		 Then this machine waits until the driver redirects to the "SA-Tenders Results" webpage
		  And this machine confirms that the "SA-Tenders Results" webpage is running and has a code "200"
		  And this machine confirms that the webpage has the "page div" element		  
		  And this machine waits until the webpage with title "keyword search | SA-Tenders.co.za" is done loading
		  And this machine downloads each SA-Tenders tender for "<Keywords>" and adds the record into the database

	Examples:
		|Keywords|
		|Ariba|
		|Asset Management|
		|Cyber Security|
		|Datawarehouse|
		|Education|
		|E-learning|
		|Email Security|
		|ERP|
		|HCM|
		|Human Capital Management|
		|Hybris|
		|Incident Management|
		|IT Service Management|
		|ITSM|
		|Lumira|
		|M-learning|
		|Online Training|
		|Oracle|
		|Oracle Backup|
		|Oracle Database|
		|Oracle Database Appliance|
		|Oracle Disaster Recovery|
		|Oracle EBS|
		|Oracle E-business Suite|
		|Oracle Enterprise Manager|
		|Oracle ExaData|
		|Oracle ExaLogic|
		|Oracle GoldenGate|
		|Oracle GRC|
		|Oracle Hyperion|
		|Oracle Linux|
		|Oracle MiniCluster|
		|Oracle ODA|
		|Oracle PrimaVera|
		|Oracle SOA Suite|
		|Oracle SuperCluster|
		|Oracle WebCentre|
		|Oracle ZFS Appliance|
		|Quality Assurance|
		|SAP Enterprise Resource Planning|
		|Security Awareness|
		|Software Security|
		|Success Factors|